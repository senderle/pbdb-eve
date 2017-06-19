from eve import Eve
from eve.auth import HMACAuth
from flask import current_app as app
from hashlib import sha1
import hmac
import base64
from eve.methods.post import post_internal
import bcrypt

#bcrypt.hashpw(password, account['password'])

class HMACAuth(HMACAuth):
     def check_auth(self, userid, hmac_hash, headers, data, allowed_roles,
                   resource, method):
         if userid == 'admin' and hmac_hash == hmac.new(str('1234567890'), str(data), sha1).hexdigest():
             return True
         # use Eve's own db driver; no additional connections/resources are
         # used
         accounts = app.data.driver.db['accounts']
         lookup = {'userid': userid}
         user = accounts.find_one(lookup) #should be userid or id?
         if allowed_roles:
            # only retrieve a user if his roles match ``allowed_roles``
            lookup['roles'] = {'$in': allowed_roles}
         if user:
             hashed_key = user['secret_key']
             secret_key = bcrypt.hashpw(hashed_key.encode('utf-8'), user['salt'].encode('utf-8'))
         # in this implementation we only hash request data, ignoring the
         # headers.
         return user and  hmac.new(str(secret_key), str(data), sha1).hexdigest() == hmac_hash


def create_user(documents):
    for document in documents:
        document['salt'] = bcrypt.gensalt()
        secret_key = document['secret_key']
        document['salt'] = bcrypt.gensalt().encode('utf-8')
        secret_key = document['secret_key'].encode('utf-8')
        document['secret_key'] = bcrypt.hashpw(secret_key, document['salt'])

#to set up app context:
#def test_connection(self, resource, method):
#    with app.app_context():

app = Eve(auth=HMACAuth)
app.on_insert_accounts += create_user

#payload = {
#    "userid": "admin",
#    "roles": ["admin"],
#    "secret_key": "1234567890"
#}

#with app.test_request_context():
#    x = post_internal('accounts', payload)
#    #print(x)

if __name__ == '__main__':

    app.run(debug=True, host="0.0.0.0")
