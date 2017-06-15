# import bcrypt # need to install ``pip install py-bcrypt`` -- add to requirements.txt?
import bcrypt
from eve import Eve
from eve.auth import BasicAuth, HMACAuth
from flask import current_app as app
from hashlib import sha1
import hmac


##### HMAC Auth #####
class HMACAuth(HMACAuth):
    def check_auth(self, username, hmac_hash, headers, data, allowed_roles,
                   resource, method):
        # use Eve's own db driver; no additional connections/resources are
        # used
        accounts = app.data.driver.db['accounts']
        user = accounts.find_one({'username': username}) #should be userid or id?
        if user:
            secret_key = user['secret_key']
        # in this implementation we only hash request data, ignoring the
        # headers.
        print hmac_hash
        return user and \
            hmac.new(str(secret_key), str(data), sha1).hexdigest() == \
                hmac_hash

app = Eve(auth=HMACAuth)


#to set up app context:
#def test_connection(self, resource, method):
#    with app.app_context():



if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
