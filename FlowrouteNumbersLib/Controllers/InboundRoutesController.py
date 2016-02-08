# -*- coding: utf-8 -*-

"""
   FlowrouteNumbersLib.Controllers.InboundRoutesController

   This file was automatically generated for flowroute by APIMATIC BETA v2.0 on 02/08/2016
"""
import unirest

from FlowrouteNumbersLib.APIHelper import APIHelper
from FlowrouteNumbersLib.Configuration import Configuration
from FlowrouteNumbersLib.APIException import APIException


class InboundRoutesController(object):


    """A Controller to access Endpoints in the FlowrouteNumbersLib API."""

    def list(self,
             limit=None,
             page=None):
        """Does a GET request to /routes/.

        TODO: type endpoint description here.

        Args:
            limit (int, optional): Number of items to display (max 200)
            page (int, optional): Page to display if paginated

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
        query_builder += "/routes/"

        # Process optional query parameters
        query_parameters = {
            "limit": limit,
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

        #append custom auth authorization
        CustomAuthUtility.appendCustomAuthParams(headers)

        # Prepare and invoke the API call request to fetch the response
        response = unirest.get(query_url, headers=headers)

        # Error handling using HTTP status codes
        if response.code == 400:
            raise APIException("USER ERROR", 400, response.body)

        elif response.code == 500:
            raise APIException("APPLICATION/SERVER ERROR", 500, response.body)

        elif response.code < 200 or response.code > 206:  # 200 = HTTP OK
            raise APIException("HTTP Response Not OK", response.code, response.body)
        
        return response.body

    def create_new_route(self,
                         route_name,
                         mtype,
                         value):
        """Does a PUT request to /routes/{route_name}.

        Create a new inbound route to be used by a phone number

        Args:
            route_name (string): New unique name for the route
            mtype (string): Type of inbound route
            value (string): The value to be associated with a route.

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
        query_builder += "/routes/{route_name}"

        # Process optional template parameters
        query_builder = APIHelper.append_url_with_template_parameters(query_builder, { 
            "route_name": route_name
        })

        # Validate and preprocess url
        query_url = APIHelper.clean_url(query_builder)

        # Prepare headers
        headers = {

            "user-agent": "Flowroute SDK 1.0",
            "content-type": "application/json; charset=utf-8",

        }

        #append custom auth authorization
        CustomAuthUtility.appendCustomAuthParams(headers)

        # Prepare and invoke the API call request to fetch the response
        response = unirest.put(query_url, headers=headers,  params=mtype)

        # Error handling using HTTP status codes
        if response.code == 400:
            raise APIException("USER ERROR", 400, response.body)

        elif response.code == 500:
            raise APIException("APPLICATION/SERVER ERROR", 500, response.body)

        elif response.code < 200 or response.code > 206:  # 200 = HTTP OK
            raise APIException("HTTP Response Not OK", response.code, response.body)
        
        return response.body
