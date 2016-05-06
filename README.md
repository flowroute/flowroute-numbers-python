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

	`from FlowrouteNumbersLib.Controllers.InboundRoutesController import *` <br>
	`from FlowrouteNumbersLib.Controllers.PurchasablePhoneNumbersController import *` <br>
	`from FlowrouteNumbersLib.Controllers.TelephoneNumbersController import *`<br>
	`from FlowrouteNumbersLib.Models import * ` <br>
   
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

	pnc.list_available_np_as()

The method takes the following parameter:

| Parameter | Required | Usage                                 |
|-----------|----------|---------------------------------------|
| `limit`  | True    | Controls the number of items returned. The number must be `1` (one) to `200`.  |

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
|No code number  |Response Not OK|This error is most commonly returned when the number passed in the method is greater than the allowed maximum of `200`.|
|500  |Application Error|This error is most commonly returned when `0` is passed for the `limit`.|

###`list_area_and_exchange(self,limit=None,npa=None,page=None)`

The `list_area_and_exchange()` method retrieves a list of every NPA-NXX (area code and exchange) available in Flowroute's phone number inventory.

#####Usage
`pnc.list_area_and_exchange()`

The method can take the following parameters:

| Parameter | Required | Usage                                                         |
|-----------|----------|---------------------------------------------------------------|
| limit     | False    | Controls the number of items returned. This can be a maximum of `200`. If no limit is passed,  `10` results are returned as the default. These results are organized numerically by the combination of NPA and NXX. For example, *`206258`* is NPA *`206`* and NXX *`258`*.                   |
| npa       | False    | Limits results to the specified NPA (area code). |
| page      | False    | Sets which page of the results is returned in the output. When set, `prev` and `next` page links appear in the response.|            |

##### Example Usage
The following example sets `2` for the `limit`, `206` for the `npa`, and to display `page` `2` in the output:

`pnc.list_area_and_exchange(limit=2,npa=206,page=2)`

#####Example response

Results are returned in numerical order, starting with the lowest NPA number. The `npaxxs` variable is formatted as a combination of the area code and exchange. In the following example, `206258` is the combination of area code `206` and exchange `258`. 

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
|No code number  |Response Not OK|This error is most commonly returned when the number passed for the limit is greater than the allowed maximum of 200.|
|500  |Application Error|This error is most commonly returned when `0` is passed for the `limit`.|

### `search(self,limit=None,              npa=None,nxx=None,page=None,ratecenter=None,state=None,tn=None)`

The search method is is used to search by NPA, NXX, Ratecenter, State, or TN (telephone number). 
##### Usage

	pnc.search()

The method can take the following parameters:

| Parameter  | Required                       | Usage                                                                     |
|------------|--------------------------------|--------------------------------------------------------------------|
| `limit`      | False                          |Controls the number of items returned. This can be a maximum of 200.                                         These results are organized numerically by the combination of NPA and NXX. For example, *`206258`* is NPA *`206`* and NXX *`258`*.   |
| `npa`        | False, unless *`nxx`* is present   | Limits results to the specified NPA (area code).             |
| `nxx`        | False                          | Limits the results to the specified NXX (exchange).              |
| `page`       | False                          | Sets which page of the results is returned in the output. When set, `prev` and `next` page links appear in the response.                         |
| `ratecenter` | False                          | Limits results to the specified *`ratecenter`*.                                |
| `state`      | False, unless *`ratecenter`* is passed. | Limits results to the specified two-character state or territory code.                                    |
| `tn`         | False                          | Limits results to the specified telephone number. This field uses partial match search. For example, if *`206`* is passed, all results that include *`206`* are returned. |

##### Example Usage

	pnc.search(limit=1,npa=206,nxx=743,page=1,ratecenter='seattle',state='wa')
	
>**Note:** The following response is formatted only for display purposes. It is not intended to show the actual response formatting.	
	
	{
  	"links": {
  	  "next": "/v1/available-tns/tns/?npa=206&nxx=743&state=wa&ratecenter=seattle&limit=1&page=2"
 	 },
 	 "tns": {
	    "12067439178": {
	     "initial_cost": "1.00",
 	     "monthly_cost": "1.25",
  	    "state": "WA",
  	    "ratecenter": "SEATTLE",
  	    "billing_methods": [
  	      "VPRI",
   	     "METERED"
   	   ]
 	   }
 		 }
	}
#####Response fields
The following fields are returned in the response:

