# -*- coding: utf-8 -*-

"""
   FlowrouteNumbersLib.Controllers.PurchasablePhoneNumbersController

   Copyright Flowroute, Inc. 2016
"""

from FlowrouteNumbersLib.APIHelper import APIHelper
from FlowrouteNumbersLib.Configuration import Configuration
from FlowrouteNumbersLib.APIException import APIException
from FlowrouteNumbersLib.CustomAuthUtility import CustomAuthUtility


class PurchasablePhoneNumbersController(object):

    """A Controller to access Endpoints in the FlowrouteNumbersLib API."""

    @staticmethod
    def list_area_and_exchange(limit=None,
                               npa=None,
                               page=None):
        """Does a GET request to /available-tns/npanxxs/.

        Retrieves a list of the NPA-NXXs (area codes and exchanges) that
        contain purchasable telephone numbers.

        Args:
            limit (int, optional): Number of items to display (Max 200)
            npa (int, optional): Restricts the results to this NPA.
            page (int, optional): Page to display

        Returns:
            mixed: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        # The base uri for api requests
        query_builder = Configuration.BASE_URI
 
        # Prepare query string for API call
        query_builder += "/available-tns/npanxxs/"

        # Process optional query parameters
        query_parameters = {
            "limit": limit,
            "npa": npa,
            "page": page
        }
        query_builder = APIHelper.append_url_with_query_parameters(query_builder, query_parameters)

        # Validate and preprocess url
        query_url = APIHelper.clean_url(query_builder)

        # Prepare headers
        headers = {
            "user-agent": "Flowroute SDK 1.0",
            "accept": "application/json",
        }

        # Prepare and invoke the API call request to fetch the response
        response = CustomAuthUtility.appendCustomAuthParams(method='GET',
                                                            query_url=query_url,
                                                            headers=headers)

        # Error handling using HTTP status codes
        if response.code == 400:
            raise APIException("USER ERROR", 400, response.body)

        elif response.code == 500:
            raise APIException("APPLICATION/SERVER ERROR", 500, response.body)

        elif response.code < 200 or response.code > 206:  # 200 = HTTP OK
            raise APIException("HTTP Response Not OK", response.code, response.body)
        
        return response.body

    @staticmethod
    def list_available_np_as(limit=200):
        """Does a GET request to /available-tns/npas/.

        Retrieves a list of all NPAs (area codes) that contain purchasable
        telephone numbers.

        Args:
            limit (int): Number of items to display (Max 200).

        Returns:
            mixed: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        # The base uri for api requests
        query_builder = Configuration.BASE_URI
 
        # Prepare query string for API call
        query_builder += "/available-tns/npas/"

        # Process optional query parameters
        query_parameters = {
            "limit": limit
        }

        query_builder = APIHelper.append_url_with_query_parameters(query_builder, query_parameters)

        # Validate and preprocess url
        query_url = APIHelper.clean_url(query_builder)

        # Prepare headers
        headers = {
            "user-agent": "Flowroute SDK 1.0",
            "accept": "application/json",
        }

        # Prepare and invoke the API call request to fetch the response
        response = CustomAuthUtility.appendCustomAuthParams(method='GET',
                                                            query_url=query_url,
                                                            headers=headers)

        # Error handling using HTTP status codes
        if response.code == 400:
            raise APIException("USER ERROR", 400, response.body)

        elif response.code == 500:
            raise APIException("APPLICATION/SERVER ERROR", 500, response.body)

        elif response.code < 200 or response.code > 206:  # 200 = HTTP OK
            raise APIException("HTTP Response Not OK", response.code, response.body)
        
        return response.body

    @staticmethod
    def search(limit=None,
               npa=None,
               nxx=None,
               page=None,
               ratecenter=None,
               state=None,
               tn=None):
        """Does a GET request to /available-tns/tns/.

        TODO: type endpoint description here.

        Args:
            limit (int, optional): Number of items to display (Max 200)
            npa (int, optional): Restricts the results to the three digit NPA
                (area code) specified. This is optional, unless NXX is
                present
            nxx (int, optional): Restricts the results to the three digit NXX
                (exchange) specified.
            page (int, optional): Page to display
            ratecenter (string, optional): Restricts the results to the
                ratecenter specified. If present, state is required
            state (string, optional): Restricts the results to the state
                specified. This is optional, unless ratecenter is present.
            tn (string, optional): Restricts the results to the telephone
                number specified.

        Returns:
            mixed: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        # The base uri for api requests
        query_builder = Configuration.BASE_URI
 
        # Prepare query string for API call
        query_builder += "/available-tns/tns/"

        # Process optional query parameters
        query_parameters = {
            "limit": limit,
            "npa": npa,
            "nxx": nxx,
            "page": page,
            "ratecenter": ratecenter,
            "state": state,
            "tn": tn
        }

        query_builder = APIHelper.append_url_with_query_parameters(query_builder, query_parameters)

        # Validate and preprocess url
        query_url = APIHelper.clean_url(query_builder)

        # Prepare headers
        headers = {
            "user-agent": "Flowroute SDK 1.0",
            "accept": "application/json",
        }

        # Prepare and invoke the API call request to fetch the response
        response = CustomAuthUtility.appendCustomAuthParams(method='GET',
                                                            query_url=query_url,
                                                            headers=headers)

        # Error handling using HTTP status codes
        if response.code == 400:
            raise APIException("USER ERROR", 400, response.body)

        elif response.code == 500:
            raise APIException("APPLICATION/SERVER ERROR", 500, response.body)

        elif response.code < 200 or response.code > 206:  # 200 = HTTP OK
            raise APIException("HTTP Response Not OK", response.code, response.body)
        
        return response.body
