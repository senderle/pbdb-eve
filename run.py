# import bcrypt # need to install ``pip install py-bcrypt`` -- add to requirements.txt?

from eve import Eve

from eve.auth import BasicAuth
from flask import current_app as app

class BCryptAuth(BasicAuth):
    def check_auth(self, username, password, allowed_roles, resource, method):
        # use Eve's own db driver; no additional connections/resources are used
        accounts = app.data.driver.db['accounts']
        account = accounts.find_one({'username': username})
        return account and \
            bcrypt.hashpw(password, account['password']) == account['password']

#class Authenticate(BasicAuth):
#    def check_auth(self, username, password, allowed_roles, resource, method):
#        if resource == 'user' and method == 'GET':
#            user = app.data.driver.db['user']
#            user = user.find_one({'username': username, 'password': password})
#            if user:
#                return True
#            else:
#                return False
#        elif resource == 'user' and method == 'POST':
#            return username == 'admin' and password == 'admin'
#        else:
#            return True


if __name__ == '__main__':
    # app = Eve(auth=Authenticate)
    app = Eve(auth=BCryptAuth)
    app.run(host="0.0.0.0")
