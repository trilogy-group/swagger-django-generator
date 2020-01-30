"""
Do not modify this file. It is generated from the Swagger specification.
"""
import json
from apitools.datagenerator import DataGenerator

import new_app.schemas as schemas


class AbstractStubClass(object):
    """
    Implementations need to be derived from this class.
    """

    # get_domains -- Synchronisation point for meld
    @staticmethod
    def get_domains(request, *args, **kwargs):
        """
        :param request: An HttpRequest
        """
        raise NotImplementedError()

    # post_domains -- Synchronisation point for meld
    @staticmethod
    def post_domains(request, body, *args, **kwargs):
        """
        :param request: An HttpRequest
        :param body: A dictionary containing the parsed and validated body
        :type body: dict
        """
        raise NotImplementedError()

    # get_domainsiddataservice -- Synchronisation point for meld
    @staticmethod
    def get_domainsiddataservice(request, id, *args, **kwargs):
        """
        :param request: An HttpRequest
        :param id: 
        :type id: integer
        """
        raise NotImplementedError()

    # post_domainsiddataserviceinit -- Synchronisation point for meld
    @staticmethod
    def post_domainsiddataserviceinit(request, body, id, *args, **kwargs):
        """
        :param request: An HttpRequest
        :param body: A dictionary containing the parsed and validated body
        :type body: dict
        :param id: 
        :type id: integer
        """
        raise NotImplementedError()

    # get_flows -- Synchronisation point for meld
    @staticmethod
    def get_flows(request, product_name=None, *args, **kwargs):
        """
        :param request: An HttpRequest
        :param product_name: (optional) name of the product
        :type product_name: string
        """
        raise NotImplementedError()

    # post_flows -- Synchronisation point for meld
    @staticmethod
    def post_flows(request, body, *args, **kwargs):
        """
        :param request: An HttpRequest
        :param body: A dictionary containing the parsed and validated body
        :type body: dict
        """
        raise NotImplementedError()

    # get_flowsid -- Synchronisation point for meld
    @staticmethod
    def get_flowsid(request, id, *args, **kwargs):
        """
        :param request: An HttpRequest
        :param id: 
        :type id: integer
        """
        raise NotImplementedError()

    # put_flowsid -- Synchronisation point for meld
    @staticmethod
    def put_flowsid(request, body, id, *args, **kwargs):
        """
        :param request: An HttpRequest
        :param body: A dictionary containing the parsed and validated body
        :type body: dict
        :param id: 
        :type id: integer
        """
        raise NotImplementedError()

    # put_flowsiddeployenv -- Synchronisation point for meld
    @staticmethod
    def put_flowsiddeployenv(request, body, id, env, *args, **kwargs):
        """
        :param request: An HttpRequest
        :param body: A dictionary containing the parsed and validated body
        :type body: dict
        :param id: 
        :type id: integer
        :param env: 
        :type env: string
        """
        raise NotImplementedError()

    # get_flowsidloadversion -- Synchronisation point for meld
    @staticmethod
    def get_flowsidloadversion(request, id, version, *args, **kwargs):
        """
        :param request: An HttpRequest
        :param id: 
        :type id: integer
        :param version: 
        :type version: string
        """
        raise NotImplementedError()

    # get_flowsidstatus -- Synchronisation point for meld
    @staticmethod
    def get_flowsidstatus(request, id, *args, **kwargs):
        """
        :param request: An HttpRequest
        :param id: 
        :type id: integer
        """
        raise NotImplementedError()

    # get_flowsidversions -- Synchronisation point for meld
    @staticmethod
    def get_flowsidversions(request, id, *args, **kwargs):
        """
        :param request: An HttpRequest
        :param id: 
        :type id: integer
        """
        raise NotImplementedError()

    # get_products -- Synchronisation point for meld
    @staticmethod
    def get_products(request, *args, **kwargs):
        """
        :param request: An HttpRequest
        """
        raise NotImplementedError()

    # post_products -- Synchronisation point for meld
    @staticmethod
    def post_products(request, body, *args, **kwargs):
        """
        :param request: An HttpRequest
        :param body: A dictionary containing the parsed and validated body
        :type body: dict
        """
        raise NotImplementedError()

    # get_tasks -- Synchronisation point for meld
    @staticmethod
    def get_tasks(request, domain_name=None, *args, **kwargs):
        """
        :param request: An HttpRequest
        :param domain_name: (optional) name of the domain
        :type domain_name: string
        """
        raise NotImplementedError()

    # post_tasks -- Synchronisation point for meld
    @staticmethod
    def post_tasks(request, body, *args, **kwargs):
        """
        :param request: An HttpRequest
        :param body: A dictionary containing the parsed and validated body
        :type body: dict
        """
        raise NotImplementedError()

    # get_tasksid -- Synchronisation point for meld
    @staticmethod
    def get_tasksid(request, id, *args, **kwargs):
        """
        :param request: An HttpRequest
        :param id: 
        :type id: integer
        """
        raise NotImplementedError()

    # put_tasksidpublish -- Synchronisation point for meld
    @staticmethod
    def put_tasksidpublish(request, body, id, *args, **kwargs):
        """
        :param request: An HttpRequest
        :param body: A dictionary containing the parsed and validated body
        :type body: dict
        :param id: 
        :type id: integer
        """
        raise NotImplementedError()

    # get_tasksidversion -- Synchronisation point for meld
    @staticmethod
    def get_tasksidversion(request, id, *args, **kwargs):
        """
        :param request: An HttpRequest
        :param id: 
        :type id: integer
        """
        raise NotImplementedError()


