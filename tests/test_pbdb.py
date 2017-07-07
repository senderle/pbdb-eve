import unittest
import eve
import string
import os
import simplejson as json
from datetime import datetime, timedelta
from pymongo import MongoClient
from test_settings import MONGO_PASSWORD, MONGO_USERNAME, \
    MONGO_DBNAME, DOMAIN, MONGO_HOST, MONGO_PORT
from flask import url_for

class ClientAppsTests(unittest.TestCase):

    def setUp(self, settings_file=None, url_converters=None):
        self.this_directory = os.path.dirname(os.path.realpath(__file__))

        if settings_file is None:
            # Load the settings file, using a robust path
            settings_file = os.path.join(self.this_directory, 'test_settings.py')

        self.connection = None

        self.setupDB()

        self.settings_file = settings_file
        self.app = eve.Eve(settings=self.settings_file,
                           url_converters=url_converters)

        self.test_client = self.app.test_client()

        self.domain = self.app.config['DOMAIN']

        self.known_resource = 'contacts'
        self.known_resource_url = ('/%s' %
                                   self.domain[self.known_resource]['url'])

    def tearDown(self):
        del self.app
        self.dropDB()


    def setupDB(self):
        self.connection = MongoClient(MONGO_HOST, MONGO_PORT)
        self.connection.drop_database(MONGO_DBNAME)
        if MONGO_USERNAME:
            self.connection[MONGO_DBNAME].add_user(MONGO_USERNAME,
                                                   MONGO_PASSWORD)



    def dropDB(self):
        self.connection = MongoClient(MONGO_HOST, MONGO_PORT)
        self.connection.drop_database(MONGO_DBNAME)
        self.connection.close()


    def post(self, url, data, headers=None, content_type='application/json'):
        if headers is None:
            headers = []
        headers.append(('Content-Type', content_type))
        r = self.test_client.post(url, data=json.dumps(data), headers=headers)
        return self.parse_response(r)

    def parse_response(self, r):
        try:
            v = json.loads(r.get_data())
        except json.JSONDecodeError:
            v = None
        return v, r.status_code

    def assert200(self, status):
        self.assertEqual(status, 200)

    def assert201(self, status):
        self.assertEqual(status, 201)

    def assert204(self, status):
        self.assertEqual(status, 204)

    def perform_post(self, data, valid_items=[0]):
        r, status = self.post(self.known_resource_url, data=data)
        self.assert201(status)
        self.assertPostResponse(r, valid_items)
        return r

    def assertPostItem(self, data, test_field, test_value):
        r = self.perform_post(data)
        item_id = r[self.domain[self.known_resource]['id_field']]
        item_etag = r[ETAG]
        db_value = self.compare_post_with_get(item_id, [test_field, ETAG])
        self.assertTrue(db_value[0] == test_value)
        self.assertTrue(db_value[1] == item_etag)

    def assertPostResponse(self, response, valid_items=[0], resource=None):
        if '_items' in response:
            results = response['_items']
        else:
            results = [response]

        id_field = self.domain[resource or self.known_resource]['id_field']

        for i in valid_items:
            item = results[i]
            self.assertTrue(STATUS in item)
            self.assertTrue(STATUS_OK in item[STATUS])
            self.assertFalse(ISSUES in item)
            self.assertTrue(id_field in item)
            self.assertTrue(LAST_UPDATED in item)
            self.assertTrue('_links' in item)
            self.assertItemLink(item['_links'], item[id_field])
            self.assertTrue(ETAG in item)

    def compare_post_with_get(self, item_id, fields):
        raw_r = self.test_client.get("%s/%s" % (self.known_resource_url,
                                                item_id))
        item, status = self.parse_response(raw_r)
        id_field = self.domain[self.known_resource]['id_field']
        self.assert200(status)
        self.assertTrue(id_field in item)
        self.assertTrue(item[id_field] == item_id)
        self.assertTrue(DATE_CREATED in item)
        self.assertTrue(LAST_UPDATED in item)
        self.assertEqual(item[DATE_CREATED], item[LAST_UPDATED])
        if isinstance(fields, list):
            return [item[field] for field in fields]
        else:
            return item[fields]

class testPlaybill(ClientAppsTests):
    def test_post_request(self):
        self.setUp()
        test_field = 'ref'
        test_value = '12345678'
        data = {test_field: test_value}
        data = json.dumps(data)
        url = 'http://159.203.127.128:5000/arbitraryurl'
        self.post(url, data, headers=None, content_type='application/json')
        response = self.test_client.get(url)
        self.assert200(response.status_code)
        

if __name__ == '__main__':
    unittest.main()
