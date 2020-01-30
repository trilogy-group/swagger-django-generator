"""
Do not modify this file. It is generated from the Swagger specification.

"""
import importlib
import logging
import json
from jsonschema import ValidationError

from django.conf import settings
from django.http import JsonResponse, HttpResponseBadRequest
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views import View

import new_app.schemas as schemas
import new_app.utils as utils

# Set up logging
logging.basicConfig(level=logging.DEBUG)
LOGGER = logging.getLogger(__name__)

try:
    VALIDATE_RESPONSES = settings.SWAGGER_API_VALIDATE_RESPONSES
except AttributeError:
    VALIDATE_RESPONSES = False
LOGGER.info("Swagger API response validation is {}".format(
    "on" if VALIDATE_RESPONSES else "off"
))

# Set up the stub class. If it is not explicitly configured in the settings.py
# file of the project, we default to a mocked class.
try:
    stub_class_path = settings.STUBS_CLASS
except AttributeError:
    stub_class_path = "new_app.stubs.MockedStubClass"

module_name, class_name = stub_class_path.rsplit(".", 1)
Module = importlib.import_module(module_name)
Stubs = getattr(Module, class_name)


def maybe_validate_result(result_string, schema):
    if VALIDATE_RESPONSES:
        try:
            utils.validate(json.loads(result_string, encoding="utf8"), schema)
        except ValidationError as e:
            LOGGER.error(e.message)


