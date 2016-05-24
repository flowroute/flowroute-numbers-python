# -*- coding: utf-8 -*-

"""
    FlowrouteNumbersLib

    Copyright Flowroute, Inc. 2016
"""
import unirest
import hmac
import hashlib
import datetime as dt
from urlparse import parse_qsl, urlparse
from urllib import urlencode
from Configuration import *


class CustomAuthUtility:

    @staticmethod
    def appendCustomAuthParams(method='GET',
                               query_url=Configuration.BASE_URI,
                               body='',
                               headers={}):
        """
        Appends the necessary OAuth credentials for making this authorized call

        :param method: The outgoing request method
        :type string: GET, PUT, PATCH, POST, DELETE
        :param query_url: URL to make the request to
        :type string:
        :param body: request payload
        :type string:
        :param headers: The out going request to access the resource
        :type dict: Header dictionary
        """

        timestamp = dt.datetime.utcnow().replace(microsecond=0).isoformat()
        headers['X-Timestamp'] = timestamp

        body_hash = ""
        if body:
            # TODO: implement conditions for body transposing into a md5 hash
            #       and accommodate for handling form data
            body_hash = hashlib.md5(body).hexdigest() if body != '' else ''

        parsed_url = urlparse(query_url)
        qpd = dict(parse_qsl(parsed_url.query))
        qp = sorted(qpd.items())
        ordered_qp = urlencode(qp)

        canonical_uri = '{0}://{1}{2}\n{3}'.format(parsed_url.scheme,
                                                   parsed_url.netloc,
                                                   parsed_url.path,
                                                   ordered_qp)

        tokens = (timestamp, method, body_hash, canonical_uri)
        message_string = u'\n'.join(tokens).encode('utf-8')
        signature = hmac.new(Configuration.password, message_string, 
                             digestmod=hashlib.sha1).hexdigest()

        url = canonical_uri.replace('\n', '?')

        response = ''
        if method == 'GET':
            response = unirest.get(url,
                                   auth=(Configuration.username, signature),
                                   headers=headers,
                                   params=body)
        elif method == 'PUT':
            response = unirest.put(url,
                                   auth=(Configuration.username, signature),
                                   headers=headers,
                                   params=body)
        elif method == 'POST':
            response = unirest.post(url,
                                    auth=(Configuration.username, signature),
                                    headers=headers,
                                    params=body)
        elif method == 'PATCH':
            response = unirest.patch(url,
                                     auth=(Configuration.username, signature),
                                     headers=headers,
                                     params=body)
        elif method == 'DELETE':
            response = unirest.delete(url,
                                      auth=(Configuration.username, signature),
                                      headers=headers,
                                      params=body)
        else:
            raise ValueError('Invalid HTTP Method was used.')

        return response
