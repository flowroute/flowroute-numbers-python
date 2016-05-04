# flowroute-numbers-python

## About the flowroute-numbers-python SDK

Flowroute-numbers-python is a Python API Wrapper that provides methods for interacting with [Flowroute's](https://www.flowroute.com) v1 API. These methods can be used to accomplish the following:

* Search for purchasable phone numbers
* Purchase phone numbers
* View your owned phone numbers and their related details
* Create new inbound routes
* Update the primary and failover route on a phone number

## Documentation 
The full documentation for Flowroute's v1 API is available at [Developer.flowroute.com](https://developer.flowroute.com/).

## Install the required libraries 

The SDK uses the **Unirest** and **jsonpickle** Python libraries, which must be installed before you can use the SDK. 
> **Note:** You must be connected to the Internet in order to install the required libraries.

1. Open a terminal session. 

2. Run the following two commands:
#####
	`cd flowroute-numbers-python/`
	
	`pip install -r requirements.txt`

  
## Import the SDK

The following shows how to import the SDK API Wrapper and setup your API credentials.

1) Run the following to import the SDK module:

	from FlowrouteNumbersLib.Controllers.InboundRoutesController  import *
	from FlowrouteNumbersLib.Controllers.PurchasablePhoneNumbersController  import *
	from FlowrouteNumbersLib.Controllers.TelephoneNumbersController  import *
	from FlowrouteNumbersLib.Models  import *        
   
2) Configure your API Username and Password from [Flowroute Manager](https://manage.flowroute.com/accounts/preferences/api/).
 > If you do not have an API Key contact <mailto:support@flowroute.com>:

	Configuration.username="AccessKey"
	Configuration.password="SecretKey"
	
> These variables can also be hard coded in the Configuration.py file instead of being overwritten in code.

3) Instantiate your controllers for later use

	irc = InboundRoutesController()
	pnc = PurchasablePhoneNumbersController()
	tnc = TelephoneNumbersController()
	


## List of Methods and Example Uses

### PurchasablePhoneNumbersController

The Purchasable Phone Numbers Controller contains all of the methods neccesary to search through Flowroute's phone number inventory. 

#### list_available\_np\_as(self,limit=None)

The list_available\_np\_as method allows you to retrieve a list of every NPA (area code) available in Flowroute's phone number inventory.

| Parameter | Required | Usage                                 |
|-----------|----------|---------------------------------------|
| limit     | False    | Controls the number of items returned (Max 200) |

##### Example Usage
	
	pnc.list_available_np_as()

#### list_area_and_exchange(self,limit=None,npa=None,page=None)

The list_area_and_exchange method allows you to retrieve a list of every NPA-NXX (area code and exchange) available in Flowroute's phone number inventory.

| Parameter | Required | Usage                                                         |
|-----------|----------|---------------------------------------------------------------|
| limit     | False    | Controls the number of items returned (Max 200)                         |
| npa       | False    | Limits results to the specified NPA (also known as area code) |
| page      | False    | Determines which page of the results is returned              |

##### Example Usage
		
	pnc.list_area_and_exchange()
	
#### search(self,limit=None,              npa=None,nxx=None,page=None,ratecenter=None,state=None,tn=None)

The search method is the most robust option for searching through Flowroute's purchasable phone number inventory. It allows you to search by NPA, NXX, Ratecenter, State, and TN.

| Parameter  | Required                       | Usage                                                                     |
|------------|--------------------------------|---------------------------------------------------------------------------|
| limit      | False                          | Controls the number of items returned (Max 200)                                     |
| npa        | False, unless nxx is present   | Limits results to the specified NPA (also known as area code)             |
| nxx        | False                          | Limits results to the specified NXX (also known as exchange)              |
| page       | False                          | Determines which page of the results is returned                          |
| ratecenter | False                          | Limits results to the specified ratecenter                                |
| state      | False, unless state is present | Limits results to the specified state                                     |
| tn         | False                          | Limits results to the specified telephone number (supports prefix search) |

