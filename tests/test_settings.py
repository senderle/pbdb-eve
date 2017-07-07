MONGO_HOST = 'db'
MONGO_PORT = 27017
MONGO_USERNAME = MONGO1_USERNAME = 'test_user'
MONGO_PASSWORD = MONGO1_PASSWORD = 'test_pw'
MONGO_DBNAME, MONGO1_DBNAME = 'eve_test', 'eve_test1'
ID_FIELD = '_id'

RESOURCE_METHODS = ['GET', 'POST', 'DELETE']
ITEM_METHODS = ['GET', 'PATCH', 'DELETE', 'PUT']

contacts = {
    'url': 'arbitraryurl',
    'cache_control': 'max-age=20,must-revalidate',
    'cache_expires': 20,
    'item_title': 'contact',
    'additional_lookup': {
        'url': 'regex("[\w]+")',   # to be unique field
        'field': 'ref'
    },
    'datasource': {'filter': {'username': {'$exists': False}}},
    'schema': {
        'ref': {
            'type': 'string',
            'minlength': 25,
            'maxlength': 25,
            'required': True,
            'unique': True,
        },
        'media': {
            'type': 'media'
        },
        'prog': {
            'type': 'integer'
        },
        'role': {
            'type': 'list',
            'allowed': ["agent", "client", "vendor"],
        },
        'rows': {
            'type': 'list',
            'schema': {
                'type': 'dict',
                'schema': {
                    'sku': {'type': 'string', 'maxlength': 10},
                    'price': {'type': 'integer'},
                },
            },
        },
        'alist': {
            'type': 'list',
            'items': [{'type': 'string'}, {'type': 'integer'}, ]
        },
        'location': {
            'type': 'dict',
            'schema': {
                'address': {'type': 'string'},
                'city': {'type': 'string', 'required': True}
            },
        },
        'born': {
            'type': 'datetime',
        }
    }
}

DOMAIN = {
    'contacts': contacts
    }
