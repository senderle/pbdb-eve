# import bcrypt # need to install ``pip install py-bcrypt`` -- add to requirements.txt?
import bcrypt
from eve import Eve

from eve.auth import BasicAuth
from flask import current_app as app

class BCryptAuth(BasicAuth):
    def check_auth(self, username, password, allowed_roles, resource, method):
        # use Eve's own db driver; no additional connections/resources are used
        accounts = app.data.driver.db['accounts']
        lookup = {'username': username}
        #account['password'] = bcrypt.hashpw(password, bcrypt.gensalt())
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



if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
