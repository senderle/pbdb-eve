# import bcrypt # need to install ``pip install py-bcrypt`` -- add to requirements.txt?
import bcrypt
from eve import Eve
from eve.auth import BasicAuth, HMACAuth
from flask import current_app as app
from hashlib import sha1
import hmac


### BCrypt Auth ######
class BCryptAuth(BasicAuth):
    def check_auth(self, username, password, allowed_roles, resource, method):
        # use Eve's own db driver; no additional connections/resources are used
        accounts = app.data.driver.db['accounts']
        lookup = {'username': username}
        if allowed_roles:
            lookup['roles'] = {'$in': allowed_roles}
        account = accounts.find_one(lookup)
        return account and \
            bcrypt.hashpw(password.encode('utf-8'), account['salt'].encode('utf-8')) == account['password']

def create_user(documents):
    for document in documents:
        document['salt'] = bcrypt.gensalt().encode('utf-8')
        password = document['password'].encode('utf-8')
        document['password'] = bcrypt.hashpw(password, document['salt'])


app = Eve(auth=BCryptAuth)
app.on_insert_accounts += create_user


##### HMAC Auth #####
class HMACAuth(HMACAuth):
    def check_auth(self, userid, hmac_hash, headers, data, allowed_roles,
                   resource, method):
        # use Eve's own db driver; no additional connections/resources are
        # used
        accounts = app.data.driver.db['accounts']
        user = accounts.find_one({'userid': userid}) #should be userid or id?
        if user:
            secret_key = user['secret_key']
        # in this implementation we only hash request data, ignoring the
        # headers.
        print hmac_hash
        return user and \
            hmac.new(str(secret_key), str(data), sha1).hexdigest() == \
                hmac_hash

app = Eve(auth=HMACAuth)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
