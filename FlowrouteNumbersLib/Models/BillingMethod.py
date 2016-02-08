# -*- coding: utf-8 -*-

"""
   FlowrouteNumbersLib.Models.BillingMethod
 
   This file was automatically generated for flowroute by APIMATIC BETA v2.0 on 02/08/2016
"""
from FlowrouteNumbersLib.APIHelper import APIHelper

class BillingMethod(object):

    """Implementation of the 'Billing Method' model.

    TODO: type model description here.

    Attributes:
        billing_method (string): VPRI or METERED

    """

    def __init__(self,
                 **kwargs):
        """Constructor for the BillingMethod class
        
        Args:
            **kwargs: Keyword Arguments in order to initialise the
                object. Any of the attributes in this object are able to
                be set through the **kwargs of the constructor. The values
                that can be supplied and their types are as follows::

                    billing_method -- string -- Sets the attribute billing_method
        
        """
        # Set all of the parameters to their default values
        self.billing_method = None

        # Create a mapping from API property names to Model property names
        replace_names = {
            "billing_method": "billing_method",
        }

        # Parse all of the Key-Value arguments
        if kwargs is not None:
            for key in kwargs:
                # Only add arguments that are actually part of this object
                if key in replace_names:
                    setattr(self, replace_names[key], kwargs[key])

    def resolve_names(self):
        """Creates a dictionary representation of this object.
        
        This method converts an object to a dictionary that represents the
        format that the model should be in when passed into an API Request.
        Because of this, the generated dictionary may have different
        property names to that of the model itself.
        
        Returns:
            dict: The dictionary representing the object.
        
        """
        # Create a mapping from Model property names to API property names
        replace_names = {
            "billing_method": "billing_method",
        }

        retval = dict()

        return APIHelper.resolve_names(self, replace_names, retval)