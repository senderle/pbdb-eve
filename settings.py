MONGO_HOST = "db"
MONGO_PORT = 27017
MONGO_DBNAME = "eve"
RESOURCE_METHODS = ['GET', 'POST']
ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']
DATE_FORMAT = "%m/%d/%Y"
# DATE_FORMAT = (default: a, %d %b %Y %H:%M:%S)
# VERSIONING = True
# VERSIONING = (default: False)
# VERSIONS = suffix added to name of collection, defaults to '_versions'
# see also VERSION, VERSION_PARAM, LATEST_VERSION, VERSION_ID_SUFFIX


## 'allowed': [-1,0,1] or 'allowed': [1-10] limits to range of numbers
## could possibly do documentation through html instead -- is it necessary to
## incorporate it in Eve schema?
## add 'required' constraint to callNumber?
#

## or convert using Cerberus and validator and allow_unknown and lambda?
#def convertToInt(string):
#    integer = int(string)



schema = {
    'archiveHoldingDocument': {
        'type': 'string', ## defaults to string no matter what?
    },
    'callNumber': {
        'type': 'string',
        'unique': True,
        'required': True
    },
    'containingCollection': {
        'type': 'string'
    },
    'dataCataloger': {
        'type': 'string'
    },
    'dimensions': {
        'type': 'string' # could change if divided into 2 fields
    },
    #'dimensions': {
    #   'type': 'dict',
    #   'schema': {
    #       'length': {
    #           'type': 'number'
    #       },
    #       'width': {
    #           'type': 'number'
    #       }
    'documentType': {
        'type': 'string',
        'allowed': ['Playbill', 'London Stage', \
                    'Yorkshire Stage', 'Other Compendia', \
                    'Periodical Advertisement', 'Periodical Review']
    },
    'pageNumber': {
        'type': 'integer' # account for Roman numerals?
    },
    'periodicalTitle': {
        'type': 'string'
    },
    'persistentUrl': {
        'type': 'string'
    },
    'printedArea': {
        'type': 'string' # could change if divided into 2 fields
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
    },

    ################################ shows!

    'shows': {
        'type': 'list',
        'schema': {
            'type': 'dict',
            'schema': {
                'date': {
                    'type': 'datetime'
                },
                'doorsOpen': {
                    'type': 'string' # or datetime?
                },
                'location': {
                    'type': 'string'
                },
                'performanceBegins': {
                    'type': 'string'
                },
                'theaterCompany': {
                    'type': 'string'
                },
                'stageManager': {
                    'type': 'string'
                },
                'venue': {
                    'type': 'string'
                },
                'featuredAttractionsForShow': {
                    'type': 'list',
                    'schema': {
                        'type': 'dict',
                        'schema': {
                            'attraction': {
                                'type': 'string'
                            },
                            'isInterpolation': {
                                'type': 'boolean'
                            }
                        }
                    }
                },
                'notes': {
                    'type': 'list',
                    'schema': {
                        'type': 'string'
                    }
                },
                'occasions': {
                    'type': 'list',
                    'schema': {
                        'type': 'dict',
                        'schema': {
                            'occasionAsStated': {
                                'type': 'string'
                            },
                            'occasionType': {
                                'type': 'string',
                                'allowed': ["Command Performance", "Benefit Performance", \
                                            "Charitable Benefit Performance", "Occasional \
                                            Performance"],
                            },
                            'beneficiary': {
                                'type': 'list',
                                'schema': {
                                    'type': 'string',
                                    #'dependencies': {
                                    #    'occasionType': {
                                    #        ['Benefit Performance', 'Charitable Benefit \
                                    #        Performance']
                                    #    }
                                    #}
                                }
                            },
                            'occasioner': {
                                'type': 'list',
                                'schema': {
                                    'type': 'string',
                                    #'dependencies': {
                                    #    'occasionType': {
                                    #        ['Command Performance', 'Occasional Performance']
                                    #    }
                                    #}
                                }
                            }
                        }
                    }
                },
                'performances': {
                    'type': 'list',
                    'schema': {
                        'type': 'dict',
                        'schema': {
                            'genreClaim': {
                                'type': 'string'
                            },
                            'kindOfPerformance': {
                                'type': 'string',
                                'allowed': ["Main Piece", "After Piece"]
                            },
                            'orderOfPerformance': {
                                'type': 'integer'
                            },
                            'title': {
                                'type': 'string'
                            },
                            'contributors': {
                                'type': 'list',
                                'schema': {
                                    'type': 'dict',
                                    'schema': {
                                        'contributorName': {
                                            'type': 'string'
                                        },
                                        'contributorType': {
                                            'type': 'string'
                                            #'allowed': ["Playwright", "Composer", \
                                            #            "Scene Painter", "Dance Master", \
                                            #            "Set Designer"]
                                        }
                                    }
                                }
                            },
                            'featuredAttractions': {
                                'type': 'list',
                                'schema': {
                                    'type': 'string'
                                }
                            },
                            'performers': {
                                'type': 'list',
                                'schema': {
                                    'type': 'dict',
                                    'schema': {
                                        'performerName': {
                                            'type': 'string'
                                        },
                                        'roleNotes': {
                                            'type': 'string'
                                        },
                                        'role': {
                                            'type': 'string'
                                        },
                                        'newPerformerNotes': {
                                            'type': 'dict',
                                            'schema': {
                                                'newPerformer': {
                                                    'type': 'boolean'
                                                },
                                                'newPerformerOrigin': {
                                                    'type': 'string'
                                                },
                                                'newRole': {
                                                    'type': 'boolean'
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                },
                'ticketing': {
                    'type': 'dict',
                    'schema': {
                        'currency': {
                            'type': 'string'
                        },
                        'boxPrice': {
                            'type': 'number' # could also be float or integer
                        },
                        'secondBoxPrice': {
                            'type': 'number'
                        },
                        'pitPrice': {
                            'type': 'number'
                        },
                        'secondPitPrice': {
                            'type': 'number'
                        },
                        'galleryPrice': {
                            'type': 'number'
                        },
                        'secondGalleryPrice': {
                            'type': 'number'
                        },
                        'upperGalleryPrice': {
                            'type': 'number'
                        },
                        'secondUpperGalleryPrice': {
                            'type': 'number'
                        },
                        'toBeHad': {
                            'type': 'string'
                        },
                        'ticketingNotes': {
                            'type': 'string'
                        }
                    }
                }
            }
        }
    }
}

ephemeralRecord = {
    'item_title' : 'record',
    'additional_lookup': {
        'url': 'regex("[\w]+")',
        #'url': 'regex("[a-z0-9]{14}")',
        'field': 'callNumber',
    },
    'schema': schema
}

#shows = {
    #'url': 'ephemeralRecord/<regex("[\w]+"):callNumber>/shows'
#}

DOMAIN = {
    'ephemeralRecord': ephemeralRecord,
    }
