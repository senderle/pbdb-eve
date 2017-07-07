import bcrypt
from eve import Eve
from eve.auth import HMACAuth
from flask import render_template, render_template_string, request, current_app as app
from hashlib import sha1
from eve.io.mongo import Validator
import hmac
import base64
import logging
import json
from schema import schema

class MyValidator(Validator):
    def _validate_documentation(self, documentation, field, value):
        if documentation:
            return
    def _validate_formType(self, formType, field, value):
        if formType:
            return

## HMAC Auth ###
class HMACAuth(HMACAuth):
     def check_auth(self, userid, hmac_hash, headers, data, allowed_roles,
                   resource, method):
         # use Eve's own db driver; no additional connections/resources are
         # used
         accounts = app.data.driver.db['accounts']
         lookup = {'userid': userid}
         user = accounts.find_one(lookup) #should be userid or id?
         if allowed_roles:
            # only retrieve a user if his roles match ``allowed_roles``
            lookup['roles'] = {'$in': allowed_roles}
         if user:
             secret_key = user['secret_key']
         # in this implementation we only hash request data, ignoring the
         # headers.
         #validator = hmac.new(str(secret_key).encode('utf-8'), None, sha1)
         #validator.update(str(data).encode('utf-8'))
         #print(secret_key)
         #print(str(secret_key).encode('utf-8'))
         #print(data)
         #print(str(data).encode('utf-8'))
         #print(hmac.new(str(secret_key).encode('utf-8'), str(data).encode('utf-8'), sha1).hexdigest())
         #print(validator.hexdigest())
         #print(hmac_hash)

         return user and  hmac.new(str(secret_key).encode('utf-8'), data, sha1).hexdigest() == hmac_hash


def create_user(documents):
    for document in documents:
        document['salt'] = bcrypt.gensalt()
        secret_key = document['secret_key']
        document['salt'] = bcrypt.gensalt().encode('utf-8')
        secret_key = document['secret_key'].encode('utf-8')
        document['secret_key'] = bcrypt.hashpw(secret_key, document['salt'])


def log_every_get(resource, request, payload):
    # custom INFO-level message is sent to the log file
    app.logger.info('We just answered to a GET request!')

def log_every_post(resource, request, payload):
    # custom INFO-level message is sent to the log file
    app.logger.info('We just answered to a POST request!')

def log_every_patch(resource, request, payload):
    # custom INFO-level message is sent to the log file
    app.logger.info('We just answered to a PATCH request!')

def log_every_put(resource, request, payload):
    # custom INFO-level message is sent to the log file
    app.logger.info('We just answered to a PUT request!')

def log_every_delete(resource, request, payload):
    # custom INFO-level message is sent to the log file
    app.logger.info('We just answered to a DELETE request!')



#app = Eve(auth=HMACAuth)
app = Eve(__name__, auth=HMACAuth, template_folder='templates', validator=MyValidator)
#app.on_insert_accounts += create_user
#app.on_post_GET += log_every_get
#app.on_post_POST += log_every_post
#app.on_post_PATCH += log_every_patch
#app.on_post_PUT += log_every_put
#app.on_post_DELETE += log_every_delete

@app.route('/form')
def something():
    return render_template('form.html')

@app.route('/main')
def main():
    return render_template('main.js')

@app.route('/schema.json')
def render_schema_json():
    schema_json = json.dumps(schema)
    return render_template_string(schema_json)


if __name__ == '__main__':

    # enable logging to 'app.log' file
    handler = logging.FileHandler('app.log')

    # set a custom log format, and add request
    # metadata to each log line
    handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s '
        '[in %(filename)s:%(lineno)d] -- ip: %(clientip)s, '
        'url: %(url)s, method:%(method)s'))

    app.logger.setLevel(logging.INFO)

    # append the handler to the default application logger
    app.logger.addHandler(handler)

    app.run(debug=True, host="0.0.0.0")
