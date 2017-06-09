
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
        },
        'shows': {
            'type': 'dict', //originally 'list'
            'schema': {
                'type': 'dict',
                'schema': {
                    'date': {
                        'type': 'string'
                    },
                    'doorsOpen': {
                        'type': 'string'
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
                    'venue': {
                        'type': 'string'
                    },
                    'featuredAttractionsForShow': {
                        'type': 'list',
                        'schema': {
                            'type': 'string'
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
                                    'type': 'string'
                                },
                                'beneficiary': {
                                    'type': 'list',
                                    'schema': {
                                        'type': 'string'
                                    }
                                },
                                'occasioner': {
                                    'type': 'list',
                                    'schema': {
                                        'type': 'string'
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
                                    'type': 'string'
                                },
                                'orderOfPerformance': {
                                    'type': 'string'
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
                                            'performerNotes': {
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
                            'boxPrice': {
                                'type': 'string'
                            },
                            'costsOrFees': {
                                'type': 'string'
                            },
                            'currency': {
                                'type': 'string'
                            },
                            'galleryPrice': {
                                'type': 'string'
                            },
                            'toBeHad': {
                                'type': 'string'
                            },
                            'totalReceipts': {
                                'type': 'string'
                            },
                            'upperGalleryPrice': {
                                'type': 'string'
                            }
                        }
                    }
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