@method_decorator(csrf_exempt, name="dispatch")
class Domains(View):

    GET_RESPONSE_SCHEMA = json.loads("""{
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
    POST_RESPONSE_SCHEMA = json.loads("""{
    "properties": {
        "id": {
            "type": "integer"
        }
    },
    "type": "object"
}""")
    POST_BODY_SCHEMA = json.loads("""{
    "properties": {
        "name": {
            "description": "Domain name",
            "type": "string"
        }
    },
    "type": "object"
}""")

    def get(self, request, *args, **kwargs):
        """
        :param self: A Domains instance
        :param request: An HttpRequest
        """
        try:

            result = Stubs.get_domains(request, )

            if type(result) is tuple:
                result, headers = result
            else:
                headers = {}

            # The result may contain fields with date or datetime values that will not
            # pass JSON validation. We first create the response, and then maybe validate
            # the response content against the schema.
            response = JsonResponse(result, safe=False)

            maybe_validate_result(response.content, self.GET_RESPONSE_SCHEMA)

            for key, val in headers.items():
                response[key] = val

            return response
        except ValidationError as ve:
            return HttpResponseBadRequest("Parameter validation failed: {}".format(ve.message))
        except ValueError as ve:
            return HttpResponseBadRequest("Parameter validation failed: {}".format(ve))

    def post(self, request, *args, **kwargs):
        """
        :param self: A Domains instance
        :param request: An HttpRequest
        """
        body = utils.body_to_dict(request.body, self.POST_BODY_SCHEMA)
        if not body:
            return HttpResponseBadRequest("Body required")

        try:

            result = Stubs.post_domains(request, body, )

            if type(result) is tuple:
                result, headers = result
            else:
                headers = {}

            # The result may contain fields with date or datetime values that will not
            # pass JSON validation. We first create the response, and then maybe validate
            # the response content against the schema.
            response = JsonResponse(result, safe=False)

            maybe_validate_result(response.content, self.POST_RESPONSE_SCHEMA)

            for key, val in headers.items():
                response[key] = val

            return response
        except ValidationError as ve:
            return HttpResponseBadRequest("Parameter validation failed: {}".format(ve.message))
        except ValueError as ve:
            return HttpResponseBadRequest("Parameter validation failed: {}".format(ve))


@method_decorator(csrf_exempt, name="dispatch")
class DomainsIdDataService(View):

    GET_RESPONSE_SCHEMA = json.loads("""{
    "properties": {
        "repo_name": {
            "type": "string"
        }
    },
    "type": "object"
}""")

    def get(self, request, id, *args, **kwargs):
        """
        :param self: A DomainsIdDataService instance
        :param request: An HttpRequest
        :param id: integer 
        """
        try:

            result = Stubs.get_domainsiddataservice(request, id, )

            if type(result) is tuple:
                result, headers = result
            else:
                headers = {}

            # The result may contain fields with date or datetime values that will not
            # pass JSON validation. We first create the response, and then maybe validate
            # the response content against the schema.
            response = JsonResponse(result, safe=False)

            maybe_validate_result(response.content, self.GET_RESPONSE_SCHEMA)

            for key, val in headers.items():
                response[key] = val

            return response
        except ValidationError as ve:
            return HttpResponseBadRequest("Parameter validation failed: {}".format(ve.message))
        except ValueError as ve:
            return HttpResponseBadRequest("Parameter validation failed: {}".format(ve))


@method_decorator(csrf_exempt, name="dispatch")
class DomainsIdDataServiceInit(View):

    POST_RESPONSE_SCHEMA = schemas.__UNSPECIFIED__
    POST_BODY_SCHEMA = json.loads("""{
    "properties": {
        "model_config": {
            "type": "string"
        }
    },
    "type": "object"
}""")

    def post(self, request, id, *args, **kwargs):
        """
        :param self: A DomainsIdDataServiceInit instance
        :param request: An HttpRequest
        :param id: integer 
        """
        body = utils.body_to_dict(request.body, self.POST_BODY_SCHEMA)
        if not body:
            return HttpResponseBadRequest("Body required")

        try:

            result = Stubs.post_domainsiddataserviceinit(request, body, id, )

            if type(result) is tuple:
                result, headers = result
            else:
                headers = {}

            # The result may contain fields with date or datetime values that will not
            # pass JSON validation. We first create the response, and then maybe validate
            # the response content against the schema.
            response = JsonResponse(result, safe=False)

            maybe_validate_result(response.content, self.POST_RESPONSE_SCHEMA)

            for key, val in headers.items():
                response[key] = val

            return response
        except ValidationError as ve:
            return HttpResponseBadRequest("Parameter validation failed: {}".format(ve.message))
        except ValueError as ve:
            return HttpResponseBadRequest("Parameter validation failed: {}".format(ve))


@method_decorator(csrf_exempt, name="dispatch")
class Flows(View):

    GET_RESPONSE_SCHEMA = json.loads("""{
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
    POST_RESPONSE_SCHEMA = json.loads("""{
    "properties": {
        "id": {
            "type": "integer"
        }
    },
    "type": "object"
}""")
    POST_BODY_SCHEMA = json.loads("""{
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

    def get(self, request, *args, **kwargs):
        """
        :param self: A Flows instance
        :param request: An HttpRequest
        """
        try:

            # product_name (optional): string name of the product
            product_name = request.GET.get("product_name", None)
            if product_name is not None:
                schema = {'type': 'string'}
                utils.validate(product_name, schema)
            result = Stubs.get_flows(request, product_name, )

            if type(result) is tuple:
                result, headers = result
            else:
                headers = {}

            # The result may contain fields with date or datetime values that will not
            # pass JSON validation. We first create the response, and then maybe validate
            # the response content against the schema.
            response = JsonResponse(result, safe=False)

            maybe_validate_result(response.content, self.GET_RESPONSE_SCHEMA)

            for key, val in headers.items():
                response[key] = val

            return response
        except ValidationError as ve:
            return HttpResponseBadRequest("Parameter validation failed: {}".format(ve.message))
        except ValueError as ve:
            return HttpResponseBadRequest("Parameter validation failed: {}".format(ve))

    def post(self, request, *args, **kwargs):
        """
        :param self: A Flows instance
        :param request: An HttpRequest
        """
        body = utils.body_to_dict(request.body, self.POST_BODY_SCHEMA)
        if not body:
            return HttpResponseBadRequest("Body required")

        try:

            result = Stubs.post_flows(request, body, )

            if type(result) is tuple:
                result, headers = result
            else:
                headers = {}

            # The result may contain fields with date or datetime values that will not
            # pass JSON validation. We first create the response, and then maybe validate
            # the response content against the schema.
            response = JsonResponse(result, safe=False)

            maybe_validate_result(response.content, self.POST_RESPONSE_SCHEMA)

            for key, val in headers.items():
                response[key] = val

            return response
        except ValidationError as ve:
            return HttpResponseBadRequest("Parameter validation failed: {}".format(ve.message))
        except ValueError as ve:
            return HttpResponseBadRequest("Parameter validation failed: {}".format(ve))


@method_decorator(csrf_exempt, name="dispatch")
class FlowsId(View):

    GET_RESPONSE_SCHEMA = json.loads("""{
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
    PUT_RESPONSE_SCHEMA = schemas.__UNSPECIFIED__
    PUT_BODY_SCHEMA = json.loads("""{
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

    def get(self, request, id, *args, **kwargs):
        """
        :param self: A FlowsId instance
        :param request: An HttpRequest
        :param id: integer 
        """
        try:

            result = Stubs.get_flowsid(request, id, )

            if type(result) is tuple:
                result, headers = result
            else:
                headers = {}

            # The result may contain fields with date or datetime values that will not
            # pass JSON validation. We first create the response, and then maybe validate
            # the response content against the schema.
            response = JsonResponse(result, safe=False)

            maybe_validate_result(response.content, self.GET_RESPONSE_SCHEMA)

            for key, val in headers.items():
                response[key] = val

            return response
        except ValidationError as ve:
            return HttpResponseBadRequest("Parameter validation failed: {}".format(ve.message))
        except ValueError as ve:
            return HttpResponseBadRequest("Parameter validation failed: {}".format(ve))

    def put(self, request, id, *args, **kwargs):
        """
        :param self: A FlowsId instance
        :param request: An HttpRequest
        :param id: integer 
        """
        body = utils.body_to_dict(request.body, self.PUT_BODY_SCHEMA)
        if not body:
            return HttpResponseBadRequest("Body required")

        try:

            result = Stubs.put_flowsid(request, body, id, )

            if type(result) is tuple:
                result, headers = result
            else:
                headers = {}

            # The result may contain fields with date or datetime values that will not
            # pass JSON validation. We first create the response, and then maybe validate
            # the response content against the schema.
            response = JsonResponse(result, safe=False)

            maybe_validate_result(response.content, self.PUT_RESPONSE_SCHEMA)

            for key, val in headers.items():
                response[key] = val

            return response
        except ValidationError as ve:
            return HttpResponseBadRequest("Parameter validation failed: {}".format(ve.message))
        except ValueError as ve:
            return HttpResponseBadRequest("Parameter validation failed: {}".format(ve))


@method_decorator(csrf_exempt, name="dispatch")
class FlowsIdDeployEnv(View):

    PUT_RESPONSE_SCHEMA = schemas.__UNSPECIFIED__
    PUT_BODY_SCHEMA = json.loads("""{
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

    def put(self, request, id, env, *args, **kwargs):
        """
        :param self: A FlowsIdDeployEnv instance
        :param request: An HttpRequest
        :param id: integer 
        :param env: string 
        """
        body = utils.body_to_dict(request.body, self.PUT_BODY_SCHEMA)
        if not body:
            return HttpResponseBadRequest("Body required")

        try:

            result = Stubs.put_flowsiddeployenv(request, body, id, env, )

            if type(result) is tuple:
                result, headers = result
            else:
                headers = {}

            # The result may contain fields with date or datetime values that will not
            # pass JSON validation. We first create the response, and then maybe validate
            # the response content against the schema.
            response = JsonResponse(result, safe=False)

            maybe_validate_result(response.content, self.PUT_RESPONSE_SCHEMA)

            for key, val in headers.items():
                response[key] = val

            return response
        except ValidationError as ve:
            return HttpResponseBadRequest("Parameter validation failed: {}".format(ve.message))
        except ValueError as ve:
            return HttpResponseBadRequest("Parameter validation failed: {}".format(ve))


@method_decorator(csrf_exempt, name="dispatch")
class FlowsIdLoadVersion(View):

    GET_RESPONSE_SCHEMA = json.loads("""{
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

    def get(self, request, id, version, *args, **kwargs):
        """
        :param self: A FlowsIdLoadVersion instance
        :param request: An HttpRequest
        :param id: integer 
        :param version: string 
        """
        try:

            result = Stubs.get_flowsidloadversion(request, id, version, )

            if type(result) is tuple:
                result, headers = result
            else:
                headers = {}

            # The result may contain fields with date or datetime values that will not
            # pass JSON validation. We first create the response, and then maybe validate
            # the response content against the schema.
            response = JsonResponse(result, safe=False)

            maybe_validate_result(response.content, self.GET_RESPONSE_SCHEMA)

            for key, val in headers.items():
                response[key] = val

            return response
        except ValidationError as ve:
            return HttpResponseBadRequest("Parameter validation failed: {}".format(ve.message))
        except ValueError as ve:
            return HttpResponseBadRequest("Parameter validation failed: {}".format(ve))


@method_decorator(csrf_exempt, name="dispatch")
class FlowsIdStatus(View):

    GET_RESPONSE_SCHEMA = json.loads("""{
    "properties": {
        "status": {
            "type": "boolean"
        }
    },
    "type": "object"
}""")

    def get(self, request, id, *args, **kwargs):
        """
        :param self: A FlowsIdStatus instance
        :param request: An HttpRequest
        :param id: integer 
        """
        try:

            result = Stubs.get_flowsidstatus(request, id, )

            if type(result) is tuple:
                result, headers = result
            else:
                headers = {}

            # The result may contain fields with date or datetime values that will not
            # pass JSON validation. We first create the response, and then maybe validate
            # the response content against the schema.
            response = JsonResponse(result, safe=False)

            maybe_validate_result(response.content, self.GET_RESPONSE_SCHEMA)

            for key, val in headers.items():
                response[key] = val

            return response
        except ValidationError as ve:
            return HttpResponseBadRequest("Parameter validation failed: {}".format(ve.message))
        except ValueError as ve:
            return HttpResponseBadRequest("Parameter validation failed: {}".format(ve))


@method_decorator(csrf_exempt, name="dispatch")
class FlowsIdVersions(View):

    GET_RESPONSE_SCHEMA = json.loads("""{
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

    def get(self, request, id, *args, **kwargs):
        """
        :param self: A FlowsIdVersions instance
        :param request: An HttpRequest
        :param id: integer 
        """
        try:

            result = Stubs.get_flowsidversions(request, id, )

            if type(result) is tuple:
                result, headers = result
            else:
                headers = {}

            # The result may contain fields with date or datetime values that will not
            # pass JSON validation. We first create the response, and then maybe validate
            # the response content against the schema.
            response = JsonResponse(result, safe=False)

            maybe_validate_result(response.content, self.GET_RESPONSE_SCHEMA)

            for key, val in headers.items():
                response[key] = val

            return response
        except ValidationError as ve:
            return HttpResponseBadRequest("Parameter validation failed: {}".format(ve.message))
        except ValueError as ve:
            return HttpResponseBadRequest("Parameter validation failed: {}".format(ve))


@method_decorator(csrf_exempt, name="dispatch")
class Products(View):

    GET_RESPONSE_SCHEMA = json.loads("""{
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
    POST_RESPONSE_SCHEMA = schemas.__UNSPECIFIED__
    POST_BODY_SCHEMA = json.loads("""{
    "properties": {
        "name": {
            "type": "string"
        }
    },
    "type": "object"
}""")

    def get(self, request, *args, **kwargs):
        """
        :param self: A Products instance
        :param request: An HttpRequest
        """
        try:

            result = Stubs.get_products(request, )

            if type(result) is tuple:
                result, headers = result
            else:
                headers = {}

            # The result may contain fields with date or datetime values that will not
            # pass JSON validation. We first create the response, and then maybe validate
            # the response content against the schema.
            response = JsonResponse(result, safe=False)

            maybe_validate_result(response.content, self.GET_RESPONSE_SCHEMA)

            for key, val in headers.items():
                response[key] = val

            return response
        except ValidationError as ve:
            return HttpResponseBadRequest("Parameter validation failed: {}".format(ve.message))
        except ValueError as ve:
            return HttpResponseBadRequest("Parameter validation failed: {}".format(ve))

    def post(self, request, *args, **kwargs):
        """
        :param self: A Products instance
        :param request: An HttpRequest
        """
        body = utils.body_to_dict(request.body, self.POST_BODY_SCHEMA)
        if not body:
            return HttpResponseBadRequest("Body required")

        try:

            result = Stubs.post_products(request, body, )

            if type(result) is tuple:
                result, headers = result
            else:
                headers = {}

            # The result may contain fields with date or datetime values that will not
            # pass JSON validation. We first create the response, and then maybe validate
            # the response content against the schema.
            response = JsonResponse(result, safe=False)

            maybe_validate_result(response.content, self.POST_RESPONSE_SCHEMA)

            for key, val in headers.items():
                response[key] = val

            return response
        except ValidationError as ve:
            return HttpResponseBadRequest("Parameter validation failed: {}".format(ve.message))
        except ValueError as ve:
            return HttpResponseBadRequest("Parameter validation failed: {}".format(ve))


@method_decorator(csrf_exempt, name="dispatch")
class Tasks(View):

    GET_RESPONSE_SCHEMA = json.loads("""{
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
    POST_RESPONSE_SCHEMA = json.loads("""{
    "properties": {
        "id": {
            "type": "integer"
        }
    },
    "type": "object"
}""")
    POST_BODY_SCHEMA = json.loads("""{
    "properties": {
        "domain_name": {
            "type": "string"
        },
        "framework": {
            "type": "string"
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
        }
    },
    "type": "object"
}""")

    def get(self, request, *args, **kwargs):
        """
        :param self: A Tasks instance
        :param request: An HttpRequest
        """
        try:

            # domain_name (optional): string name of the domain
            domain_name = request.GET.get("domain_name", None)
            if domain_name is not None:
                schema = {'type': 'string'}
                utils.validate(domain_name, schema)
            result = Stubs.get_tasks(request, domain_name, )

            if type(result) is tuple:
                result, headers = result
            else:
                headers = {}

            # The result may contain fields with date or datetime values that will not
            # pass JSON validation. We first create the response, and then maybe validate
            # the response content against the schema.
            response = JsonResponse(result, safe=False)

            maybe_validate_result(response.content, self.GET_RESPONSE_SCHEMA)

            for key, val in headers.items():
                response[key] = val

            return response
        except ValidationError as ve:
            return HttpResponseBadRequest("Parameter validation failed: {}".format(ve.message))
        except ValueError as ve:
            return HttpResponseBadRequest("Parameter validation failed: {}".format(ve))

    def post(self, request, *args, **kwargs):
        """
        :param self: A Tasks instance
        :param request: An HttpRequest
        """
        body = utils.body_to_dict(request.body, self.POST_BODY_SCHEMA)
        if not body:
            return HttpResponseBadRequest("Body required")

        try:

            result = Stubs.post_tasks(request, body, )

            if type(result) is tuple:
                result, headers = result
            else:
                headers = {}

            # The result may contain fields with date or datetime values that will not
            # pass JSON validation. We first create the response, and then maybe validate
            # the response content against the schema.
            response = JsonResponse(result, safe=False)

            maybe_validate_result(response.content, self.POST_RESPONSE_SCHEMA)

            for key, val in headers.items():
                response[key] = val

            return response
        except ValidationError as ve:
            return HttpResponseBadRequest("Parameter validation failed: {}".format(ve.message))
        except ValueError as ve:
            return HttpResponseBadRequest("Parameter validation failed: {}".format(ve))


@method_decorator(csrf_exempt, name="dispatch")
class TasksId(View):

    GET_RESPONSE_SCHEMA = json.loads("""{
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

    def get(self, request, id, *args, **kwargs):
        """
        :param self: A TasksId instance
        :param request: An HttpRequest
        :param id: integer 
        """
        try:

            result = Stubs.get_tasksid(request, id, )

            if type(result) is tuple:
                result, headers = result
            else:
                headers = {}

            # The result may contain fields with date or datetime values that will not
            # pass JSON validation. We first create the response, and then maybe validate
            # the response content against the schema.
            response = JsonResponse(result, safe=False)

            maybe_validate_result(response.content, self.GET_RESPONSE_SCHEMA)

            for key, val in headers.items():
                response[key] = val

            return response
        except ValidationError as ve:
            return HttpResponseBadRequest("Parameter validation failed: {}".format(ve.message))
        except ValueError as ve:
            return HttpResponseBadRequest("Parameter validation failed: {}".format(ve))


@method_decorator(csrf_exempt, name="dispatch")
class TasksIdPublish(View):

    PUT_RESPONSE_SCHEMA = schemas.__UNSPECIFIED__
    PUT_BODY_SCHEMA = json.loads("""{
    "properties": {
        "is_published": {
            "type": "boolean"
        }
    },
    "type": "object"
}""")

    def put(self, request, id, *args, **kwargs):
        """
        :param self: A TasksIdPublish instance
        :param request: An HttpRequest
        :param id: integer 
        """
        body = utils.body_to_dict(request.body, self.PUT_BODY_SCHEMA)
        if not body:
            return HttpResponseBadRequest("Body required")

        try:

            result = Stubs.put_tasksidpublish(request, body, id, )

            if type(result) is tuple:
                result, headers = result
            else:
                headers = {}

            # The result may contain fields with date or datetime values that will not
            # pass JSON validation. We first create the response, and then maybe validate
            # the response content against the schema.
            response = JsonResponse(result, safe=False)

            maybe_validate_result(response.content, self.PUT_RESPONSE_SCHEMA)

            for key, val in headers.items():
                response[key] = val

            return response
        except ValidationError as ve:
            return HttpResponseBadRequest("Parameter validation failed: {}".format(ve.message))
        except ValueError as ve:
            return HttpResponseBadRequest("Parameter validation failed: {}".format(ve))


@method_decorator(csrf_exempt, name="dispatch")
class TasksIdVersion(View):

    GET_RESPONSE_SCHEMA = json.loads("""{
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

    def get(self, request, id, *args, **kwargs):
        """
        :param self: A TasksIdVersion instance
        :param request: An HttpRequest
        :param id: integer 
        """
        try:

            result = Stubs.get_tasksidversion(request, id, )

            if type(result) is tuple:
                result, headers = result
            else:
                headers = {}

            # The result may contain fields with date or datetime values that will not
            # pass JSON validation. We first create the response, and then maybe validate
            # the response content against the schema.
            response = JsonResponse(result, safe=False)

            maybe_validate_result(response.content, self.GET_RESPONSE_SCHEMA)

            for key, val in headers.items():
                response[key] = val

            return response
        except ValidationError as ve:
            return HttpResponseBadRequest("Parameter validation failed: {}".format(ve.message))
        except ValueError as ve:
            return HttpResponseBadRequest("Parameter validation failed: {}".format(ve))


class __SWAGGER_SPEC__(View):

    def get(self, request, *args, **kwargs):
        spec = json.loads("""{
    "basePath": "/abizerlokhandwala/devflows-api/1.0.0",
    "definitions": {
        "data_service": {
            "properties": {
                "domain": {
                    "$ref": "#/definitions/domain",
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
        },
        "deployment_status": {
            "properties": {
                "flow": {
                    "$ref": "#/definitions/flow",
                    "x-scope": [
                        ""
                    ]
                },
                "id": {
                    "type": "integer"
                },
                "prod_version": {
                    "$ref": "#/definitions/flow_version",
                    "x-scope": [
                        ""
                    ]
                },
                "stage_version": {
                    "$ref": "#/definitions/flow_version",
                    "x-scope": [
                        ""
                    ]
                }
            },
            "type": "object"
        },
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
            "type": "object"
        },
        "flow": {
            "properties": {
                "id": {
                    "type": "integer"
                },
                "name": {
                    "type": "string"
                },
                "product": {
                    "$ref": "#/definitions/product",
                    "x-scope": [
                        "",
                        "#/definitions/flow_version",
                        "#/definitions/flow"
                    ]
                }
            },
            "type": "object"
        },
        "flow_version": {
            "properties": {
                "flow": {
                    "$ref": "#/definitions/flow",
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
            "type": "object"
        },
        "task": {
            "properties": {
                "domain": {
                    "$ref": "#/definitions/domain",
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
    },
    "host": "virtserver.swaggerhub.com",
    "info": {
        "title": "Devflow API",
        "version": "1.0.0"
    },
    "paths": {
        "/domains": {
            "get": {
                "description": "get all domains\\n",
                "parameters": [],
                "produces": [
                    "application/json"
                ],
                "responses": {
                    "200": {
                        "description": "search results matching criteria",
                        "schema": {
                            "properties": {
                                "domains": {
                                    "items": {
                                        "type": "string"
                                    },
                                    "type": "array"
                                }
                            },
                            "type": "object"
                        }
                    },
                    "400": {
                        "description": "bad input parameter"
                    }
                },
                "summary": "get all domains",
                "tags": [
                    "domain"
                ]
            },
            "post": {
                "consumes": [
                    "application/json"
                ],
                "description": "Adds a new domain",
                "parameters": [
                    {
                        "in": "body",
                        "name": "body",
                        "required": false,
                        "schema": {
                            "properties": {
                                "name": {
                                    "description": "Domain name",
                                    "type": "string"
                                }
                            },
                            "type": "object"
                        }
                    }
                ],
                "produces": [
                    "application/json"
                ],
                "responses": {
                    "201": {
                        "description": "domain created",
                        "schema": {
                            "properties": {
                                "id": {
                                    "type": "integer"
                                }
                            },
                            "type": "object"
                        }
                    },
                    "400": {
                        "description": "invalid input, object invalid"
                    },
                    "409": {
                        "description": "an existing domain already exists"
                    }
                },
                "summary": "add domain",
                "tags": [
                    "domain"
                ]
            }
        },
        "/domains/{id}/data-service": {
            "get": {
                "description": "get data model by domain name\\n",
                "parameters": [
                    {
                        "in": "path",
                        "name": "id",
                        "required": true,
                        "type": "integer"
                    }
                ],
                "produces": [
                    "application/json"
                ],
                "responses": {
                    "200": {
                        "description": "search results matching criteria",
                        "schema": {
                            "properties": {
                                "repo_name": {
                                    "type": "string"
                                }
                            },
                            "type": "object"
                        }
                    },
                    "400": {
                        "description": "bad input parameter"
                    }
                },
                "summary": "get model of a domain",
                "tags": [
                    "data model"
                ]
            }
        },
        "/domains/{id}/data-service-init": {
            "post": {
                "consumes": [
                    "application/json"
                ],
                "description": "Adds a new data model for the given domain",
                "parameters": [
                    {
                        "in": "path",
                        "name": "id",
                        "required": true,
                        "type": "integer"
                    },
                    {
                        "in": "body",
                        "name": "body",
                        "required": false,
                        "schema": {
                            "properties": {
                                "model_config": {
                                    "type": "string"
                                }
                            },
                            "type": "object"
                        }
                    }
                ],
                "responses": {
                    "201": {
                        "description": "data model created"
                    },
                    "400": {
                        "description": "invalid input, object invalid"
                    },
                    "409": {
                        "description": "an existing data model already exists"
                    }
                },
                "summary": "add data model of a domain",
                "tags": [
                    "data model"
                ]
            }
        },
        "/flows": {
            "get": {
                "description": "get flow by product name\\n",
                "parameters": [
                    {
                        "description": "name of the product",
                        "in": "query",
                        "name": "product_name",
                        "required": false,
                        "type": "string"
                    }
                ],
                "produces": [
                    "application/json"
                ],
                "responses": {
                    "200": {
                        "description": "search results matching criteria",
                        "schema": {
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
                        }
                    },
                    "400": {
                        "description": "bad input parameter"
                    }
                },
                "summary": "get all flows part of a product",
                "tags": [
                    "flow"
                ]
            },
            "post": {
                "consumes": [
                    "application/json"
                ],
                "description": "Adds a new flow",
                "parameters": [
                    {
                        "in": "body",
                        "name": "body",
                        "required": false,
                        "schema": {
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
                        }
                    }
                ],
                "produces": [
                    "application/json"
                ],
                "responses": {
                    "201": {
                        "description": "flow created",
                        "schema": {
                            "properties": {
                                "id": {
                                    "type": "integer"
                                }
                            },
                            "type": "object"
                        }
                    },
                    "400": {
                        "description": "invalid input, object invalid"
                    },
                    "409": {
                        "description": "an existing flow already exists"
                    }
                },
                "summary": "add flow",
                "tags": [
                    "flow"
                ]
            }
        },
        "/flows/{id}": {
            "get": {
                "description": "get flow by id\\n",
                "parameters": [
                    {
                        "in": "path",
                        "name": "id",
                        "required": true,
                        "type": "integer"
                    }
                ],
                "produces": [
                    "application/json"
                ],
                "responses": {
                    "200": {
                        "description": "search results matching criteria",
                        "schema": {
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
                        }
                    },
                    "400": {
                        "description": "bad input parameter"
                    }
                },
                "summary": "get flow",
                "tags": [
                    "flow"
                ]
            },
            "put": {
                "consumes": [
                    "application/json"
                ],
                "description": "Updates a flow",
                "parameters": [
                    {
                        "in": "path",
                        "name": "id",
                        "required": true,
                        "type": "integer"
                    },
                    {
                        "in": "body",
                        "name": "body",
                        "required": false,
                        "schema": {
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
                        }
                    }
                ],
                "responses": {
                    "204": {
                        "description": "flow updated"
                    },
                    "400": {
                        "description": "invalid input, object invalid"
                    }
                },
                "summary": "update flow",
                "tags": [
                    "flow"
                ]
            }
        },
        "/flows/{id}/deploy/{env}": {
            "put": {
                "consumes": [
                    "application/json"
                ],
                "description": "env parameter can take the values \\"prod\\" and \\"dev\\"",
                "parameters": [
                    {
                        "in": "path",
                        "name": "id",
                        "required": true,
                        "type": "integer"
                    },
                    {
                        "in": "path",
                        "name": "env",
                        "required": true,
                        "type": "string"
                    },
                    {
                        "in": "body",
                        "name": "body",
                        "required": false,
                        "schema": {
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
                        }
                    }
                ],
                "responses": {
                    "201": {
                        "description": "flow deployed"
                    },
                    "400": {
                        "description": "invalid input, object invalid"
                    }
                },
                "summary": "deploy flow to environment",
                "tags": [
                    "deploy flow to environment"
                ]
            }
        },
        "/flows/{id}/load/{version}": {
            "get": {
                "description": "version is the version of the flow",
                "parameters": [
                    {
                        "in": "path",
                        "name": "id",
                        "required": true,
                        "type": "integer"
                    },
                    {
                        "in": "path",
                        "name": "version",
                        "required": true,
                        "type": "string"
                    }
                ],
                "produces": [
                    "application/json"
                ],
                "responses": {
                    "200": {
                        "description": "search results matching criteria",
                        "schema": {
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
                        }
                    },
                    "400": {
                        "description": "bad input parameter"
                    }
                },
                "summary": "load flow of given environment",
                "tags": [
                    "load flow"
                ]
            }
        },
        "/flows/{id}/status": {
            "get": {
                "description": "get deployment status of flow with given id (true/false)",
                "parameters": [
                    {
                        "in": "path",
                        "name": "id",
                        "required": true,
                        "type": "integer"
                    }
                ],
                "produces": [
                    "application/json"
                ],
                "responses": {
                    "200": {
                        "description": "true/false",
                        "schema": {
                            "properties": {
                                "status": {
                                    "type": "boolean"
                                }
                            },
                            "type": "object"
                        }
                    },
                    "400": {
                        "description": "invalid input, object invalid"
                    }
                },
                "summary": "get deployment status of flow with given id",
                "tags": [
                    "status"
                ]
            }
        },
        "/flows/{id}/versions": {
            "get": {
                "description": "get all versions of a flow",
                "parameters": [
                    {
                        "in": "path",
                        "name": "id",
                        "required": true,
                        "type": "integer"
                    }
                ],
                "produces": [
                    "application/json"
                ],
                "responses": {
                    "200": {
                        "description": "get all versions of a flow",
                        "schema": {
                            "properties": {
                                "versions": {
                                    "items": {
                                        "type": "string"
                                    },
                                    "type": "array"
                                }
                            },
                            "type": "object"
                        }
                    },
                    "400": {
                        "description": "invalid input, object invalid"
                    }
                },
                "summary": "get all versions of a flow",
                "tags": [
                    "flow"
                ]
            }
        },
        "/products": {
            "get": {
                "description": "get all products by name\\n",
                "parameters": [],
                "produces": [
                    "application/json"
                ],
                "responses": {
                    "200": {
                        "description": "search results matching criteria",
                        "schema": {
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
                        }
                    },
                    "400": {
                        "description": "bad input parameter"
                    }
                },
                "summary": "get all products",
                "tags": [
                    "product"
                ]
            },
            "post": {
                "consumes": [
                    "application/json"
                ],
                "description": "Adds a new product",
                "parameters": [
                    {
                        "in": "body",
                        "name": "body",
                        "required": false,
                        "schema": {
                            "properties": {
                                "name": {
                                    "type": "string"
                                }
                            },
                            "type": "object"
                        }
                    }
                ],
                "responses": {
                    "201": {
                        "description": "product created"
                    },
                    "400": {
                        "description": "invalid input, object invalid"
                    },
                    "409": {
                        "description": "an existing product already exists"
                    }
                },
                "summary": "add product",
                "tags": [
                    "product"
                ]
            }
        },
        "/tasks": {
            "get": {
                "description": "get all tasks part of a domain\\n",
                "parameters": [
                    {
                        "description": "name of the domain",
                        "in": "query",
                        "name": "domain_name",
                        "required": false,
                        "type": "string"
                    }
                ],
                "produces": [
                    "application/json"
                ],
                "responses": {
                    "200": {
                        "description": "search results matching criteria",
                        "schema": {
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
                        }
                    },
                    "400": {
                        "description": "bad input parameter"
                    }
                },
                "summary": "get all tasks part of a domain",
                "tags": [
                    "task"
                ]
            },
            "post": {
                "consumes": [
                    "application/json"
                ],
                "description": "Adds a new task under a particular domain",
                "parameters": [
                    {
                        "in": "body",
                        "name": "body",
                        "required": false,
                        "schema": {
                            "properties": {
                                "domain_name": {
                                    "type": "string"
                                },
                                "framework": {
                                    "type": "string"
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
                                }
                            },
                            "type": "object"
                        }
                    }
                ],
                "produces": [
                    "application/json"
                ],
                "responses": {
                    "201": {
                        "description": "task created",
                        "schema": {
                            "properties": {
                                "id": {
                                    "type": "integer"
                                }
                            },
                            "type": "object"
                        }
                    },
                    "400": {
                        "description": "invalid input, object invalid"
                    },
                    "409": {
                        "description": "an existing task already exists"
                    }
                },
                "summary": "add task",
                "tags": [
                    "task"
                ]
            }
        },
        "/tasks/{id}": {
            "get": {
                "description": "get task by id\\n",
                "parameters": [
                    {
                        "in": "path",
                        "name": "id",
                        "required": true,
                        "type": "integer"
                    }
                ],
                "produces": [
                    "application/json"
                ],
                "responses": {
                    "200": {
                        "description": "search results matching criteria",
                        "schema": {
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
                        }
                    },
                    "400": {
                        "description": "bad input parameter"
                    }
                },
                "summary": "get task",
                "tags": [
                    "task"
                ]
            }
        },
        "/tasks/{id}/publish": {
            "put": {
                "consumes": [
                    "application/json"
                ],
                "description": "Updates a task under a particular domain",
                "parameters": [
                    {
                        "in": "path",
                        "name": "id",
                        "required": true,
                        "type": "integer"
                    },
                    {
                        "in": "body",
                        "name": "body",
                        "required": false,
                        "schema": {
                            "properties": {
                                "is_published": {
                                    "type": "boolean"
                                }
                            },
                            "type": "object"
                        }
                    }
                ],
                "responses": {
                    "204": {
                        "description": "task updated"
                    },
                    "400": {
                        "description": "invalid input, object invalid"
                    }
                },
                "summary": "update task",
                "tags": [
                    "task"
                ]
            }
        },
        "/tasks/{id}/version": {
            "get": {
                "description": "get all versions of a task\\n",
                "parameters": [
                    {
                        "in": "path",
                        "name": "id",
                        "required": true,
                        "type": "integer"
                    }
                ],
                "produces": [
                    "application/json"
                ],
                "responses": {
                    "200": {
                        "description": "search results matching criteria",
                        "schema": {
                            "properties": {
                                "versions": {
                                    "items": {
                                        "type": "number"
                                    },
                                    "type": "array"
                                }
                            },
                            "type": "object"
                        }
                    },
                    "400": {
                        "description": "bad input parameter"
                    }
                },
                "summary": "get all task versions",
                "tags": [
                    "task"
                ]
            }
        }
    },
    "schemes": [
        "https"
    ],
    "swagger": "2.0",
    "x-components": {}
}""")
        # Mod spec to point to demo application
        spec["basePath"] = "/"
        spec["host"] = "localhost:8000"
        # Add basic auth as a security definition
        security_definitions = spec.get("securityDefinitions", {})
        security_definitions["basic_auth"] = {"type": "basic"}
        spec["securityDefinitions"] = security_definitions
        return JsonResponse(spec)