##### Example Usage

	pnc.search()
	
### TelephoneNumbersController

The Telephone Numbers Controller contains all of the methods neccesary to purchase a new phone number and to manage your owned phone number inventory.

#### purchase(self,billing,number)	

The purchase method is used to purchase a telephone number from Flowroute's inventory.

| Parameter       | Required | Usage                                                                                |
|-----------------|----------|--------------------------------------------------------------------------------------|
| billing         | True     | A JSON object that specifies which billing method to use. Either "METERED" or "VPRI" |
| telephoneNumber | True     | The telephone number that you would like to purchase                                 |
	
##### Example Usage

	billing = BillingMethod(billing_method="VPRI")
	number = "15852003968"
	tnc.purchase(billing,number)

> If your query is succesful you will be returned an empty string and a 201 Created

#### list\_account\_telephone_numbers(self,limit=None,page=None,pattern=None)

The list\_account\_telephone_numbers method is used to retrieve a list of all of the phone numbers on your Flowroute account.

| Parameter | Required | Usage                                                     |
|-----------|----------|-----------------------------------------------------------|
| limit     | False    | Controls the number of items returned (Max 200)           |
| page      | False    | Determines which page of the results is returned          |
| pattern   | False    | A telephone number to search for (supports prefix search) |

##### Example Usage
	
	tnc.list_account_telephone_numbers(limit=1,page=2,pattern=1206)

#### telephone\_number\_details(self,telephone_number)

The telephone\_number\_details method is used to retrieve the billing method, primary route, and failover route for the specified telephone number. 

| Parameter       | Required | Usage                                             |
|-----------------|----------|---------------------------------------------------|
| telephoneNumber | True     | The telephone number that you would like to query |

##### Example Usage

	tnc.telephone_number_details(12064205788)

#### update(self,number,routes)

The update method is used to update both the primary and failover route for a phone number. Both the primary and failover route must be specified inside of an array (see Example Usage). The first route name specified will be assigned as the primary route and the second route name specified will be assigned as the failover route. The list of available route names can be retrieved by using the list method in the InboundRoutesController.

| Parameter       | Required | Usage                                                                  |
|-----------------|----------|------------------------------------------------------------------------|
| telephoneNumber | True     | The telephone number that you would like to update routes for          |
| routes          | True     | The names of the primary and failover routes for the phone number (must be an array) |

##### Example Usage
	
	rtes = [Route(name='sip-reg'), Route(name='ea4f4056663e27b082999689982e4723')]
	tnc.update(number=12064205780, routes=rtes)

### InboundRoutesController

The Inbound Routes Controller contains the methods required to view all of your existing inbound routes and to create new inbound routes.

#### list(self,limit=None,page=None)

The list method is used to return all of the existing inbound routes from your Flowroute account.

| Parameter | Required | Usage                                            |
|-----------|----------|--------------------------------------------------|
| limit     | False    | Controls the number of items returned (Max 200)  |
| page      | False    | Determines which page of the results is returned |

##### Example Usage

	irc.list()
	
#### create\_new\_route(self,route_name,mtype,value)

The create\_new\_route method is used to create a new inbound route.

| Parameter | Required | Usage                                                                                   |
|-----------|----------|-----------------------------------------------------------------------------------------|
| route_name | True     | The name you would like to assign to the new route (supports alphanumeric characters)   |
| mtype      | True     | The type of route you would like to create. Valid options are "HOST", "PSTN", and "URI" |
| value     | True     | The actual route that you would like to create                                          |

##### Example Usage

	irc.create_new_route(route_name='PSTNroute1',mtype='PSTN',value='18002364455')	
	irc.create_new_route(route_name='HOSTroute1',mtype='HOST',value='24.239.23.40:5060')
	irc.create_new_route(route_name='URIroute1',mtype='URI',value='sip:120664480000@215.122.69.152:5060')
