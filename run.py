import bcrypt
from eve import Eve
from eve.auth import HMACAuth
from flask import render_template, request, current_app as app
from hashlib import sha1
import hmac
import base64
import logging
#from eve.methods.post import post_internal


#bcrypt.hashpw(password, account['password'])

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
        #     hashed_key = user['secret_key']
        #     secret_key = bcrypt.hashpw(hashed_key.encode('utf-8'), user['salt'])
         # in this implementation we only hash request data, ignoring the
         # headers.
         return user and  hmac.new(str(secret_key).encode('utf-8'), str(userid).encode('utf-8'), sha1).hexdigest() == hmac_hash


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

def oplog_extras(resource, entries):
    for entry in entries:
        entry['extra'] = {'r': 'resource'}

#to set up app context:
#def test_connection(self, resource, method):
#    with app.app_context():

#app = Eve(auth=HMACAuth)
app = Eve(__name__, auth=HMACAuth, template_folder='templates')
#app.on_insert_accounts += create_user
#app.on_post_GET += log_every_get
#app.on_post_POST += log_every_post
#app.on_post_PATCH += log_every_patch
#app.on_post_PUT += log_every_put
#app.on_post_DELETE += log_every_delete
#app.on_oplog_push += oplog_extras
#payload = {
#    "userid": "admin",
#    "roles": ["admin"],
#    "secret_key": "1234567890"
#}

def hashing(secret_key, userid):
    hmac_hash = hmac.new(str(secret_key).encode('utf-8'), str(userid).encode('utf-8'), sha1).hexdigest()
    return hmac_hash

@app.route('/something')
def something():
    userid = 'test'
    secret_key = '12345'
    hmac_hash = hashing(secret_key, userid)
    data = {'callNumber': '132', 'archiveHoldingDocument': 'London'} #dict??
    return render_template('something.html', userid=userid, data=data)


if __name__ == '__main__':

    # enable logging to 'app.log' file
    handler = logging.FileHandler('app.log')

    # set a custom log format, and add request
    # metadata to each log line
    handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s '
        '[in %(filename)s:%(lineno)d] -- ip: %(clientip)s, '
        'url: %(url)s, method:%(method)s'))

    # the default log level is set to WARNING, so
    # we have to explictly set the logging level
    # to INFO to get our custom message logged.
    app.logger.setLevel(logging.INFO)

    # append the handler to the default application logger
    app.logger.addHandler(handler)

    app.run(debug=True, host="0.0.0.0")
