"""
Do not modify this file. It is generated from the Swagger specification.

Container module for JSONSchema definitions.
This does not include inlined definitions.

The pretty-printing functionality provided by the json module is superior to
what is provided by pformat, hence the use of json.loads().
"""
import json

# When no schema is provided in the definition, we use an empty schema
__UNSPECIFIED__ = {}

data_service = json.loads("""
{
    "properties": {
        "domain": {
            "properties": {
                "id": {
                    "type": "integer"
                },
                "name": {
                    "type": "string",
                    "uniqueItems": true
                }
            },
            "type": "object",
            "x-scope": [
                ""
            ]
        },
        "id": {
            "type": "integer"
        },
        "model_config": {
            "type": "string"
        },
        "repo_name": {
            "type": "string"
        }
    },
    "type": "object"
}
""")

deployment_status = json.loads("""
{
    "properties": {
        "flow": {
            "properties": {
                "id": {
                    "type": "integer"
                },
                "name": {
                    "type": "string"
                },
                "product": {
                    "properties": {
                        "id": {
                            "type": "integer"
                        },
                        "name": {
                            "type": "string",
                            "uniqueItems": true
                        }
                    },
                    "type": "object",
                    "x-scope": [
                        "",
                        "#/definitions/flow_version",
                        "#/definitions/flow"
                    ]
                }
            },
            "type": "object",
            "x-scope": [
                ""
            ]
        },
        "id": {
            "type": "integer"
        },
        "prod_version": {
            "properties": {
                "flow": {
                    "properties": {
                        "id": {
                            "type": "integer"
                        },
                        "name": {
                            "type": "string"
                        },
                        "product": {
                            "properties": {
                                "id": {
                                    "type": "integer"
                                },
                                "name": {
                                    "type": "string",
                                    "uniqueItems": true
                                }
                            },
                            "type": "object",
                            "x-scope": [
                                "",
                                "#/definitions/flow_version",
                                "#/definitions/flow"
                            ]
                        }
                    },
                    "type": "object",
                    "x-scope": [
                        "",
                        "#/definitions/flow_version"
                    ]
                },
                "flow_json": {
                    "type": "string"
                },
                "id": {
                    "type": "integer"
                },
                "version": {
                    "type": "number"
                }
            },
            "type": "object",
            "x-scope": [
                ""
            ]
        },
        "stage_version": {
            "properties": {
                "flow": {
                    "properties": {
                        "id": {
                            "type": "integer"
                        },
                        "name": {
                            "type": "string"
                        },
                        "product": {
                            "properties": {
                                "id": {
                                    "type": "integer"
                                },
                                "name": {
                                    "type": "string",
                                    "uniqueItems": true
                                }
                            },
                            "type": "object",
                            "x-scope": [
                                "",
                                "#/definitions/flow_version",
                                "#/definitions/flow"
                            ]
                        }
                    },
                    "type": "object",
                    "x-scope": [
                        "",
                        "#/definitions/flow_version"
                    ]
                },
                "flow_json": {
                    "type": "string"
                },
                "id": {
                    "type": "integer"
                },
                "version": {
                    "type": "number"
                }
            },
            "type": "object",
            "x-scope": [
                ""
            ]
        }
    },
    "type": "object"
}
""")

domain = json.loads("""
{
    "properties": {
        "id": {
            "type": "integer"
        },
        "name": {
            "type": "string",
            "uniqueItems": true
        }
    },
    "type": "object"
}
""")

flow = json.loads("""
{
    "properties": {
        "id": {
            "type": "integer"
        },
        "name": {
            "type": "string"
        },
        "product": {
            "properties": {
                "id": {
                    "type": "integer"
                },
                "name": {
                    "type": "string",
                    "uniqueItems": true
                }
            },
            "type": "object",
            "x-scope": [
                "",
                "#/definitions/flow_version",
                "#/definitions/flow"
            ]
        }
    },
    "type": "object"
}
""")

flow_version = json.loads("""
{
    "properties": {
        "flow": {
            "properties": {
                "id": {
                    "type": "integer"
                },
                "name": {
                    "type": "string"
                },
                "product": {
                    "properties": {
                        "id": {
                            "type": "integer"
                        },
                        "name": {
                            "type": "string",
                            "uniqueItems": true
                        }
                    },
                    "type": "object",
                    "x-scope": [
                        "",
                        "#/definitions/flow_version",
                        "#/definitions/flow"
                    ]
                }
            },
            "type": "object",
            "x-scope": [
                "",
                "#/definitions/flow_version"
            ]
        },
        "flow_json": {
            "type": "string"
        },
        "id": {
            "type": "integer"
        },
        "version": {
            "type": "number"
        }
    },
    "type": "object"
}
""")

product = json.loads("""
{
    "properties": {
        "id": {
            "type": "integer"
        },
        "name": {
            "type": "string",
            "uniqueItems": true
        }
    },
    "type": "object"
}
""")

task = json.loads("""
{
    "properties": {
        "domain": {
            "properties": {
                "id": {
                    "type": "integer"
                },
                "name": {
                    "type": "string",
                    "uniqueItems": true
                }
            },
            "type": "object",
            "x-scope": [
                ""
            ]
        },
        "env_variables": {
            "type": "string"
        },
        "framework": {
            "type": "string"
        },
        "id": {
            "type": "integer"
        },
        "input_schema": {
            "type": "string"
        },
        "is_bootstrapped": {
            "type": "boolean"
        },
        "is_published": {
            "type": "boolean"
        },
        "name": {
            "type": "string"
        },
        "output_schema": {
            "type": "string"
        },
        "path": {
            "type": "string"
        },
        "port": {
            "type": "string"
        },
        "repo_name": {
            "type": "string"
        }
    },
    "type": "object"
}
""")

