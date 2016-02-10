# -*- coding: utf-8 -*-

"""
   FlowrouteNumbersLib.Controllers.TelephoneNumbersController

   This file was automatically generated for flowroute by APIMATIC BETA v2.0 on 02/08/2016
"""
import unirest

from FlowrouteNumbersLib.APIHelper import APIHelper
from FlowrouteNumbersLib.Configuration import Configuration
from FlowrouteNumbersLib.APIException import APIException
from FlowrouteNumbersLib.CustomAuthUtility import CustomAuthUtility


class TelephoneNumbersController(object):


    """A Controller to access Endpoints in the FlowrouteNumbersLib API."""

    def telephone_number_details(self,
                                 telephone_number):
        """Does a GET request to /tns/{telephone_number}.

        Returns the routing and billing information for the specified
        telephone number on your account

        Args:
            telephone_number (string): This is the TN for which you would like
                to retrieve configuration details for

        Returns:
            string: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        # The base uri for api requests
        query_builder = Configuration.BASE_URI
 
        # Prepare query string for API call
        query_builder += "/tns/{telephone_number}"

        # Process optional template parameters
        query_builder = APIHelper.append_url_with_template_parameters(query_builder, { 
            "telephone_number": telephone_number
        })

        # Validate and preprocess url
        query_url = APIHelper.clean_url(query_builder)

        # Prepare headers
        headers = {

            "user-agent": "Flowroute SDK 1.0",

        }

        #append custom auth authorization
        #CustomAuthUtility.appendCustomAuthParams(headers)

        # Prepare and invoke the API call request to fetch the response
        #response = unirest.get(query_url, headers=headers)
        response = CustomAuthUtility.appendCustomAuthParams(method='GET',
            query_url=query_url, headers=headers)

        # Error handling using HTTP status codes
        if response.code == 400:
            raise APIException("USER ERROR", 400, response.body)

        elif response.code == 500:
            raise APIException("APPLICATION/SERVER ERROR", 500, response.body)

        elif response.code < 200 or response.code > 206:  # 200 = HTTP OK
            raise APIException("HTTP Response Not OK", response.code, response.body)
        
        return response.body

    def purchase(self,
                 billing,
                 number):
        """Does a PUT request to /tns/{number}.

        Purchases the telephone number indicated by the request URI, with the
        billing method indicated in the body. Allowable billing methods are
        returned in the search results for available telephone numbers.

        Args:
            billing (BillingMethod): The billing method to apply to the
                telephone number being purchased.
            number (string): Telephone number to purchase

        Returns:
            string: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        # The base uri for api requests
        query_builder = Configuration.BASE_URI
 
        # Prepare query string for API call
        query_builder += "/tns/{number}"

        # Process optional template parameters
        query_builder = APIHelper.append_url_with_template_parameters(query_builder, { 
            "number": number
        })

        # Validate and preprocess url
        query_url = APIHelper.clean_url(query_builder)

        # Prepare headers
        headers = {

            "user-agent": "Flowroute SDK 1.0",
            "content-type": "application/json; charset=utf-8",

        }
        # Quick kwargs setting
        #body = '{"billing_method": "%s"}' % billing
        body = APIHelper.json_serialize(billing)

        #append custom auth authorization
        #CustomAuthUtility.appendCustomAuthParams(headers)

        # Prepare and invoke the API call request to fetch the response
        #response = unirest.put(query_url, headers=headers,  params=APIHelper.json_serialize(billing))
        response = CustomAuthUtility.appendCustomAuthParams(method='PUT',
            query_url=query_url, body=body, headers=headers)

        # Error handling using HTTP status codes
        if response.code == 400:
            raise APIException("USER ERROR", 400, response.body)

        elif response.code == 500:
            raise APIException("APPLICATION/SERVER ERROR", 500, response.body)

        elif response.code < 200 or response.code > 206:  # 200 = HTTP OK
            raise APIException("HTTP Response Not OK", response.code, response.body)
        
        return response.body

    def list_account_telephone_numbers(self,
                                       limit=None,
                                       page=None,
                                       pattern=None):
        """Does a GET request to /tns/.

        Retrieves a list of all the phone numbers on your account

        Args:
            limit (int, optional): Number of items to display (max 200)
            page (int, optional): Page to display
            pattern (string, optional): A full or partial telephone number to
                search for

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
        query_builder += "/tns/"

        # Process optional query parameters
        query_parameters = {
            "limit": limit,
            "page": page,
            "pattern": pattern
        }
        query_builder = APIHelper.append_url_with_query_parameters(query_builder, query_parameters)

        # Validate and preprocess url
        query_url = APIHelper.clean_url(query_builder)

        # Prepare headers
        headers = {

            "user-agent": "Flowroute SDK 1.0",
            "accept": "application/json",

        }

        #append custom auth authorization
        #CustomAuthUtility.appendCustomAuthParams(headers)

        # Prepare and invoke the API call request to fetch the response
        #response = unirest.get(query_url, headers=headers)
        response = CustomAuthUtility.appendCustomAuthParams(method='GET',
            query_url=query_url, headers=headers)

        # Error handling using HTTP status codes
        if response.code == 400:
            raise APIException("USER ERROR", 400, response.body)

        elif response.code == 500:
            raise APIException("APPLICATION/SERVER ERROR", 500, response.body)

        elif response.code < 200 or response.code > 206:  # 200 = HTTP OK
            raise APIException("HTTP Response Not OK", response.code, response.body)
        
        return response.body

    def update(self,
               number,
               routes):
        """Does a PATCH request to /tns/{number}.

        Updates the routing information for a telephone number on your
        account, as indicated by the specified URI. The body of the request
        requires two routes listed in order of preference (primary first and
        fail over second).

        Args:
            number (string): The telephone number who's routing you wish to
                update
            routes (list of Route): JSON string containing the The routes
                obtained from the routes resource that you would like to point
                your telephone number to.

        Returns:
            string: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        # The base uri for api requests
        query_builder = Configuration.BASE_URI
 
        # Prepare query string for API call
        query_builder += "/tns/{number}"

        # Process optional template parameters
        query_builder = APIHelper.append_url_with_template_parameters(query_builder, { 
            "number": number
        })

        # Validate and preprocess url
        query_url = APIHelper.clean_url(query_builder)

        # Prepare headers
        headers = {

            "user-agent": "Flowroute SDK 1.0",
            "content-type": "application/json; charset=utf-8",

        }
        routes = APIHelper.json_serialize(routes)
        body = '{"routes": %s}' % routes

        #append custom auth authorization
        #CustomAuthUtility.appendCustomAuthParams(headers)

        # Prepare and invoke the API call request to fetch the response
        #response = unirest.patch(query_url, headers=headers,  params=APIHelper.json_serialize(routes))
        response = CustomAuthUtility.appendCustomAuthParams(method='PATCH',
            query_url=query_url, body=body, headers=headers)

        # Error handling using HTTP status codes
        if response.code == 400:
            raise APIException("USER ERROR", 400, response.body)

        elif response.code == 500:
            raise APIException("APPLICATION/SERVER ERROR", 500, response.body)

        elif response.code < 200 or response.code > 206:  # 200 = HTTP OK
            raise APIException("HTTP Response Not OK", response.code, response.body)
        
        return response.body