Parameter | Description                                             |
|--------|-------------------------------------------------------|
| `tns`  | Object composed of *`telephonenumber`*.|                           |
||	 <li>*`telephone number`*: The retrieved telephone number object, which is composed of:|
||	<li><ul> `initial_cost`: The one-time fixed cost for that telephone number. The default value is USD `1.00`.|
| | 	<li> <ol>`monthly_cost`: The recurring monthly cost to maintain that telephone number. The default value is USD `1.25`.|
||	<li>`state`: The US State or Canadian territory in which the NPA/NXX is located.|
||	<li>`ratecenter`: The ratecenter associated with the NPA/NXX.</ol>|
||	<li> `billing_methods`: Displays the two billing methods for the telephone number: `VPRI` or `METERED`. </li> |

	
##TelephoneNumbersController

The Telephone Numbers Controller contains all of the methods neccesary to purchase a new phone number and to manage your owned phone number inventory.

#### `purchase(self,billing,number)`	

The purchase method is used to purchase a telephone number from Flowroute's inventory.

##### Usage

 *`billing`*` = BillingMethod(billing_method="VPRI" or "METERED")`</br>
 *`number`*`= "11-digit E.164-formatted telephone number"`<br>
 `tnc.purchase`*`(billing,number)`*

The method takes the following parameters:


| Parameter       | Required | Usage                                                                                |
|-----------------|----------|--------------------------------------------------------------------------------------|
| *`billing`*         | True     | Variable that sets the billing method  the BillingMethod. The variable is then associated with one of two billing methods, `VPRI` or `METERED`. <ul><li>`VPRI` are concurrent calls limited to the number of VPRI channels you have, but with unlimited usage on each channel.<li> `METERED` are unlimited concurrent calls, billed per-minute.</li>For this example, the variable is named *`billing`*.|
| *`number`* | True     | Variable that sets the phone number to purchase. Must be from the list of available Flowroute telephone numbers and must be formatted using an E.164 11-digit `1NPANXXXXXXXXX` format.</ul></br> For this example, the variable is named *`number`*.|                               |
	
##### Example Usage

	billing = BillingMethod(billing_method="VPRI")
	number = "15852003968"
	tnc.purchase(billing,number)

##### Example response
For a successful purchase, an empty string (`''`) is returned
#####Error response
The following error can be returned:

| Error code | Message  | Description                                                 |
|------------|----------|-------------------------------------------------------|
|No code number  |HTTP Response Not OK|The phone number to purchase might be incorrect.|

#### `list_account_telephone_numbers(self,limit=None,page=None,pattern=None)`


The `list_account_telephone_numbers` method is used to retrieve a list of all of the phone numbers on your Flowroute account.

#####Usage

`tnc.list_account_telephone_numbers()`

The method can take the following parameters:

| Parameter | Required | Usage                                                     |
|-----------|----------|-----------------------------------------------------------|
| `limit`  | True    | Controls the number of items returned. The number can be `1` (one) to `200`. If no `limit` is specified, a default value of `10` results are returned.  |
| `page`      | False    | If multiple pages of numbers are returned, this field displays the results from the set page.     |
| `pattern`   | False    |The telephone number on which to search. Partial search is supported; if any part of a telephone number is passed, the pattern will return *all* telephone numbers that include that pattern. |

##### Example Usage
	
	tnc.list_account_telephone_numbers(limit=5,page=2,pattern=206)

#####Example response
	{
	  "links": {
	    "prev": "/v1/tns/?limit=1&page=1",
	    "next": "/v1/tns/?limit=1&page=3"
 	 },
	  "tns": {
	    "12062092844": {
   		  "routes": [
   	     {
   	       "type": "SIP-REG",
   	       "name": "sip-reg"
   	     },
   	     {
   	       "type": "SIP-REG",
   	       "name": "sip-reg"
   	     }
   	   ],
   	   "billing_method": "METERED",
   	   "detail": "/v1/tns/12062092844"
   	 }
  	}
	}
#####Response fields

Parameter | Description                                             |
|--------|-------------------------------------------------------|
| `tns`  | Object composed of *`telephonenumber`*.|                           |
|| <li>*`telephone number`*: The telephone number you own. This object composed of the following:|
| |<li><ol>`Routes`: Defines the parameters of the route. Composed of the following:
| |	<li> <ol><ol>`type`: 
|	|<li> <ol><ol>`name`: Name of the route. If no route
||`billing_method`: This will be one of the two billing methods for that number, either `VPRI` or `METERED`.
||detail: Provides more detail that can be passed when using the `telephone_number_details` method below|
	
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