class MockedStubClass(AbstractStubClass):
    """
    Provides a mocked implementation of the AbstractStubClass.
    """
    GENERATOR = DataGenerator()

    @staticmethod
    def get_domains(request, *args, **kwargs):
        """
        :param request: An HttpRequest
        """
        response_schema = json.loads("""{
    "properties": {
        "domains": {
            "items": {
                "type": "string"
            },
            "type": "array"
        }
    },
    "type": "object"
}""")
        if "type" not in response_schema:
            response_schema["type"] = "object"

        if response_schema["type"] == "array" and "type" not in response_schema["items"]:
            response_schema["items"]["type"] = "object"

        return MockedStubClass.GENERATOR.random_value(response_schema)

    @staticmethod
    def post_domains(request, body, *args, **kwargs):
        """
        :param request: An HttpRequest
        :param body: A dictionary containing the parsed and validated body
        :type body: dict
        """
        response_schema = json.loads("""{
    "properties": {
        "id": {
            "type": "integer"
        }
    },
    "type": "object"
}""")
        if "type" not in response_schema:
            response_schema["type"] = "object"

        if response_schema["type"] == "array" and "type" not in response_schema["items"]:
            response_schema["items"]["type"] = "object"

        return MockedStubClass.GENERATOR.random_value(response_schema)

    @staticmethod
    def get_domainsiddataservice(request, id, *args, **kwargs):
        """
        :param request: An HttpRequest
        :param id: 
        :type id: integer
        """
        response_schema = json.loads("""{
    "properties": {
        "repo_name": {
            "type": "string"
        }
    },
    "type": "object"
}""")
        if "type" not in response_schema:
            response_schema["type"] = "object"

        if response_schema["type"] == "array" and "type" not in response_schema["items"]:
            response_schema["items"]["type"] = "object"

        return MockedStubClass.GENERATOR.random_value(response_schema)

    @staticmethod
    def post_domainsiddataserviceinit(request, body, id, *args, **kwargs):
        """
        :param request: An HttpRequest
        :param body: A dictionary containing the parsed and validated body
        :type body: dict
        :param id: 
        :type id: integer
        """
        response_schema = schemas.__UNSPECIFIED__
        if "type" not in response_schema:
            response_schema["type"] = "object"

        if response_schema["type"] == "array" and "type" not in response_schema["items"]:
            response_schema["items"]["type"] = "object"

        return MockedStubClass.GENERATOR.random_value(response_schema)

    @staticmethod
    def get_flows(request, product_name=None, *args, **kwargs):
        """
        :param request: An HttpRequest
        :param product_name: (optional) name of the product
        :type product_name: string
        """
        response_schema = json.loads("""{
    "properties": {
        "flows": {
            "items": {
                "properties": {
                    "name": {
                        "type": "string"
                    }
                },
                "type": "object"
            },
            "type": "array"
        }
    },
    "type": "object"
}""")
        if "type" not in response_schema:
            response_schema["type"] = "object"

        if response_schema["type"] == "array" and "type" not in response_schema["items"]:
            response_schema["items"]["type"] = "object"

        return MockedStubClass.GENERATOR.random_value(response_schema)

    @staticmethod
    def post_flows(request, body, *args, **kwargs):
        """
        :param request: An HttpRequest
        :param body: A dictionary containing the parsed and validated body
        :type body: dict
        """
        response_schema = json.loads("""{
    "properties": {
        "id": {
            "type": "integer"
        }
    },
    "type": "object"
}""")
        if "type" not in response_schema:
            response_schema["type"] = "object"

        if response_schema["type"] == "array" and "type" not in response_schema["items"]:
            response_schema["items"]["type"] = "object"

        return MockedStubClass.GENERATOR.random_value(response_schema)

    @staticmethod
    def get_flowsid(request, id, *args, **kwargs):
        """
        :param request: An HttpRequest
        :param id: 
        :type id: integer
        """
        response_schema = json.loads("""{
    "properties": {
        "flow_json": {
            "type": "object"
        },
        "id": {
            "type": "integer"
        },
        "name": {
            "type": "string"
        },
        "prod_version": {
            "type": "string"
        },
        "product": {
            "type": "string"
        },
        "staging_version": {
            "type": "string"
        }
    },
    "type": "object"
}""")
        if "type" not in response_schema:
            response_schema["type"] = "object"

        if response_schema["type"] == "array" and "type" not in response_schema["items"]:
            response_schema["items"]["type"] = "object"

        return MockedStubClass.GENERATOR.random_value(response_schema)

    @staticmethod
    def put_flowsid(request, body, id, *args, **kwargs):
        """
        :param request: An HttpRequest
        :param body: A dictionary containing the parsed and validated body
        :type body: dict
        :param id: 
        :type id: integer
        """
        response_schema = schemas.__UNSPECIFIED__
        if "type" not in response_schema:
            response_schema["type"] = "object"

        if response_schema["type"] == "array" and "type" not in response_schema["items"]:
            response_schema["items"]["type"] = "object"

        return MockedStubClass.GENERATOR.random_value(response_schema)

    @staticmethod
    def put_flowsiddeployenv(request, body, id, env, *args, **kwargs):
        """
        :param request: An HttpRequest
        :param body: A dictionary containing the parsed and validated body
        :type body: dict
        :param id: 
        :type id: integer
        :param env: 
        :type env: string
        """
        response_schema = schemas.__UNSPECIFIED__
        if "type" not in response_schema:
            response_schema["type"] = "object"

        if response_schema["type"] == "array" and "type" not in response_schema["items"]:
            response_schema["items"]["type"] = "object"

        return MockedStubClass.GENERATOR.random_value(response_schema)

    @staticmethod
    def get_flowsidloadversion(request, id, version, *args, **kwargs):
        """
        :param request: An HttpRequest
        :param id: 
        :type id: integer
        :param version: 
        :type version: string
        """
        response_schema = json.loads("""{
    "properties": {
        "flow_json": {
            "type": "object"
        },
        "name": {
            "type": "string"
        },
        "product": {
            "type": "string"
        }
    },
    "type": "object"
}""")
        if "type" not in response_schema:
            response_schema["type"] = "object"

        if response_schema["type"] == "array" and "type" not in response_schema["items"]:
            response_schema["items"]["type"] = "object"

        return MockedStubClass.GENERATOR.random_value(response_schema)

    @staticmethod
    def get_flowsidstatus(request, id, *args, **kwargs):
        """
        :param request: An HttpRequest
        :param id: 
        :type id: integer
        """
        response_schema = json.loads("""{
    "properties": {
        "status": {
            "type": "boolean"
        }
    },
    "type": "object"
}""")
        if "type" not in response_schema:
            response_schema["type"] = "object"

        if response_schema["type"] == "array" and "type" not in response_schema["items"]:
            response_schema["items"]["type"] = "object"

        return MockedStubClass.GENERATOR.random_value(response_schema)

    @staticmethod
    def get_flowsidversions(request, id, *args, **kwargs):
        """
        :param request: An HttpRequest
        :param id: 
        :type id: integer
        """
        response_schema = json.loads("""{
    "properties": {
        "versions": {
            "items": {
                "type": "string"
            },
            "type": "array"
        }
    },
    "type": "object"
}""")
        if "type" not in response_schema:
            response_schema["type"] = "object"

        if response_schema["type"] == "array" and "type" not in response_schema["items"]:
            response_schema["items"]["type"] = "object"

        return MockedStubClass.GENERATOR.random_value(response_schema)

    @staticmethod
    def get_products(request, *args, **kwargs):
        """
        :param request: An HttpRequest
        """
        response_schema = json.loads("""{
    "properties": {
        "products": {
            "items": {
                "properties": {
                    "id": {
                        "type": "integer"
                    },
                    "name": {
                        "type": "string"
                    }
                },
                "type": "object"
            },
            "type": "array"
        }
    },
    "type": "object"
}""")
        if "type" not in response_schema:
            response_schema["type"] = "object"

        if response_schema["type"] == "array" and "type" not in response_schema["items"]:
            response_schema["items"]["type"] = "object"

        return MockedStubClass.GENERATOR.random_value(response_schema)

    @staticmethod
    def post_products(request, body, *args, **kwargs):
        """
        :param request: An HttpRequest
        :param body: A dictionary containing the parsed and validated body
        :type body: dict
        """
        response_schema = schemas.__UNSPECIFIED__
        if "type" not in response_schema:
            response_schema["type"] = "object"

        if response_schema["type"] == "array" and "type" not in response_schema["items"]:
            response_schema["items"]["type"] = "object"

        return MockedStubClass.GENERATOR.random_value(response_schema)

    @staticmethod
    def get_tasks(request, domain_name=None, *args, **kwargs):
        """
        :param request: An HttpRequest
        :param domain_name: (optional) name of the domain
        :type domain_name: string
        """
        response_schema = json.loads("""{
    "properties": {
        "tasks": {
            "items": {
                "properties": {
                    "framework": {
                        "type": "string"
                    },
                    "id": {
                        "type": "integer"
                    },
                    "name": {
                        "type": "string"
                    },
                    "path": {
                        "type": "string"
                    },
                    "repo_name": {
                        "type": "string"
                    },
                    "type": {
                        "type": "string"
                    }
                },
                "type": "object"
            },
            "type": "array"
        }
    },
    "type": "object"
}""")
        if "type" not in response_schema:
            response_schema["type"] = "object"

        if response_schema["type"] == "array" and "type" not in response_schema["items"]:
            response_schema["items"]["type"] = "object"

        return MockedStubClass.GENERATOR.random_value(response_schema)

    @staticmethod
    def post_tasks(request, body, *args, **kwargs):
        """
        :param request: An HttpRequest
        :param body: A dictionary containing the parsed and validated body
        :type body: dict
        """
        response_schema = json.loads("""{
    "properties": {
        "id": {
            "type": "integer"
        }
    },
    "type": "object"
}""")
        if "type" not in response_schema:
            response_schema["type"] = "object"

        if response_schema["type"] == "array" and "type" not in response_schema["items"]:
            response_schema["items"]["type"] = "object"

        return MockedStubClass.GENERATOR.random_value(response_schema)

    @staticmethod
    def get_tasksid(request, id, *args, **kwargs):
        """
        :param request: An HttpRequest
        :param id: 
        :type id: integer
        """
        response_schema = json.loads("""{
    "properties": {
        "domain_name": {
            "type": "string"
        },
        "framework": {
            "type": "string"
        },
        "id": {
            "type": "integer"
        },
        "input_schema": {
            "properties": {
                "args": {
                    "items": {
                        "properties": {
                            "variable_name": {
                                "type": "string"
                            },
                            "variable_type": {
                                "type": "string"
                            }
                        },
                        "type": "object"
                    },
                    "type": "array"
                },
                "num_args": {
                    "type": "integer"
                }
            },
            "type": "object"
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
            "properties": {
                "args": {
                    "items": {
                        "properties": {
                            "variable_name": {
                                "type": "string"
                            },
                            "variable_type": {
                                "type": "string"
                            }
                        },
                        "type": "object"
                    },
                    "type": "array"
                },
                "num_args": {
                    "type": "integer"
                }
            },
            "type": "object"
        },
        "path": {
            "type": "string"
        },
        "repo_name": {
            "type": "string"
        },
        "type": {
            "type": "string"
        },
        "version": {
            "type": "number"
        }
    },
    "type": "object"
}""")
        if "type" not in response_schema:
            response_schema["type"] = "object"

        if response_schema["type"] == "array" and "type" not in response_schema["items"]:
            response_schema["items"]["type"] = "object"

        return MockedStubClass.GENERATOR.random_value(response_schema)

    @staticmethod
    def put_tasksidpublish(request, body, id, *args, **kwargs):
        """
        :param request: An HttpRequest
        :param body: A dictionary containing the parsed and validated body
        :type body: dict
        :param id: 
        :type id: integer
        """
        response_schema = schemas.__UNSPECIFIED__
        if "type" not in response_schema:
            response_schema["type"] = "object"

        if response_schema["type"] == "array" and "type" not in response_schema["items"]:
            response_schema["items"]["type"] = "object"

        return MockedStubClass.GENERATOR.random_value(response_schema)

    @staticmethod
    def get_tasksidversion(request, id, *args, **kwargs):
        """
        :param request: An HttpRequest
        :param id: 
        :type id: integer
        """
        response_schema = json.loads("""{
    "properties": {
        "versions": {
            "items": {
                "type": "number"
            },
            "type": "array"
        }
    },
    "type": "object"
}""")
        if "type" not in response_schema:
            response_schema["type"] = "object"

        if response_schema["type"] == "array" and "type" not in response_schema["items"]:
            response_schema["items"]["type"] = "object"

        return MockedStubClass.GENERATOR.random_value(response_schema)
