# -*- coding: utf-8 -*-

"""
    flowroutenumbersandmessaging.controllers.cnams_controller

    This file was automatically generated by APIMATIC v2.0 (https://apimatic.io).
"""

from .base_controller import BaseController
from ..api_helper import APIHelper
from ..configuration import Configuration
from .numbers_controller import NumbersController


class CNAMsController(BaseController):

    """A Controller to access Endpoints in the
        flowroutenumbersandmessaging API."""

    def list_cnams(self,
                   limit=None,
                   offset=None,
                   is_approved=None):
        """Does a GET request to /v2/cnams.

        Returns a list of all cnams owned by the user.

        Args:
            limit (int, optional): Limits the number of items to retrieve. A
                maximum of 200 items can be retrieved.
            offset (int, optional): Offsets the list of phone numbers by your
                specified value. For example, if you have 4 phone numbers and
                you entered 1 as your offset value, then only 3 of your phone
                numbers will be displayed in the response.
            is_approved if set to true or false, will only show matching records

        Returns:
            mixed: Response from the API. A JSON object of E911 Records
             that satisfy your search criteria.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _query_builder = Configuration.base_uri
        _query_builder += '/v2/cnams'
        _query_parameters = {
            'limit': limit,
            'offset': offset
        }
        if is_approved is not None:
            _query_parameters['is_approved'] = is_approved

        _query_builder = APIHelper.append_url_with_query_parameters(
            _query_builder,
            _query_parameters,
            Configuration.array_serialization)
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare and execute request
        _request = self.http_client.get(_query_url)

        return self.handle_request_and_response(_request)

    def get_cnam(self, cnam_id):
        """Does a GET request to /v2/cnams/<cnam_id>.

        Returns a record detail for the CNAM Record Id specified

        Args:

        Returns:
            mixed: Response from the API. A JSON object of of an E911 record
             that satisfy your search criteria.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _query_builder = Configuration.base_uri
        _query_builder += '/v2/cnams/{}'.format(cnam_id)
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare and execute request
        _request = self.http_client.get(_query_url)

        return self.handle_request_and_response(_request)

    def create_cnam_record(self, value):
        """Does a POST request to /v2/cnams.

        Searches for CNAM Records that match the criteria

        Args:
            value (string, required): The text string for the new CNAM record

        Returns:
            mixed: Response from the API. A JSON object of of a CNAM record
                with the new data

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        body = {
            "value": value
        }

        # Prepare query URL
        _query_builder = Configuration.base_uri
        _query_builder += '/v2/cnams'
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json'
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, headers=_headers,
                                         parameters=body)

        return self.handle_request_and_response(_request)

    def associate_cnam(self, cnam_id, phone_number):
        # first, verify the number belongs to the user
        did = NumbersController().list_account_phone_numbers(
            contains=phone_number)

        if did is None:
            error_string = "Error, this phone number does not belong to you."
            return error_string

        did = did['data'][0]['id']

        # Prepare query URL
        _query_builder = Configuration.base_uri
        _query_builder += '/v2/numbers/{}/relationships/cnam/{}'.format(did,
                                                                        cnam_id)
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json'
        }

        # Prepare and execute request
        _request = self.http_client.patch(_query_url, headers=_headers)

        return self.handle_request_and_response(_request)

    def unassociate_cnam(self, phone_number):
        # first, verify the number belongs to the user
        did = NumbersController().list_account_phone_numbers(
            contains=phone_number)

        if did is None:
            error_string = "Error, this phone number does not belong to you."
            return error_string

        did = did['data'][0]['id']

        # Prepare query URL
        _query_builder = Configuration.base_uri
        _query_builder += '/v2/numbers/{}/relationships/cnam'.format(did)
        _query_url = APIHelper.clean_url(_query_builder)
        # Prepare headers
        _headers = {
            'accept': 'application/json'
        }

        # Prepare and execute request
        _request = self.http_client.delete(_query_url, headers=_headers)

        return self.handle_request_and_response(_request)

    def remove_cnam(self, cnam_id):
        # Prepare query URL
        _query_builder = Configuration.base_uri
        _query_builder += '/v2/cnams/{}'.format(cnam_id)
        _query_url = APIHelper.clean_url(_query_builder)
        # Prepare headers
        _headers = {
            'accept': 'application/json'
        }

        # Prepare and execute request
        _request = self.http_client.delete(_query_url, headers=_headers)

        return self.handle_request_and_response(_request)
