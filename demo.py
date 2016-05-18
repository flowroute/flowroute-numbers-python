"""
demo.py

Flowroute-numbers-python is a Python API Wrapper that provides methods for interacting with v1 (version 1)
of the Flowroute API. These methods can be used to accomplish the following:

* Search for purchasable phone numbers
* Purchase phone numbers
* View the phone numbers you own, as well as their related details
* Create a new inbound route
* Update the primary and failover route on a phone number


Copyright Flowroute, Inc.  2016

"""
from FlowrouteNumbersLib.Controllers.InboundRoutesController import *
from FlowrouteNumbersLib.Controllers.PurchasablePhoneNumbersController import *
from FlowrouteNumbersLib.Controllers.TelephoneNumbersController import *
from FlowrouteNumbersLib.Models import *

import pprint

print("Number Control Demo")

# Setup your api credentials
Configuration.username = 'ACCESS_KEY'
Configuration.password = 'SECRET_KEY'

# -- Purchasable Phone Numbers --

# Create our controller
pnc = PurchasablePhoneNumbersController()

# Retrieve Available NPAs
print("--Retrieve Available NPAs")
response = pnc.list_available_np_as(limit=10)
pprint.pprint(response)

# Retrieve Available NPA NXXs
print("--Retrieve Available NPA NXXs\n")
response = pnc.list_area_and_exchange(limit=10)
pprint.pprint(response)

# Search for purchasable Numbers
print("--Search for numbers in Seattle Washington\n")
response = pnc.search(10, 206, 641, None, 'seattle', 'wa', None)
pprint.pprint(response)


# -- Telephone Numbers --
# Create our controller
tnc = TelephoneNumbersController()

# Purchase a Phone Number
print("--Purchase a Phone Number\n")
billing = BillingMethod(billing_method="VPRI")
number = '12066417607'

try:
    response = tnc.purchase(billing=billing, number=number)
    pprint.pprint(response)
except APIException as e:
    print("Error - " + str(e.response_code) + ' ' + e.response_body['error'] + '\n')

# List Account Phone Numbers
print("--List Account Phone Numbers\n")
try:
    response = tnc.list_account_telephone_numbers()
    pprint.pprint(response)
except APIException as e:
    print("Error - " + str(e.response_code) + ' ' + e.response_body['error'] + '\n')

# Retrieve Phone Number Details
print("--Retrieve Number Details\n")
try:
    response = tnc.telephone_number_details(number)
    pprint.pprint(response)
except APIException as e:
    print("Error - " + str(e.response_code) + ' ' + e.response_body['error'] + '\n')


# --- Inbound Routes
# Create our controller
irc = InboundRoutesController()

# Retrieve Routes
print("--Retrieve Inbound Routes\n")
response = irc.list()
pprint.pprint(response)
