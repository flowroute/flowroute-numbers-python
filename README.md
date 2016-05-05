# flowroute-numbers-python

## About the flowroute-numbers-python SDK

Flowroute-numbers-python is a Python API Wrapper that provides methods for interacting with **v1** (version 1) of the [Flowroute](https://www.flowroute.com) API. These methods can be used to accomplish the following:

* Search for purchasable phone numbers
* Purchase phone numbers
* View the phone numbers you own, as well as their related details
* Create a new inbound route
* Update the primary and failover route on a phone number

## Documentation 
The full documentation for Flowroute's v1 API is available at [Flowroute Developer Portal](https://developer.flowroute.com/).

## Install the required libraries 

The SDK uses the **Unirest** and **jsonpickle** Python libraries, which must be installed before you can use the SDK. 
> **Note:** You must be connected to the Internet in order to install the required libraries.

2. If needed, create a parent directory folder where you want to install the SDK.
 
3. Go to the parent directory, and run the following:

 	`git clone https://github.com/flowroute/flowroute-numbers-python.git`
 	
 	The `git clone` command clones the **flowroute-numbers-python** respository as a sub directory within the parent folder.
 	
4.	Change directories to the newly created **flowroute-numbers-python** directory.

5.	Run the following:

	`pip install -r requirements.txt`

6.	Import the SDK.

  
## Import the SDK

The following describes how to import the Python SDK and set up your API credentials. Before you start, you should have your API credentials (Access Key and Secret Key). These can be found on the **Preferences > API Control** page of the [Flowroute](https://manage.flowroute.com/accounts/preferences/api/) portal.

>**Note:** If you do not have API credentials, contact <mailto:support@flowroute.com>.

1.	From the **flowroute-number-python** directory, run

	`python`
		
2.	At the `>>>` prompt run the following import commands:

	`from FlowrouteNumbersLib.Controllers.InboundRoutesController  import *`
	`from FlowrouteNumbersLib.Controllers.PurchasablePhoneNumbersController  import *`
	`from FlowrouteNumbersLib.Controllers.TelephoneNumbersController  import *`
	`from FlowrouteNumbersLib.Models  import *  `      
   
3.	Run the following, replacing the *`Access Key`* and *`Secret Key`* variables within the quotes (`""`) with your own Access Key and Secret Key::

		Configuration.username="Access Key"
		Configuration.password="Secret Key"
	
	> **Note:** These variables can also be hard coded in the **Configuration.py** file instead of being overwritten in code.

4.	Instantiate your controllers for later use
	
		irc = InboundRoutesController()
		pnc = PurchasablePhoneNumbersController()
		tnc = TelephoneNumbersController()
	

## PurchasablePhoneNumbersController

The Purchasable Phone Numbers Controller contains all methods neccesary to search through Flowroute's phone number inventory. 

### `list_available_np_as(self,limit=None)`

The `list_available_np_as()` method retrieves a list of every NPA (area code) available in Flowroute's phone number inventory.

####Usage

	pnc.list_available_np_as(limit=x)

| Parameter | Required | Usage                                 |
|-----------|----------|---------------------------------------|
| `limit=x`  | True    | Controls the number of items returned. The number must be 1 (one) to 200.  |

##### Example Usage
The following example passes `2` as the number of items to return. 

	pnc.list_available_np_as(limit=2)	

#####Example response

Results are returned in numerical order, starting with the lowest NPA number.

>**Note:** The following response is formatted only to provide an example of what the output can include. It is not intended to show the output in your installation.

	{
 	 "npas": {
 	   "201": {
 	     "nxxs": "/v1/available-tns/npanxxs/?npa=201",
  	    "tns": "/v1/available-tns/tns/?npa=201"
 	   },
 	   "202": {
	      "nxxs": "/v1/available-tns/npanxxs/?npa=202",
	      "tns": "/v1/available-tns/tns/?npa=202"
	    }
	  },
	  "links": {
  	  "next": "/v1/available-tns/npas/?limit=2&page=2"
	  }
	}
#####Error response
The following errors can be returned:

| Error code | Message  | Description                                                 |
|------------|----------|-------------------------------------------------------|
|No code number  |Response Not OK|This error is most commonly returned when the number passed in the method is greater than the allowed maximum.|
|500  |Application Error|This error is most commonly returned when `0` is passed.|

###`list_area_and_exchange(self,limit=None,npa=None,page=None)`

The `list_area_and_exchange()` method retrieves a list of every NPA-NXX (area code and exchange) available in Flowroute's phone number inventory.

#####Usage
`pnc.list_area_and_exchange(limit=x,npa=x,page=x)`

| Parameter | Required | Usage                                                         |
|-----------|----------|---------------------------------------------------------------|
| limit     | False    | Controls the number of items returned. This can be a maximum of 200.                         |
| npa       | False    | Limits results to the specified NPA (area code). |
| page      | False    | Sets which page of the results is returned in the output.             |

##### Example Usage
The following example sets a limit of `2`, `206` for the NPA, and to display page `2` in the output.

`pnc.list_area_and_exchange(limit=2,npa=206,page=2)`

#####Example response

Results are returned in numerical order, starting with the lowest NPA number. The `npaxxs` variable is formatted as a combination of the area code and exchange. In the following example, `206258` is area code `206` and exchange `258`. 

>**Note:** The following response is formatted only for display purposes. It is not intended to show the actual response formatting.

	{
  	"npanxxs": {
  	  "206258": {
  	    "tns": "/v1/available-tns/tns/?npa=206&nxx=258"
 	   },
 	   "206238": {
 	     "tns": "/v1/available-tns/tns/?npa=206&nxx=238"
	    }
	  },
	  "links": {
	    "prev": "/v1/available-tns/npanxxs/?npa=206&limit=2&page=1",
	    "next": "/v1/available-tns/npanxxs/?npa=206&limit=2&page=3"
 	 }
	}

#####Error response
The following error can be returned:

| Error code | Message  | Description                                                 |
|------------|----------|-------------------------------------------------------|
|No code number  |Response Not OK|This error is most commonly returned when the number passed in the method is greater than the allowed maximum.|
|500  |Application Error|This error is most commonly returned when `0` is passed.|

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
