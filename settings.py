MONGO_HOST = "db"
MONGO_PORT = 27017
MONGO_DBNAME = "eve"
RESOURCE_METHODS = ['GET', 'POST']
ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']
# PUBLIC_METHODS = ['GET']
# PUBLIC_ITEM_METHODS = ['GET']
DATE_FORMAT = "%m/%d/%Y"
# DATE_FORMAT = (default: a, %d %b %Y %H:%M:%S)
# VERSIONING = True
# VERSIONING = (default: False)
# VERSIONS = suffix added to name of collection, defaults to '_versions'
# see also VERSION, VERSION_PARAM, LATEST_VERSION, VERSION_ID_SUFFIX


## 'allowed': [-1,0,1] or 'allowed': [1-10] limits to range of numbers

schema = {
    'archiveHoldingDocument': {
        'type': 'string',
        'maxlength': 200,
        'documentation': "The name of the library or archive that holds the document."
    },
    'callNumber': {
        'type': 'string',
        'unique': True,
        'required': True,
        'maxlength': 200,
        'documentation': "The call number of the document as specified by the holding institution."
    },
    'containingCollection': {
        'type': 'string',
        'maxlength': 200,
        'documentation': "The name of the collection the document resides in."
    },
    'dataCataloger': {
        'type': 'string',
        'maxlength': 200,
        'documentation': "Your unique identifier as a cataloger. May be your name, your initials, \
                        or some other unique word or phrase of your choice."
    },
    'dimensions': {
        'type': 'string', # could change if divided into 2 fields
        'maxlength': 200, # will probably change?
        'documentation': "A comma-separated 2-tuple containing the \
                        length and width of the document in centimeters."
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
                    'Periodical Advertisement', 'Periodical Review'],
        'maxlength': 200,
        'documentation': "The document type. One of Playbill / London Stage / Yorkshire Stage / \
                        Other Compendia / Periodical Advertisement / Periodical Review"
    },
    'pageNumber': {
        'type': 'integer', # account for Roman numerals?
        'documentation': "If the record is contained in another paginated document, the starting page of \
                        the record in that document."
    },
    'periodicalTitle': {
        'type': 'string',
        'maxlength': 200,
        'documentation': "The name of the containing periodical (e.g. for advertisements). We may develop \
                        a controlled vocabulary for this."
    },
    'persistentUrl': {
        'type': 'string',
        'maxlength': 200,
        'documentation': "A persistent URL where identifying information about the document may be found."
    },
    'printedArea': {
        'type': 'string', # could change if divided into 2 fields (see 'dimensions')
        'maxlength': 200, # may also have to change
        'documentation': "A comma-separated 2-tuple containing the length and width of the printed area of \
                        the document in centimeters."
    },
    'advertisements': {
        'type': 'list',
        'schema': {
            'type': 'string',
            'maxlength': 1000,
            'documentation': "The text of each advertisement, as given by the document, to be entered at the \
                            discretion of the cataloger." #fixed spelling mistake 'discretion'
        }
    },
    'announcements': {
        'type': 'list',
        'schema': {
            'type': 'string',
            'maxlength': 1000,
            'documentation': "The text of each announcement, as given by the document, to be entered at the \
                            discretion of the cataloger." #same spelling mistake as above, changed 'advertisement' to 'announcement'
        }
    },
    'documentPrinter': {
        'type': 'dict',
        'schema': {
            'location': {
                'type': 'string',
                'maxlength': 200,
                'documentation': "The name of the printer."
            },
            'name': {
                'type': 'string',
                'maxlength': 200,
                'documentation': "The city where the document was printed."
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
                    'type': 'datetime',
                    'documentation': "The exact date of the performance. For ranges of dates, create a separate Show \
                                    Record for each date."
                },
                'doorsOpen': {
                    'type': 'string', # or datetime?
                    'maxlength': 200,
                    'documentation': "The time when doors open, if listed, using \
                                    a 24-hour clock."
                },
                'location': {
                    'type': 'string',
                    'maxlength': 200,
                    'documentation': "The geographical location of the performance, exactly as given by the document."
                },
                'performanceBegins': {
                    'type': 'string',
                    'maxlength': 200,
                    'documentation': "The time when the performance begins, \
                                    using a 24-hour clock."
                },
                'theaterCompany': {
                    'type': 'string',
                    'maxlength': 200,
                    'documentation': "The name of the theater company, exactly \
                                    as given by the document."
                },
                'stageManager': {
                    'type': 'string',
                    'maxlength': 200,
                    'documentation': "The name of the stage manager, if present \
                                    in the document, exactly as given."
                },
                'venue': {
                    'type': 'string',
                    'maxlength': 200,
                    'documentation': "The venue of the performance, exactly as given by the document."
                },
                'featuredAttractionsForShow': {
                    'type': 'string',
                    'maxlength': 200,
                    'documentation': "Any featured attractions described in the \
                                    document, exactly as given."
                },
                'notes': {
                    'type': 'list',
                    'schema': {
                        'type': 'string',
                        'maxlength': 1000,
                        'documentation':  "Notes describing compelling or otherwise \
                                        important details from the document that \
                                        will not be captured by any other field."
                    }
                },
                'occasions': {
                    'type': 'list',
                    'schema': {
                        'type': 'dict',
                        'schema': {
                            'occasionAsStated': {
                                'type': 'string',
                                'maxlength': 200,
                                'documentation': "The occasion for an occasional performance, \
                                                exactly as given by the document."
                            },
                            'occasionType': {
                                'type': 'string',
                                'allowed': ["Command Performance", "Benefit Performance", \
                                            "Charitable Benefit Performance", "Occasional \
                                            Performance"],
                                'maxlength': 200,
                                'documentation': "The type of occasional performance. One of Command performance / \
                                                Benefit Performance / Charitable Benefit Performance / Occasional Performance."
                            },
                            'beneficiary': {
                                'type': 'list',
                                'schema': {
                                    'type': 'string',
                                    'maxlength': 200,
                                    'documentation': "One or more people, ideally denoted by \
                                                    URIs from a controlled vocabulary."
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
                                    'maxlength': 200,
                                    'documentation': "One or more people, ideally denoted by \
                                                    URIs from a controlled vocabulary."
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
                                'type': 'string',
                                'maxlength': 200,
                                'documentation': "The genre claim, exactly as given by the document."
                            },
                            'kindOfPerformance': {
                                'type': 'string',
                                'allowed': ["Main Piece", "After Piece"],
                                'maxlength': 200,
                                'documentation': "Kind of performance. May either be \
                                                Main Piece or After Piece."
                            },
                            'orderOfPerformance': {
                                'type': 'integer',
                                'documentation': "An integer describing the position of \
                                                this performance within the larger show. \
                                                Starts at 1. Interpolations should be \
                                                numbered in order, and are assumed to \
                                                occur within the last full piece listed."
                            },
                            'title': {
                                'type': 'string',
                                'maxlength': 200,
                                'documentation': "The title of the work being performed, \
                                                exactly as given by the document."
                            },
                            'contributors': {
                                'type': 'list',
                                'schema': {
                                    'type': 'dict',
                                    'schema': {
                                        'contributorName': {
                                            'type': 'string',
                                            'maxlength': 200,
                                            'documentation': "The name of the contributor."
                                        },
                                        'contributorType': {
                                            'type': 'string',
                                            'maxlength': 200,
                                            'documentation': "The type of contributor (e.g. Scene Painter, Director, etc.)."
                                            #'allowed': ["Playwright", "Composer", \
                                            #            "Scene Painter", "Dance Master", \
                                            #            "Set Designer"]
                                        }
                                    }
                                }
                            },
                            'performanceFeaturedAttraction': {
                                'type': 'list',
                                'schema': {
                                    'type': 'dict',
                                    'schema': {
                                        'attraction': {
                                            'type': 'string',
                                            'maxlength': 200,
                                            'documentation': "Any featured attractions described in the \
                                                            document, exactly as given."
                                        },
                                        'isInterpolation': {
                                            'type': 'boolean',
                                            'documentation': "An indicator set to true if the document \
                                                            identifies this as an interpolation \
                                                            within the larger performance."
                                        }
                                    }
                                }
                            },
                            'performers': {
                                'type': 'list',
                                'schema': {
                                    'type': 'dict',
                                    'schema': {
                                        'performerName': {
                                            'type': 'string',
                                            'maxlength': 200,
                                            'documentation': "The name of the performer."
                                        },
                                        'roleNotes': {
                                            'type': 'string',
                                            'maxlength': 200,
                                            'documentation': "Notes on the role or performer, exactly as given by the document."
                                        },
                                        'role': {
                                            'type': 'string',
                                            'maxlength': 200,
                                            'documentation': "The name of the performer's role."
                                        },
                                        'newPerformerNotes': {
                                            'type': 'dict',
                                            'schema': {
                                                'newPerformer': {
                                                    'type': 'boolean',
                                                    'documentation': "An indicator set to true if the document \
                                                                    identifies this as the performer's first \
                                                                    appearance at this venue."
                                                },
                                                'newPerformerOrigin': {
                                                    'type': 'string',
                                                    'maxlength': 200,
                                                    'documentation': "The performer's previous venue, if given \
                                                                    by the document, and if the document \
                                                                    identifies this as the performer's first \
                                                                    appearance at this venue."
                                                },
                                                'newRole': {
                                                    'type': 'boolean',
                                                    'documentation': "An indicator set to true if the document \
                                                                    identifies this as the performer's first \
                                                                    appearance in this role."
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
                            'type': 'string',
                            'maxlength': 200,
                            'documentation': "The national currency in use. Currently one of UK / US."
                        },
                        'boxPrice': {
                            'type': 'number', # could also be float or integer
                            'documentation': "The cost of a box seat, as measured using the smallest possible unit of currency."
                        },
                        'secondBoxPrice': {
                            'type': 'number',
                            'documentation': "The cost of a second box seat, as measured using the smallest possible unit \
                                            of currency."
                        },
                        'pitPrice': {
                            'type': 'number',
                            'documentation': "The cost of a pit seat, as \
                                            measured using the smallest possible unit \
                                            of currency."
                        },
                        'secondPitPrice': {
                            'type': 'number',
                            'documentation': "The cost of a second pit seat, as \
                                            measured using the smallest possible unit \
                                            of currency."
                        },
                        'galleryPrice': {
                            'type': 'number',
                            'documentation': "The cost of a second pit seat, as measured using the smallest possible unit \
                                            of currency."
                        },
                        'secondGalleryPrice': {
                            'type': 'number',
                            'documentation': "The cost of a second gallery seat, as measured using the smallest possible \
                                            unit of currency."
                        },
                        'upperGalleryPrice': {
                            'type': 'number',
                            'documentation': "The cost of a upper gallery seat, as measured using the smallest possible \
                                            unit of currency."
                        },
                        'secondUpperGalleryPrice': {
                            'type': 'number',
                            'documentation': "The cost of a second upper gallery seat, \
                                            as measured using the smallest possible \
                                            unit of currency."
                        },
                        'toBeHad': {
                            'type': 'string',
                            'maxlength': 200,
                            'documentation': "The name of the ticketing agent or agents."
                        },
                        'ticketingNotes': {
                            'type': 'string',
                            'maxlength': 200,
                            'documentation': "Additional notes about ticketing."
                        }
                    }
                }
            }
        }
    }
}


accountschema =  {
    'username': {
        'type': 'string',
        'required': True,
        'unique': True,
        },
    'password': {
        'type': 'string',
        'required': True,
    },
},

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

accounts = {
    'additional_lookup': {
        'url': 'regex("[\w]+")',
        'field': 'username',
    },

    # We also disable endpoint caching as we don't want client apps to
    # cache account data.
    'cache_control': '',
    'cache_expires': 0,

    'schema': accountschema
}

DOMAIN = {
    'ephemeralRecord': ephemeralRecord,
    'accounts': accounts
    }
