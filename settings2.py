ephemeralRecord = {
    'schema': {
        'archiveHoldingDocument': {
            'type': 'string'
        },
        'callNumber': {
            'type': 'string'
        },
        'containingCollection': {
            'type': 'string'
        },
        'dataCataloger': {
            'type': 'string'
        },
        'dimensions': {
            'type': 'string'
        },
        'documentType': {
            'type': 'string'
        },
        'periodicalTitle': {
            'type': 'string'
        },
        'persistentUrl': {
            'type': 'string'
        },
        'printedArea': {
            'type': 'string'
        },
        'advertisements': {
            'type': 'list',
            'schema': {
                'type': 'string'
            }
        },
        'announcements': {
            'type': 'list',
            'schema': {
                'type': 'string'
            }
        },
        'documentPrinter': {
            'type': 'dict',
            'schema': {
                'location': {
                    'type': 'string'
                },
                'name': {
                    'type': 'string'
                }
            }
        }
    }
}

eve_settings = {
    'MONGO_HOST': 'localhost',
    'MONGO_DBNAME': 'testing',
    'RESOURCE_METHODS': ['GET', 'POST', 'DELETE'],
    'BANDWIDTH_SAVER': False,
    'DOMAIN': {
        'ephemeralRecord': ephemeralRecord,
    },
}

#####################
# barebones version

MONGO_HOST = "db"
MONGO_PORT = 27017
MONGO_DBNAME = "eve"

DOMAIN = {
    'ephemeralRecord': {
        'schema': {
            'archiveHoldingDocument': {
                'type': 'string'
            },
            'callNumber': {
                'type': 'string'
            },
            'containingCollection': {
                'type': 'string'
            },
            'dataCataloger': {
                'type': 'string'
            },
            'dimensions': {
                'type': 'string'
            },
            'documentType': {
                'type': 'string'
            },
            'periodicalTitle': {
                'type': 'string'
            },
            'persistentUrl': {
                'type': 'string'
            },
            'printedArea': {
                'type': 'string'
            },
            'advertisements': {
                'type': 'list',
                'schema': {
                    'type': 'string'
                }
            },
            'announcements': {
                'type': 'list',
                'schema': {
                    'type': 'string'
                }
            },
            'documentPrinter': {
                'type': 'dict',
                'schema': {
                    'location': {
                        'type': 'string'
                    },
                    'name': {
                        'type': 'string'
                    }
                }
            }
        }
    }
}


RESOURCE_METHODS = ['GET', 'POST']
