# flowroute-numbers-python

Flowroute-numbers-python is a Python API Wrapper that provides methods for interacting with **v1** (version 1) of the [Flowroute](https://www.flowroute.com) API. These methods can be used to accomplish the following:

* Search for purchasable phone numbers
* Purchase phone numbers
* View the phone numbers you own, as well as their related details
* Create a new inbound route
* Update the primary and failover route on a phone number
* 
## Documentation 
The full documentation for v2 of the Flowroute API is available [here](https://developer.flowroute.com/v2.0/docs).

##Before you begin

The following are required before you can deploy the SDK.

### Have your API credentials

You will need your Flowroute API credentials (Access Key and Secret Key). These can be found on the **Preferences > API Control** page of the [Flowroute](https://manage.flowroute.com/accounts/preferences/api/) portal. If you do not have API credentials, contact <mailto:support@flowroute.com>.

### Know your Flowroute phone number

To create and send a message, you will need your Flowroute phone number, which should be enabled for SMS. If you do not know your phone number, or if you need to verify whether or not it is enabled for SMS, you can find it on the [DIDs](https://manage.flowroute.com/accounts/dids/) page of the Flowroute portal.

## Install the required libraries

The SDK uses the **Unirest** and **jsonpickle** Python libraries, which must be installed before you can use the SDK. 

> **Note:** You must be connected to the Internet in order to install the required libraries.

1. Open a terminal session. 

2. If needed, create a parent directory folder where you want to install the SDK.
 
3. Go to the newly created folder, and run the following:

 	`git clone https://github.com/flowroute/flowroute-numbering-python.git`
 	
 	The `git clone` command clones the **flowroute-numbering-python** repository as a sub directory within the parent folder.
 	
4.	Change directories to the newly created **flowroute-numbering-python** directory.

5.	Run the following:

	`pip install -r requirements.txt`

6.	Create a script to import the SDK.

## Create a PHP file to import the Controllers and Models<a name=createphp></a>

The following describes importing the SDK and setting up your API credentials. Importing the SDK allows you to instantiate the [Controllers](#controllers), which contain the methods used to perform tasks with the SDK. In order to do this, create and run a PHP file. 

When creating your own file for running the methods you will need to create one or more files that instantiate the Controllers and the methods. The following shows these lines. Depending on your approach, not all lines will be required.
	
		from FlowrouteNumbersLib.Controllers.InboundRoutesController import *
		from FlowrouteNumbersLib.Controllers.PurchasablePhoneNumbersController import *
		from FlowrouteNumbersLib.Controllers.TelephoneNumbersController import *
		from FlowrouteNumbersLib.Models import *
		
		Configuration.username="Access Key"
		Configuration.password="Secret Key"
		
		pnc = PurchasablePhoneNumbersController()
		tnc = TelephoneNumbersController()
		irc = InboundRoutesController()
		
		print (response)
	
			
>**Important:** Throughout this SDK, `response` is used in examples. `response` is a variable name that can be changed to a name of your own choosing. It can support an unlimited number of characters. If you choose to rename `response`, make sure that any method that references that variable name is also changed to use the new name. For example, you might have the following:
>
>`blob = pnc.list_area_and_exchange()`
>
>`print (blob)`

 You can create your own Python file by any of the following methods:
 
 1.	Create a single file that contains all of the Controllers and methods, then commenting out the lines for each method you don't want to run.
 
 2.	Create a unique file for each Controller, adding only those lines relevant to that Controller and related methods, and then commenting out the lines for each method you're not using. You would create three unique Controller files.
 
 3.	Create a unique file for each method. Each file will then contain the lines instantiating the relevant Controller.

This SDK describes the second option. However, whichever option you select, the file(s) should be saved in the **flowroute-numbers-python** directory. When you want to run a method using a file, run the following on the command line in the **flowroute-numbers-python** directory:

		python <Python File Name.py>

## Use demo.py<a name=usedemo></a>

A demo Python file, **demo.py**, is included with the installed libraries. This file contains a list of the methods and parameters.  You can use this file to run with your API credentials and retrieve information.

To use **demo.py**, open the file with a code text editor, such as *Sublime Text*, and modify parameters if needed or comment out lines. Whether or not you add any parameters or comment out lines, the file can be run as-is by running the following on the command line at the top-level **flowroute-numbers-python** directory:

	python demo.py

For creating your own file or for more information on the parameters within the methods, see [Controllers](#controllers) for more information:
	
##Controllers<a name=controllers></a>

flowroute-numbers-python supports the following Controllers:

*	[`PurchasablePhoneNumbersController`](#purchasecontroller)

* 	[`TelephoneNumbersController`](#telephonecontroller) 

*  [`InboundRoutesController`](#inboundcontroller)

>**Important:** The SDK displays sample responses. Formatting of the responses is provided for clarity only. They are not intended to show the formatting of your own response. 

###PurchasablePhoneNumbersController<a name=purchasecontroller></a>

The PurchasablePhoneNumbers Controller contains all of the methods necessary to search through Flowroute's phone number inventory. Methods must be added to a PHP file and that file run from a command line. For example, you can create a **purchase.py** file contains the following information:

		from FlowrouteNumbersLib.Controllers.PurchasablePhoneNumbersController import *
		from FlowrouteNumbersLib.Models import *
		
		Configuration.username="Access Key"
		Configuration.password="Secret Key"
		
		pnc = PurchasablePhoneNumbersController()
		
		# List NPAs
		response = pnc.list_available_np_as(limit=None)
		print (response)
		
		#List NPA and NXX
		response = pnc.list_area_and_exchange(limit=None,npa=None,page=None)
		print (response)		
		
		#Search
		response = pnc.search(limit=None,npa=None,nxx=None,page=None,ratecenter='None',state='None',tn=None)
		print (response)
		
PurchasePhoneNumbersController methods are added after `pnc = PurchasablePhoneNumbersController()`. If you do not want to execute a specific method, comment those lines out with `#`. 

*	[`list_available_np_as`](#listnpas)

* 	[`list_area_and_exchange`](#listnpanxx)

*  [`search`](#search)

In a terminal window, run the file from the **flowroute-numbers-python** directory. For example:

	python purchase.py

#### `list_available_np_as(limit)`<a name=listnpas></a>

The `list_available_np_as()` method retrieves a list of every NPA (area code) available in Flowroute's phone number inventory.

#####Usage

	response = pnc.list_available_np_as(limit=None)
	print (response)

The method takes the following parameter:

| Parameter | Required |  Type| Usage                              |
|-----------|----------|--------|-------------------------------|
| `limit`  | True    | Integer| Defines controls the number of items returned. The maximum number of items is 200. If the field is left blank `()` all NPAs are returned. If `(limit=None)`, then 10 NPAs are returned by default.|

##### Example Usage
The following example passes `2` as the number of items to return. 

	response = pnc.list_available_np_as(limit=2)
	print (response)

#####Example response

Results are returned in numerical order, starting with the lowest NPA number.

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
|No error code.  |Response Not OK|This error is most commonly returned when the number passed in the method is greater than the allowed maximum of `200`.|
|`500`  |Application Error|This error is most commonly returned when `0` is passed for the `limit`.|

####`list_area_and_exchange(limit,npa,page)`<a name=listnpanxx></a>

The `list_area_and_exchange()` method retrieves a list of every NPA-NXX (area code and exchange) available in Flowroute's phone number inventory.

#####Usage

	response = pnc.list_area_and_exchange(limit=None,npa=None,page=None)
	print (response)

The method takes the following parameters:

| Parameter | Required |  Type |Usage                                                         |
|-----------|----------|--------|-------------------------------------------------------|
| `limit`     | False    | integer |Controls the number of items returned. This can be a maximum of `200`. If no limit is passed,  `10` results are returned as the default. These results are organized numerically by the combination of NPA and NXX. For example, *`206258`* is NPA *`206`* and NXX *`258`*.                   |
| `npa`       | False    |  integer |Limits results to the specified NPA (area code). Partial search is supported. For example, passing `20` for the value returns all NPAs that include `20`.|
| `page`      | False    |  integer |Sets which page of the results is returned in the output. When set, `prev` and `next` page links appear in the response.|       

##### Example Usage

The following example sets `2` for the `limit`, `206` for the `npa`, and to display `page` `2` in the output:

	response = pnc.list_area_and_exchange(limit=2,npa=106,page=2)
	print (response)

#####Example response

Results are returned in numerical order, starting with the lowest NPA number. The `npaxxs` variable is formatted as a combination of the area code and exchange. In the following example, `206258` is the combination of area code `206` and exchange `258`. 

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
|No error code.  |Response Not OK|This error is most commonly returned when the number passed for the limit is greater than the allowed maximum of 200.|
|`500`  |Application Error|This error is most commonly returned when `0` is passed for the `limit`.|

####`search(limit,npa,nxx,page,ratecenter,state,tn)`<a name=search></a>

The `search()` method is the most robust option for searching through Flowroute's purchasable phone number inventory. It allows you to search by NPA, NXX, Ratecenter, State, and/or TN (telephone number). 

##### Usage

	response = pnc.search(limit=None,npa=None,nxx=None,page=None,ratecenter='None',state='None',tn=None)
	print (response)

The method takes the following parameters:

| Parameter  | Required    |                   | Usage                                                                     
|------------|-------------|------------------|--------------------------------------------------------------|
| `limit`      | False     |integer | Controls the number of items returned. This can be a maximum of 200. If neither a number nor `None` are passed, a maximum of 10 NPANXXs are returned as a default, organized numerically by the combination of NPA and NXX. For example, *`206258`* is NPA *`206`* and NXX *`258`*.   |
| `npa`        | False, unless *`nxx`* is present| integer   | Limits results to the specified three-digit NPA (area code). Partial numbers are not supported.      |
| `nxx`        | False| integer |Limits the results to the specified three-digit NXX (exchange). Partial numbers are not supported.    |
| `page`       | False    | integer |Sets which page of the results is returned in the output. When set, `prev` and `next` page links appear in the response.|
| `ratecenter` | False   | string |Limits results to the specified *`ratecenter`*. This field is case-insensitive. If replacing `None` with a ratecenter, enclose the ratecenter name in single quotes (`''`)|                              
| `state`      | False, unless *`ratecenter`* is passed.|string | Limits results to the specified two-character state or territory code. This field is case-insensitive. If replacing `None` with a state, enclose the state name in single quotes (`''`)|    
| `tn`         | False       | string |Limits results to the specified telephone number. This field uses partial match search. For example, if *`206`* is passed, all results that include *`206`* are returned. |

##### Example Usage

		response = pnc.search(limit=1,npa=206,nxx=743,page=1,ratecenter='seattle',state='wa',tn=None)
		print (response)

#####Example response

The following results are returned based on the search parameters:

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
| `tns`  | Object composed of *`telephonenumber`*, `state`, `ratecenter`, and `billing_methods`.|                           |
||	*`telephone number`*- The retrieved telephone number object, which is composed of:|
||	<ul><ul><li> `initial_cost`- The one-time fixed cost for that telephone number. The default value is USD `1.00`.</ul>|
| | <ul><ul><li>`monthly_cost`- The recurring monthly cost to maintain that telephone number. The default value is USD `1.25`.</ul>|
||	`state`- The US State or Canadian province/territory in which the NPA NXX is located.|
||	`ratecenter`- The ratecenter associated with the NPA NXX.</ol>|
||	`billing_methods`- Displays the billing methods available for the telephone number: <ul><li>`VPRI`, or</ul></li> <ul><li>`METERED` </ul></li> |
	
##TelephoneNumbersController<a name=telephonecontroller></a>

The Telephone Numbers Controller contains all of the methods necessary to purchase a new phone number and to manage your owned phone number inventory. Methods must be added to a PHP file and that file run from a command line. For example, you can create a **numbers.py** file that contains the following base information:

	from FlowrouteNumbersLib.Controllers.TelephoneNumbersController import *
	from FlowrouteNumbersLib.Models import *  
	
	Configuration.username="Access Key"
	Configuration.password="Secret Key"
	
	tnc = TelephoneNumbersController()
	
	#Purchase a Number
	billing = BillingMethod(billing_method="VPRI" or "METERED")
 	number = "telephone number"
 	response = tnc.purchase`*`(billing,number)
 	print (response)
 	
 	#List Account Telephone Numbers
 	response = tnc.list_account_telephone_numbers(limit=None,page=None,pattern=None)
 	print (response)
 	
 	#Telephone Number Details
 	response = tnc.telephone_number_details(number)
 	print (response)
 	
 	#Update Telephone Number Routes
 	route variable name = [Route(name='primary route'), Route(name='failover route')] 
 	response = tnc.update(number=phoneNumber, routes=route variable name)
 	print (response)

TelephoneNumbersController methods are added after `tnc = TelephoneNumbersController()`. 

The Controller supports the following methods:

*	[`purchase`](#purchasenumber)
* 	[`list_account_telephone_numbers`](#listnumbers)
*  [`telephone_number_details`](#numberdetails)
*  [`update`](#updateroute)

In a terminal window, run the file from the **flowroute-numbers-python** directory. For example:

	python numbers.py

#### `purchase(billing,number)`<a name=purchasenumber></a>

The purchase method is used to purchase a telephone number from Flowroute's inventory.

##### Usage

 *`billing`*` = BillingMethod(billing_method="VPRI" or "METERED")`</br>
 *`number`*`=`*`"telephone number"`* </br>
 `response = tnc.purchase`*`(billing,number)`*
 print (response)

The method takes the following parameters:

| Parameter       | Required | Data type|Usage                                                                |
|-----------------|----------|---------|-----------------------------------------------------------------------|
| *`billing`*    | True  | string   | Variable that sets the billing the BillingMethod. The variable is then associated with one of two billing methods, `VPRI` or `METERED`. <ul><li>`VPRI` are concurrent calls limited to the number of VPRI channels you have, but with unlimited usage on each channel.<li> `METERED` are unlimited concurrent calls, billed per-minute.</li>For this example, the variable is named *`billing`*.|
| *`number`* | True     | string |Variable that sets the phone number to purchase. Must be from the list of available Flowroute telephone numbers and must be formatted using an E.164, 11-digit `1NPANXXXXXXXXX` format.</ul></br> For this example, the variable is named*`number`*.|                               |
	
##### Example Usage

	billing = BillingMethod(billing_method="VPRI")
	number = "15852003968"
	response = tnc.purchase(billing,number)
	print (response)

##### Example response

For a successful purchase, an empty string (`''`) is returned

#####Error response
The following error can be returned:

| Error code | Message  | Description                                                 |
|------------|----------|-------------------------------------------------------|
|No error code.  |HTTP Response Not OK|The phone number to purchase might be incorrect.|

#### `list_account_telephone_numbers(limit,page,pattern)`<a name=listnumbers></a>

The `list_account_telephone_numbers` method is used to retrieve a list of all of the phone numbers on your Flowroute account.

#####Usage

	response = tnc.list_account_telephone_numbers(limit=None,page=None,pattern=None)
	print (response)

The method takes the following parameters:

| Parameter | Required | Data type|Usage                                                     |
|-----------|----------|---------|--------------------------------------------------|
| `limit`  | True    | integer | Controls the number of items returned. This can be a maximum of 200. If neither a number nor `None` are passed, a maximum of 10 numbers are returned as a default.  |
| `page`      | False    | integer |If multiple pages of numbers are returned, this field displays the results from the set page.     |
| `pattern`   | False    | integer |The telephone number on which to search. Partial search is supported; if any part of a telephone number is passed, the pattern will return *all* telephone numbers that include that pattern. |

##### Example Usage
	
	response = tnc.list_account_telephone_numbers(limit=5,page=2,pattern=206)
	print (response)

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
   	   "detail": "/v1/tns/16476998778"
   	 }
  	}
	}
#####Response fields
The following fields are returned in the response:

|Parameter | Description                                             |
|--------|-------------------------------------------------------|
| `tns`  | The telephone number retrieved from the request; it is composed of the following *`telephonenumber`* object.|                           |
|| <ul><li>*`telephone number`*- The telephone number you own. This object is further composed of `routes`:|
| |<ul><ul><li>`routes`- Defines the parameters of the route. Composed of the following:</ul>
| |	<ul><ul><ul><li>`type`- Indicates the type of route: `HOST`, `PSTN`, or `URI`. If no route is assigned, `SIP-REG` is the default name assigned to the route.
| |<ul> <ul><ul><li>`name`- Name of the route. If no `name` was given to the route, `sip-reg` is the assigned default name.</ul>
||<ul><li>`billing_method`- Either `VPRI` or `METERED`.
||<ul><li>`detail`- Provides more detail that can be passed when using the `telephone_number_details` method below. </ul>|

#####Error response
The following error can be returned:

| Error code | Message  | Description                                                 |
|------------|----------|-------------------------------------------------------|
|  No error code. |`{}`|The telephone number passed in the method does not contain the correct number of digits. It must use an E.164 11-digit, `1NPANXXXXXX` format.

	
#### `telephone_number_details(telephone_number)`<a name=numberdetails></a>

The `telephone_number_details` method is used to retrieve the billing method, primary route, and failover route for the specified telephone number. 

#####Usage

	response = tnc.telephone_number_details(number)
	print (response)

The method takes the following parameter:

| Parameter       | Required|Data type | Usage                                             |
|-----------------|----------|--------|-------------------------------------------|
| `number` | True  | string   | The telephone number on which to query. This must be a Flowroute number on your account, and must use an E.164 1NPANXXXXXX format. |

##### Example Usage

	response = tnc.telephone_number_details(16476998778)
	print (response)
	
#####Example response
	{
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
	  "billing_method": "METERED"
	}
##### Response fields

|Parameter | Description                                         |
|--------|-------------------------------------------------------|
| `routes`  | The routes associated with the telephone number; it is composed of the following:
| |	<ul><li>`type`- Indicates the type of route: `HOST`, `PSTN`, `URI`, or `SIP-REG`. `SIP-REG` is the default name assigned to the route if none is assigned. A route `type` can be created using the [`create_new_route`](#createroute) endpoint.</li>
| |<ul> <li>`name`- Name of the route. If no `name` was given to the route, `sip-reg` is the assigned default name. A `name` is assigned to a route when the route is created.</ul></li>
|`billing_method`| Either `VPRI` or `METERED`.|

#####Error response
The following error can be returned:

| Error code | Message  | Description                                           |
|------------|----------|-------------------------------------------------------|
|No error code.  |`{}`|An incorrect number of digits was passed for the telephone number. The number must use E.164, 11-digit `1NPANXXXXXX` format.|

#### `update(self,number,routes)`<a name="updateroute"></a>

The `update` method is used to update both the primary and failover route for a phone number, specified within an array. See **Example usage** below. The first route name within the array is assigned as the primary route; the second route listed in the array will be the failover route in the event the first route is unavailable. The list of available route names can be retrieved by using the [`list`](#listroutes) endpoint.

#####Usage

	route variable name = [Route(name='primary route'), Route(name='failover route')]
	response = tnc.update(number=phoneNumber, routes=route variable name)
	print (response)

The method takes the following parameters:

| Parameter       | Required | Data type| Usage                                                                  |
|-----------------|----------|----------|-------------------------------------------------|
|`route variable name`|True| string| The variable name identifying the array. This field supports an unlimited number of characters. For this example, *`rtes`* is the variable name. This variable name is also passed in the following `response` line.
|`name='route name'`|True| string| Name of an existing route. The first `name` in the array is assigned as the primary route; the second `name` in the array is assigned as the secondary, or failover, route. See [`create_new_route`](#createroute) for the steps to create a route. This field supports an unlimited number of characters.
| `phoneNumber` | True   | string  | The phone number for which to update routes. This must be a Flowroute phone number, and must use an E.164 1NPANXXXXXX format.          |

##### Example usage
	
	rtes = [Route(name='sip-reg'), Route(name='ea4f4056663e27b082999689982e4723')]
	response = tnc.update(number=16476998778, routes=rtes)
	print (response)

### InboundRoutesController<a name=inboundcontroller></a>

The InboundRoutesController contains the methods required to create new routes and to view your current routes. Methods must be added to a PHP file and that file run from a command line. For example, you can create a **routes.py** file that contains the following information:

	from FlowrouteNumbersLib.Controllers.InboundRoutesController import *
	from FlowrouteNumbersLib.Models import *  
	
	Configuration.username="Access Key"
	Configuration.password="Secret Key"
	
	irc = InboundRoutesController()
	
	#List Routes
	response = irc.list(limit=None, page=None)
	print (response)
		 	
 	#Create a New Route
 	response = irc.create_new_route(route_name='name',mtype='route type',value='type value')
 	print (response)
 	
	print (response)

TelephoneNumbersController methods are added after `irc = InboundRoutesController()`. 

The Controller supports the following methods:

*	[`list`](#listroutes)
*  [`create_new_route`](#createroute)

In a terminal window, run the file from the **flowroute-numbers-python** directory. For example:

	python routes.py

#### `list(limit,page)`<a name"listroutes"></a>

The `list` method is used to return all of the existing inbound routes from your Flowroute account. From the list, you can retrieve the names and types of routes when applying a route to a phone number or updating an existing route on a phone number.

##### Usage

	response = irc.list(limit=None, page=None)
	print (response)

The method takes the following parameters:

| Parameter | Required| Data type | Usage                                            |
|-----------|----------|----------|----------------------------------------|
| `limit`     | False  | string  | Sets the number of items returned. The maximum number is `200`. If no limit is set, `10` is used as a default. |
| `page`      | False  | string  | Sets which page of the results is returned. For example, if this parameter is set to `1`, page 1 of the results is returned when run. |

##### Example Usage

	response = irc.list(limit=4, page=None)
	print (response)

#####Example response
	
	{
	routes:
     {
       HOSTroute1:
            {
                type: HOST
                value => 24.239.23.40:5060
            }
       PSTNroute1:
            {
                type: PSTN
                value: 178
            }
        URIroute1:
            {
                type: URI
                value: sip:16476998778@215.122.69.152:5060
            }
        sip-reg:
            {
                type: SIP-REG
                value: sip-reg
            }
     }
	}

#####Error response
| Error code | Message  | Description                                                 |
|------------|----------|-------------------------------------------------------|
|No error code.  |HTTP Response Not OK|One or more of the parameters is outside the range of supported values.|	
	
#### `create_new_route(route_name,mtype,value)`<a name="createroute"></a>

The `create_new_route` method is used to create a new inbound route. An inbound route can then be assigned as either a primary or failover route for a phone number. See [`update`](#updateroute) for the steps to update primary and failover routes.

#####Usage

	response = irc.create_new_route(route_name='name',mtype='route type',value='type value')
	print (response)

The method takes the following parameters:

| Parameter | Required | Data type |Description                                                                                   |
|-----------|----------|------------|---------------------------------------------------|
| `name` | True  |string   | The name of the new route. This field supports an unlimited number of alphanumeric characters.  |
| `route type`      | True   | string | The type of route. Valid options are `HOST`, `PSTN`, and `URI` |
| `type value`     | True    | string | Value of the route, dependent on the `type`: <ul><li>If `HOST`, the value must be an IP address or URL with an optional port number—for example, an IP address could be `24.239.23.40:5060` or a URL could be `myphone.com`. If no port is specified, the server will attempt to use DNS SRV records. <li>If `PSTN`, the value must be formatted as a valid E.164, 11-digit formatted North American phone number—for example,`16476998778`. <li>If `URI`, the value must be formatted as  `protocol:user@domain[:port][;transport=<tcp/udp>`—for example, `sip:alice@atlanta.com`,  `sip:16476998778@215.122.69.152:5060;transport=tcp`, or `sips:securecall@securedserver.com`.</li></ul>|                                        

You can create as many route types as you want, but each must have a unique `name`.

##### Example Usage

The following example shows the creation of three new routes:

	response = irc.create_new_route(route_name='PSTNroute1',mtype='PSTN',value='16476998778')
	print (response)
	response = irc.create_new_route(route_name='HOSTroute1',mtype='HOST',value='24.239.23.40:5060')
	print (response)
	response = irc.create_new_route(route_name='URIroute1',mtype='URI',value='sip:16476998778@215.122.69.152:5060')
	print (response)
	
#####Example response

An empty string (`''`) is returned for each successfully created route; no other code or message is returned. An error encountered for a specific `irc.create_new_route()` line will not prevent the other routes from being created.
 
	irc.create_new_route(route_name='PSTNroute1',mtype='PSTN',value='16476998778')
	''
	irc.create_new_route(route_name='HOSTroute1',mtype='HOST',value='24.239.23.40:5060')
	''
	irc.create_new_route(route_name='URIroute1',mtype='URI',value='sip:16476998778@215.122.69.152:5060')
	''

#####Error response
The following errors can be returned:

| Error code | Message  | Description                                           |
|------------|----------|-------------------------------------------------------|
|Bad request  |`{}`|Typically this occurs when an incorrect number of digits was passed for the telephone number. The number must use E.164, 11-digit `1NPANXXXXXXXXX` format.|
|No error code|HTTP Response Not OK|Typically this occurs when a `value` is malformed. |