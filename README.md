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

### Get a code text editor

Steps in this SDK describe creating one or more script files that allow you to execute the methods. Script files can be created either using a terminal window shell or through using a code text editor. For example, *Sublime Text*. 

## Install the required libraries

The SDK uses the **Unirest** and **jsonpickle** Python libraries, which must be installed before you can use the SDK. 

> **Important:** The SDK supports only Python 2.x. Python 1.x and 3.x are not supported.

1. Open a terminal session. 

2. If needed, create a parent directory folder where you want to install the SDK.
 
3. Go to the newly created folder, and run the following:

 	`git clone https://github.com/flowroute/flowroute-numbering-python.git`
 	
 	The `git clone` command clones the **flowroute-numbering-python** repository as a sub directory within the parent folder.
 	
4.	Change directories to the newly created **flowroute-numbering-python** directory.

5.	Run the following:

	`pip install -r requirements.txt`

6.	Create a script to import the SDK.

## Create a Python file to import the Controllers and Models<a name=create></a>

The following describes importing the SDK and setting up your API credentials. Importing the SDK allows you to instantiate the [Controllers](#controllers), which contain the methods used to perform tasks with the SDK. In order to do this, you will need to create and run a Python file. You can create the file either through using a terminal shell or through a code text editor. The sample files in this SDK were created using a code text editor. In the following example, all Controllers are instantiated using a single file:

1.	Using a code text editor, create a new file.

2.	At the top of the file, add the lines that import the Controllers:

		from FlowrouteNumbersLib.Controllers.InboundRoutesController import *
		from FlowrouteNumbersLib.Controllers.PurchasablePhoneNumbersController import *
		from FlowrouteNumbersLib.Controllers.TelephoneNumbersController import *
		from FlowrouteNumbersLib.Models import *

3.	Next, add the lines which pass your credentials to the Controllers:

		Configuration.username="Access Key"
		Configuration.password="Secret Key"
		
4.	Replace `Access Key` and `Secret Key` with your own Access Key and Secret Key.

	>**Important:** Verify that your Access Key and Secret Key are correct when adding them to the file. An incorrect Key will throw an `HTTP Response Not OK` message when invoking a method.

5.	Add the following lines to instantiate the Controllers for use:

		pnc = PurchasablePhoneNumbersController()
		tnc = TelephoneNumbersController()
		irc = InboundRoutesController()

6.	Optionally, add a line that prints out a response after invoking a method, allowing you to see a response in the terminal window for invoked method.

		print (response)

	>**Important:** Throughout this SDK, `response` is used in method examples. `response` is a variable name that can be changed to a name of your own choosing. It can support an unlimited number of characters. If you choose to rename `response`, make sure that any method that references that variable name is also changed to use the new name. In the following example, `response` is changed to `blob` wherever `response` is used:
>
>`#List NPA and NXX`<br>
>`blob = pnc.list_area_and_exchange()`<br>
>`print (blob)`

7.	Save the Python file in your top-level **flowroute-numbers-python** directory with a .py extension. For example, *mycontrollers.py*.

8.	Add Controller methods as needed. See [Controllers](#controllers).

###Example Python file

The following shows an example of a single Python file that imports and instantiates all three Controllers:
	
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
	
	
With this in mind, you can then decide the approach you want to take towards creating a file. You can create your own Python file using any of the following processes:
 
 1.	Create a single file that contains all of the Controllers and methods, then commenting out the lines for each method you don't want to invoke.
 
 2.	Create a unique file for each Controller, adding only those lines relevant to that Controller and related methods, and then commenting out the lines for each method you're not invoking. This process creates three unique Controller files.
 
 3.	Create a unique file for each method. Each file will then contain the only the lines for the relevant Controller and method.

This SDK describes the second option. However, whichever option you select, the file(s) should be saved in the **flowroute-numbers-python** directory. When you want to invoke a method using a Python file, in a terminal window run the following on the command line from the **flowroute-numbers-python** directory:

		python <Python File Name.py>

## Use demo.py<a name=usedemo></a>

A demo Python file, **demo.py**, is included with the installed libraries. This file contains a list of the methods and parameters.  You can use this file with your API credentials to instantiate all Controllers and invoke all methods.

To use **demo.py**, open the file with a code text editor, such as *Sublime Text*, and modify parameters if needed or comment out lines. Whether or not you add any parameters or comment out lines, the file can be run as-is by running the following on the command line at the top-level **flowroute-numbers-python** directory:

	python demo.py

##Controllers<a name=controllers></a>

The following sections describe **flowroute-numbers-python** Controllers:

*	[`PurchasablePhoneNumbersController`](#purchasecontroller)

* 	[`TelephoneNumbersController`](#telephonecontroller) 

*  [`InboundRoutesController`](#inboundcontroller)

>**Important:** The SDK displays sample responses. Formatting of the responses is provided for clarity only. They are not intended to show the formatting of your own response. 

###PurchasablePhoneNumbersController<a name=purchasecontroller></a> 

Location: **./flowroute-numbers-python/FlowrouteNumbersLib/Controllers**

The PurchasablePhoneNumbers Controller contains all of the methods necessary to search through Flowroute's phone number inventory. The following shows a sample file named **purchase.py** file, which invokes only that Controller's methods:

		from FlowrouteNumbersLib.Controllers.PurchasablePhoneNumbersController import *
		from FlowrouteNumbersLib.Models import *
		
		Configuration.username="Access Key"
		Configuration.password="Secret Key"
		
		pnc = PurchasablePhoneNumbersController()
		
		#List Available NPAs
		response = pnc.list_available_np_as(limit=None)
		
		#List NPA and NXX
		response = pnc.list_area_and_exchange(limit=None,npa=None,page=None)
	
		#Search
		response = pnc.search(limit=None,npa=None,nxx=None,page=None,ratecenter='None',state='None',tn=None)
		
		print (response)

When creating your own Python file, add each method after `pnc = PurchasablePhoneNumbersController()`, but before `print (response)`. If you do not want to invoke a specific method, comment out that method's lines with `#`.  

The Controller contains the following methods:

*	[`list_available_np_as`](#listnpas)

* 	[`list_area_and_exchange`](#listnpanxx)

*  [`search`](#search)

#### `list_available_np_as(limit)`<a name=listnpas></a>

The `list_available_np_as()` method retrieves a list of every NPA (area code) available in Flowroute's phone number inventory.

#####Usage

Add the following lines to your Python file:

	#List Available NPAs
	response = pnc.list_available_np_as(limit=None)

The method takes the following parameter:

| Parameter | Required |  Type| Usage                              |
|-----------|----------|--------|-------------------------------|
| `limit`  | True    | Integer| Defines controls the number of items returned. The maximum number of items is 200. If the field is left blank, `()`, all NPAs are returned. If `(limit=None)`, then ten NPAs are returned by default.|

##### Example Usage

The following example limits the number of NPAs returned to `2`: 

	#List Available NPAs
	response = pnc.list_available_np_as(limit=2)

##### Example response

Results are returned in numerical order, starting with the lowest number NPA.

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
##### Error response

| Error code | Message  | Description                                                 |
|------------|----------|-------------------------------------------------------|
|No error code|HTTP Response Not OK|Typically this occurs when a `limit` does not fall within the allowed range of `1` to `200`, or if a negative number was passed. |
|`500`  |Application Error|This error is most commonly returned when `0` is passed for the `limit`.|

####`list_area_and_exchange(limit,npa,page)`<a name=listnpanxx></a>

The `list_area_and_exchange()` method retrieves a list of every NPANXX (area code and exchange) available in Flowroute's phone number inventory.

##### Usage

Add the following lines to your Python file:

	#List NPA and NXX
	response = pnc.list_area_and_exchange(limit=None,npa=None,page=None)

The method takes the following parameters:

| Parameter | Required |  Type |Usage                                                         |
|-----------|----------|--------|-------------------------------------------------------|
| `limit`     | False    | integer |Controls the number of items returned. This can be a maximum of `200`. If no limit is passed,  `10` results are returned as the default. These results are organized numerically by the combination of NPA and NXX. For example, *`206258`* is NPA *`206`* and NXX *`258`*.                   |
| `npa`       | False    |  integer |Limits results to the specified NPA (area code). Partial search is supported. For example, passing `20` for the value returns all NPAs that include `20`.|
| `page`      | False    |  integer |Sets which page of the results is returned in the output. When set, `prev` and `next` page links appear in the response.|       

##### Example Usage

The following example sets the `limit` the results to `2`, the `npa` to `206`, and to display `page` `2`:

	#List NPA and NXX
	response = pnc.list_area_and_exchange(limit=2,npa=106,page=2)

##### Example response

Results are returned in numerical order, starting with the lowest NPA number. The `npaxxs` parameter variable is formatted as a combination of the NPA and NXX. In the following example, `206258` is the combination of NPA `206` and NXX `258`. 

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

>**Note:** If no results are found based on the passed parameters, `{}` is returned as a response.

##### Error response

| Error code | Message  | Description                                                 |
|------------|----------|-------------------------------------------------------|
|No error code|HTTP Response Not OK|Typically this occurs when a `limit` does not fall within the allowed range, of `1` to `200` or a negative number; or if `0` or a negative number are passed for the `page`. |
|`500`  |Application Error|This error is most commonly returned when `0` is passed for the `limit`.|

####`search(limit,npa,nxx,page,ratecenter,state,tn)`<a name=search></a>

The `search()` method is the most robust option for searching through Flowroute's purchasable phone number inventory. It allows you to search by NPA, NXX, Ratecenter, State, and/or TN (telephone number). 

##### Usage

Add the following lines to your Python file:

	#Search
	response = pnc.search(limit=None,npa=None,nxx=None,page=None,ratecenter='None',state='None',tn=None)

The method takes the following parameters:

| Parameter  | Required    |                   | Usage                                                                     
|------------|-------------|------------------|--------------------------------------------------------------|
| `limit`      | False     |integer | Controls the number of items returned. This can be a maximum of 200. If neither a number nor `None` are passed, a maximum of 10 NPANXXs are returned as a default, organized numerically by the combination of NPA and NXX. For example, *`206258`* is NPA *`206`* and NXX *`258`*.   |
| `npa`        | False, unless *`nxx`* is present| integer   | Limits results to the specified three-digit NPA (area code). Partial numbers are not supported.      |
| `nxx`        | False| integer |Limits the results to the specified three-digit NXX (exchange). Partial numbers are not supported.    |
| `page`       | False    | integer |Sets which page of the results is returned in the output. When set, `prev` and `next` page links appear in the response.|
| `ratecenter` | False   | string |Limits results to the specified *`ratecenter`*. This field is case-insensitive. If replacing `None` with a ratecenter, enclose the ratecenter name in single quotes (`''`).|                              
| `state`      | False, unless *`ratecenter`* is passed.|string | Limits results to the specified two-character state or territory code. This field is case-insensitive. If replacing `None` with a state, enclose the state name in single quotes (`''`).|    
| `tn`         | False       | string |Limits results to the specified telephone number. This field uses partial match search. For example, if *`206`* is passed, all results that include *`206`* are returned. |

##### Example Usage

In the following example, a search request sets the `limit` to `1`, the `npa` to `206`, the `nxx` to `743`, to `display` page `2`, the `ratecenter` to `"seattle"`, the `state` to `"wa"`, and the `tn` to `None`.

		#Search
		response = pnc.search(limit=1,npa=206,nxx=743,page=1,ratecenter='seattle',state='wa',tn=None)

##### Example response

Based on the parameters passed above, the following result is returned:

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
	
>**Note:** If no results are found based on the passed parameters, `{}` is returned as a response.

##### Response field descriptions

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

##### Error response

| Error code | Message  | Description                                           |
|------------|----------|-------------------------------------------------------|
|No error code|HTTP Response Not OK|Typically this occurs when a passed value does not fall within the range of allowed values. For example, this might be a `limit` that does not fall within the `1` to `200` range. |
	
##TelephoneNumbersController<a name=telephonecontroller></a> 

Location: **./flowroute-numbers-python/FlowrouteNumbersLib/Controllers**

The TelephoneNumbersController supports all of the methods necessary to purchase a new phone number and to manage your owned phone number inventory. The following shows a sample file named **phonenumbers.py** file that invokes only the TelephoneNumbersController methods:

	from FlowrouteNumbersLib.Controllers.TelephoneNumbersController import *
	from FlowrouteNumbersLib.Models import *  
	
	Configuration.username="Access Key"
	Configuration.password="Secret Key"
	
	tnc = TelephoneNumbersController()
	
	#Purchase a Number
	billing = BillingMethod(billing_method="VPRI" or "METERED")
 	number = "telephone number"
 	response = tnc.purchase`*`(billing,number)
  	
 	#List Account Telephone Numbers
 	response = tnc.list_account_telephone_numbers(limit=None,page=None,pattern=None)
 	
 	#Telephone Number Details
 	response = tnc.telephone_number_details(number)
 	
 	#Update Telephone Number Routes
 	route variable name = [Route(name='primary route'), Route(name='failover route')] 
 	response = tnc.update(number=phoneNumber, routes=route variable name)

 	print (response)

Add any of the following TelephoneNumbersController methods after `tnc = TelephoneNumbersController()`, but before `print (response)`. If you do not want to execute a specific method, comment out that method's lines with `#`.

The Controller contains the following methods:

*	[`purchase`](#purchasenumber)
* 	[`list_account_telephone_numbers`](#listnumbers)
*  [`telephone_number_details`](#numberdetails)
*  [`update`](#updateroute)

#### `purchase(billing,number)`<a name=purchasenumber></a>

The `purchase` method is used to purchase a telephone number from Flowroute's inventory.

##### Usage

Add the following lines to your Python file:

	#Purchase a Telephone Number
 	billing = BillingMethod(billing_method="")
 	number = "telephone number"
 	response = tnc.purchase(billing,number)

First, define the variable names used in the method: 

|Variable name    |Required  |Type      |Description|
|-----------------|----------|----------|-------------------------------------------------------| 
|`billing`      | True     | string   |The variable name assigned to the billing method. An unlimited number of characters can be used. For this example, `billing` is the name of the variable. |
|`number`        | True     | string   | This variable identifies the phone number to purchase. An unlimited number of characters can be used. For this example, `number` is the name of the variable.|

Next, define the `billing` and `number` variables themselves:

| Parameter       | Required | Data type|Usage                                                                |
|-----------------|----------|---------|-----------------------------------------------------------------------|
| `billing_method("")`   | True  | string   | Sets the billing method for the purchased telephone number. It must be one of the following: `VPRI` or `METERED`. <ul><li>`VPRI` are concurrent calls limited to the number of VPRI channels you have, but with unlimited usage on each channel.<li> `METERED` are unlimited concurrent calls, billed per-minute.</ul>The variable name can be of as many characters as you want, but the name you choose must be used consistently throughout this method. For this example, the variable is named `billing`. |                           
| `telephone number`|true| string |Phone number associated with the `number` variable. This number must be from the list of available Flowroute telephone numbers and must be formatted using an E.164, 11-digit `1NPANXXXXXXXXX` format.|
	
##### Example Usage

	#Purchase a Telephone Number
	billing = BillingMethod(billing_method="VPRI")
	number = "15852003968"
	response = tnc.purchase(billing,number)

##### Example response

For a successful purchase, an empty line is returned. No other success message is displayed.

##### Error response

| Error code | Message  | Description                                                 |
|------------|----------|-------------------------------------------------------|
|No error code.  |HTTP Response Not OK|The phone number to purchase might already have been purchased, or the number might have been entered incorrectly.|

#### `list_account_telephone_numbers(limit,page,pattern)`<a name=listnumbers></a>

The `list_account_telephone_numbers` method is used to retrieve a list of all of the phone numbers on your Flowroute account.

##### Usage

Add the following lines to your Python file:

	#List Account Telephone Numbers
	response = tnc.list_account_telephone_numbers(limit=None,page=None,pattern=None)

The method takes the following parameters:

| Parameter | Required | Data type|Usage                                                     |
|-----------|----------|---------|--------------------------------------------------|
| `limit`  | True    | integer | Controls the number of items returned. This can be a maximum of 200. If neither a number nor `None` are passed, a maximum of 10 numbers are returned as a default.  |
| `page`      | False    | integer |If multiple pages of numbers are returned, this field displays the results from the set page.     |
| `pattern`   | False    | integer |The telephone number on which to search. Partial search is supported; if any part of a telephone number is passed, the pattern will return *all* telephone numbers that include that pattern. |

##### Example Usage
	
	#List Account Telephone Numbers
	response = tnc.list_account_telephone_numbers(limit=5,page=2,pattern=206)

##### Example response
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
	
>**Note:** If no results are found based on the passed parameters, `{}` is returned as a response.
	
##### Response fields
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

##### Error response

| Error code | Message  | Description                                           |
|------------|----------|-------------------------------------------------------|
|No error code|HTTP Response Not OK|Typically this occurs when a passed `limit` does not fall within the range of allowed values of `1` to `200`. |

	
#### `telephone_number_details(telephone_number)`<a name=numberdetails></a>

The `telephone_number_details` method is used to retrieve the billing method, primary route, and failover route for the specified telephone number. 

##### Usage

Add the following lines to your Python file:

	#Telephone Number Details
	response = tnc.telephone_number_details(number)

The method takes the following parameter:

| Parameter       | Required|Data type | Description                              |
|-----------------|----------|--------|-------------------------------------------|
| `number` | True  | string   | The telephone number on which to query. This must be a Flowroute number on your account, and must use an E.164 1NPANXXXXXX format. |

##### Example Usage

In the following example, details are requested for the telephone number just purchased using the [`purchase`](#purchasenumber) method.

	"Telephone Number Details
	response = tnc.telephone_number_details(16476998778)
	
##### Example response
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

##### Error response

| Error code | Message  | Description                                           |
|------------|----------|-------------------------------------------------------|
|No error code.  | HTTP Response Not OK|An incorrect number of digits was passed for the telephone number, or the number passed in the method is not one of your Flowroute numbers. The number must use E.164, 11-digit `1NPANXXXXXX` format.|

#### `update(self,number,routes)`<a name="updateroute"></a>

The `update` method is used to update both the primary and failover route for a phone number, specified within an array. See **Example usage** below. The first route name within the array is assigned as the primary route; the second route listed in the array is assigned as the failover route in the event the first route is unavailable. The list of available route names can be retrieved by calling the [`list`](#listroutes) method.

##### Usage

	#Update Telephone Number Routes
	rtes = [Route(name='primary route'), Route(name='failover route')]
	response = tnc.update(number=phoneNumber, routes=route variable name)

First, define the variable name that identifies the array:

| Parameter       | Required | Type |Description |                                                     
|-----------------|----------|-------|----------------------------------------------------------|
|`rtes`|True| string| Variable name that identifies the array. This field supports an unlimited number of characters. In this example, `rtes` is used.|

Next, define the variables that compose the array:

| Parameter       | Required | Data type| Usage                                                                  |
|-----------------|----------|----------|-------------------------------------------------|
|`pimary route/failover route'`|True| string| Name of an existing route. The first `name` in the array is assigned as the primary route; the second `name` in the array is assigned as the secondary, or failover, route. See [`create_new_route`](#createroute) for the steps to create a route.|
| `phoneNumber` | True   | string  | TThe telephone number on which to update the routes. You must use a Flowroute phone number in an 11-digit, E.164 format: *`1NPANXXXXXX`*.          |

##### Example usage
	
	#Update Telephone Number Routes
	rtes = [Route(name='sip-reg'), Route(name='ea4f4056663e27b082999689982e4723')]
	response = tnc.update(number=16476998778, routes=rtes)

##### Example response

An empty line is returned for a successful update. No other message is returned. You can verify that the routes were changed by calling the [`list`](#listroutes) method.

##### Error response

| Error code | Message  | Description                                           |
|------------|----------|-------------------------------------------------------|
|No error code.  | HTTP Response Not OK|An incorrect route name or an incorrect phone number was passed.|

### InboundRoutesController<a name=inboundcontroller></a>

Location: **./flowroute-numbers-python/FlowrouteNumbersLib/Controllers**

The InboundRoutesController contains the methods required to create new routes and to view your current routes. Methods are added to a Python file, and then that file run from a command line. The following shows a sample file named **routes.py** file, which invokes the Controller's methods:

	from FlowrouteNumbersLib.Controllers.InboundRoutesController import *
	from FlowrouteNumbersLib.Models import *  
	
	Configuration.username="Access Key"
	Configuration.password="Secret Key"
	
	irc = InboundRoutesController()
	
	#List Routes
	response = irc.list(limit=None, page=None)
		 	
 	#Create a New Route
 	response = irc.create_new_route(route_name='name',mtype='route type',value='type value')
 	
	print (response)

TelephoneNumbersController methods are added after `irc = InboundRoutesController()`, but before `print (response)`.  If you do not want to execute a specific method, comment those lines out with `#` 

The Controller contains the following methods:

*	[`list`](#listroutes)
*  [`create_new_route`](#createroute)

#### `list(limit,page)`<a name=listroutes></a>

The `list` method is used to return all of the existing inbound routes from your Flowroute account. From the list, you can retrieve the names and types of routes when applying a route to a phone number or updating an existing route on a phone number.

##### Usage

Add the following lines to your Python file:

	#List Routes
	response = irc.list(limit=None, page=None)

The method takes the following parameters:

| Parameter | Required| Data type | Usage                                            |
|-----------|----------|----------|----------------------------------------|
| `limit`  | True    | Integer| Defines controls the number of items returned. The maximum number of routes returned is 200. If the field is left blank, `()`, all routes are returned. If `(limit=None)`, then ten routes are returned by default.|
| `page`      | False  | string  | Sets which page of the results is returned. For example, if this parameter is set to `1`, page 1 of the results is returned when run. |

##### Example Usage

	#List Routes
	response = irc.list(limit=4, page=None)

##### Example response
	
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
|No error code|HTTP Response Not OK|Typically this occurs when a `limit` does not fall within the allowed range of `1` to `200`, or a negative number; or if `0` or a negative number are passed for the `page`. |	
	
#### `create_new_route(route_name,mtype,value)`<a name="createroute"></a>

The `create_new_route` method is used to create a new inbound route. An inbound route can then be assigned as either a primary or failover route for a phone number. See [`update`](#updateroute) for the steps to update primary and failover routes.

#####Usage

	#Create New Routes
	response = irc.create_new_route(route_name='name',mtype='route type',value='type value')

The method takes the following parameters:

| Parameter | Required | Data type |Description                                                                                   |
|-----------|----------|------------|---------------------------------------------------|
| `name` | True  |string   | The name of the new route. This field supports an unlimited number of alphanumeric characters.  |
| `route type`      | True   | string | The type of route. Allowed values are `HOST`, `PSTN`, and `URI` |
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

>**Note**: In the example above, `print (response)` is added after each line. This returns a success or error response for each line.

#####Example response

An empty string (`''`) is returned for each successfully created route; no other code or message is returned. An error encountered for a specific `irc.create_new_route()` line does not prevent the other routes from being created.
 
	irc.create_new_route(route_name='PSTNroute1',mtype='PSTN',value='16476998778')
	''
	irc.create_new_route(route_name='HOSTroute1',mtype='HOST',value='24.239.23.40:5060')
	''
	irc.create_new_route(route_name='URIroute1',mtype='URI',value='sip:16476998778@215.122.69.152:5060')
	''

#####Error response

| Error code | Message  | Description                                           |
|------------|----------|-------------------------------------------------------|
|Bad request  |`{}`|Typically this occurs when an incorrect number of digits was passed for the telephone number. The number must use E.164, 11-digit `1NPANXXXXXXXXX` format.|
|No error code|HTTP Response Not OK|Typically this occurs when a `value` is malformed. |