from eve import Eve
app = Eve()

from eve.auth import BasicAuth

#from eve.io.mongo import Validator

#class MyValidator(Validator):
#    def _validate_isodd(self, isodd, field, value):
#        if isodd and not bool(value & 1):
#            self._error(field, "Value must be an odd number")

#app = Eve(validator=MyValidator)
#def convert(request, lookup):
#    return int(lookup[field])

class Authenticate(BasicAuth):
    def check_auth(self, username, password, allowed_roles, resource, method):
        if resource == 'user' and method == 'GET':
            user = app.data.driver.db['user']
            user = user.find_one({'username': username, 'password': password})
            if user:
                return True
            else:
                return False
        elif resource == 'user' and method == 'POST':
            return username == 'admin' and password == 'admin'
        else:
            return True

#if field == "dimensions" | field == "printedArea":
#    return convert(request,lookup)

if __name__ == '__main__':
    # app = Eve(auth=Authenticate)
    app.run(host="0.0.0.0")
