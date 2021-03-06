# -*- coding: utf-8 -*-

"""
    flowroutenumbersandmessagingcontrollers.base_controller

    This file was automatically generated by APIMATIC v2.0
    ( https://apimatic.io ).
"""

from ..api_helper import APIHelper
from ..http.http_context import HttpContext
from ..http.requests_client import RequestsClient
from ..exceptions.error_exception import ErrorException
from ..exceptions.api_exception import APIException
from ..http.auth.basic_auth import BasicAuth


class BaseController(object):

    """All controllers inherit from this base class.

    Attributes:
        http_client (HttpClient): The HttpClient which a specific controller
            instance will use. By default all the controller objects share
            the same HttpClient. A user can use his own custom HttpClient
            as well.
        http_call_back (HttpCallBack): An object which holds call back
            methods to be called before and after the execution of an
            HttpRequest.
    """

    http_client = RequestsClient()

    http_call_back = None

    global_headers = {
        'user-agent': 'Flowroute SDK v3.0'
    }

    def __init__(self, client=None, call_back=None):
        if client is not None:
            self.http_client = client
        if call_back is not None:
            self.http_call_back = call_back

    @staticmethod
    def validate_parameters(**kwargs):
        """Validates required parameters of an endpoint.

        Args:
            kwargs (dict): A dictionary of the required parameters.

        """
        for name, value in kwargs.items():
            if value is None:
                raise ValueError("Required parameter {} cannot be None.".
                                 format(name))

    def execute_request(self, request, binary=False):
        """Executes an HttpRequest.

        Args:
            request (HttpRequest): The HttpRequest to execute.
            binary (bool): A flag which should be set to True if
                a binary response is expected.

        Returns:
            HttpContext: The HttpContext of the request. It contains,
                both, the request itself and the HttpResponse object.

        """
        # Invoke the on before request HttpCallBack if specified
        if self.http_call_back is not None:
            self.http_call_back.on_before_request(request)

        # Add global headers to request
        request.headers = APIHelper.merge_dicts(self.global_headers,
                                                request.headers)

        # Invoke the API call to fetch the response.
        func = self.http_client.execute_as_binary if binary else \
            self.http_client.execute_as_string
        response = func(request)
        context = HttpContext(request, response)

        # Invoke the on after response HttpCallBack if specified
        if self.http_call_back is not None:
            self.http_call_back.on_after_response(context)

        return context

    @staticmethod
    def validate_response(context):
        """Validates an HTTP response by checking for global errors.

        Args:
            context (HttpContext): The HttpContext of the API call.

        """
        if (context.response.status_code < 200) or \
                (context.response.status_code > 208):
            raise APIException('HTTP response not OK.', context)

    # Process request and status code and response text
    def handle_request_and_response(self, request):
        BasicAuth.apply(request)
        context = self.execute_request(request)

        # Endpoint and global error handling using HTTP status codes.
        if context.response.status_code == 401:
            raise ErrorException('Unauthorized – There was an issue with your '
                                 'API credentials.', context)
        elif context.response.status_code == 403:
            raise ErrorException('Forbidden – You don\'t have permission to '
                                 'access this resource.', context)
        elif context.response.status_code == 404:
            raise ErrorException('The specified resource was not found',
                                 context)
        elif context.response.status_code == 422:
            raise ErrorException('Unprocessable Entity - You tried to enter an'
                                 ' incorrect value.', context)
        self.validate_response(context)

        return APIHelper.json_deserialize(context.response.raw_body)
