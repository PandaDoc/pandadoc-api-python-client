# pandadoc_client.ContactsApi

All URIs are relative to *https://api.pandadoc.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**contact_create**](ContactsApi.md#contact_create) | **POST** /public/v1/contacts | Create contact
[**contact_delete**](ContactsApi.md#contact_delete) | **DELETE** /public/v1/contacts/{id} | Delete contact by id
[**contact_details**](ContactsApi.md#contact_details) | **GET** /public/v1/contacts/{id} | Get contact details by id
[**contact_list**](ContactsApi.md#contact_list) | **GET** /public/v1/contacts | List contacts
[**contact_update**](ContactsApi.md#contact_update) | **PATCH** /public/v1/contacts/{id} | Update contact by id


# **contact_create**
> ContactDetailsResponse contact_create(contact_create_request)

Create contact

### Example

* Api Key Authentication (apiKey):
* OAuth Authentication (oauth2):

```python
import pandadoc_client
from pandadoc_client.api import contacts_api
from pandadoc_client.model.contact_create_request import ContactCreateRequest
from pandadoc_client.model.contact_details_response import ContactDetailsResponse
from pprint import pprint

# Defining the host is optional and defaults to https://api.pandadoc.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pandadoc_client.Configuration(
    host="https://api.pandadoc.com",
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = 'YOUR_API_KEY'
configuration.api_key_prefix['apiKey'] = 'API-Key'

# Configure OAuth2 access token for authorization: oauth2
# configuration = pandadoc_client.Configuration(
#    host="https://api.pandadoc.com",
# )
# configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pandadoc_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = contacts_api.ContactsApi(api_client)
    contact_create_request = ContactCreateRequest(
        email="user01@pandadoc.com",
        first_name="John",
        last_name="Doe",
        company="John Doe Inc.",
        job_title="CTO",
        phone="+14842634627",
        state="Texas",
        street_address="1313 Mockingbird Lane",
        city="Austin",
        postal_code="75001",
    )  # ContactCreateRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Create contact
        api_response = api_instance.contact_create(contact_create_request)
        pprint(api_response)
    except pandadoc_client.ApiException as e:
        print("Exception when calling ContactsApi->contact_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contact_create_request** | [**ContactCreateRequest**](ContactCreateRequest.md)|  |

### Return type

[**ContactDetailsResponse**](ContactDetailsResponse.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Authentication error |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **contact_delete**
> contact_delete(id)

Delete contact by id

### Example

* Api Key Authentication (apiKey):
* OAuth Authentication (oauth2):

```python
import pandadoc_client
from pandadoc_client.api import contacts_api
from pprint import pprint

# Defining the host is optional and defaults to https://api.pandadoc.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pandadoc_client.Configuration(
    host="https://api.pandadoc.com",
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = 'YOUR_API_KEY'
configuration.api_key_prefix['apiKey'] = 'API-Key'

# Configure OAuth2 access token for authorization: oauth2
# configuration = pandadoc_client.Configuration(
#    host="https://api.pandadoc.com",
# )
# configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pandadoc_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = contacts_api.ContactsApi(api_client)
    id = "SyoufNkJiHRn24LpuJ7RXb"  # str | Contact id.

    # example passing only required values which don't have defaults set
    try:
        # Delete contact by id
        api_instance.contact_delete(id)
    except pandadoc_client.ApiException as e:
        print("Exception when calling ContactsApi->contact_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Contact id. |

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Bad Request |  -  |
**403** | Authentication error |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **contact_details**
> ContactDetailsResponse contact_details(id)

Get contact details by id

### Example

* Api Key Authentication (apiKey):
* OAuth Authentication (oauth2):

```python
import pandadoc_client
from pandadoc_client.api import contacts_api
from pandadoc_client.model.contact_details_response import ContactDetailsResponse
from pprint import pprint

# Defining the host is optional and defaults to https://api.pandadoc.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pandadoc_client.Configuration(
    host="https://api.pandadoc.com",
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = 'YOUR_API_KEY'
configuration.api_key_prefix['apiKey'] = 'API-Key'

# Configure OAuth2 access token for authorization: oauth2
# configuration = pandadoc_client.Configuration(
#    host="https://api.pandadoc.com",
# )
# configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pandadoc_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = contacts_api.ContactsApi(api_client)
    id = "SyoufNkJiHRn24LpuJ7RXb"  # str | Contact id.

    # example passing only required values which don't have defaults set
    try:
        # Get contact details by id
        api_response = api_instance.contact_details(id)
        pprint(api_response)
    except pandadoc_client.ApiException as e:
        print("Exception when calling ContactsApi->contact_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Contact id. |

### Return type

[**ContactDetailsResponse**](ContactDetailsResponse.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Bad Request |  -  |
**403** | Authentication error |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **contact_list**
> ContactListResponse contact_list()

List contacts

### Example

* Api Key Authentication (apiKey):
* OAuth Authentication (oauth2):

```python
import pandadoc_client
from pandadoc_client.api import contacts_api
from pandadoc_client.model.contact_list_response import ContactListResponse
from pprint import pprint

# Defining the host is optional and defaults to https://api.pandadoc.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pandadoc_client.Configuration(
    host="https://api.pandadoc.com",
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = 'YOUR_API_KEY'
configuration.api_key_prefix['apiKey'] = 'API-Key'

# Configure OAuth2 access token for authorization: oauth2
# configuration = pandadoc_client.Configuration(
#    host="https://api.pandadoc.com",
# )
# configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pandadoc_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = contacts_api.ContactsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # List contacts
        api_response = api_instance.contact_list()
        pprint(api_response)
    except pandadoc_client.ApiException as e:
        print("Exception when calling ContactsApi->contact_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ContactListResponse**](ContactListResponse.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Bad Request |  -  |
**403** | Authentication error |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **contact_update**
> ContactDetailsResponse contact_update(id, contact_update_request)

Update contact by id

### Example

* Api Key Authentication (apiKey):
* OAuth Authentication (oauth2):

```python
import pandadoc_client
from pandadoc_client.api import contacts_api
from pandadoc_client.model.contact_details_response import ContactDetailsResponse
from pandadoc_client.model.contact_update_request import ContactUpdateRequest
from pprint import pprint

# Defining the host is optional and defaults to https://api.pandadoc.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pandadoc_client.Configuration(
    host="https://api.pandadoc.com",
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = 'YOUR_API_KEY'
configuration.api_key_prefix['apiKey'] = 'API-Key'

# Configure OAuth2 access token for authorization: oauth2
# configuration = pandadoc_client.Configuration(
#    host="https://api.pandadoc.com",
# )
# configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pandadoc_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = contacts_api.ContactsApi(api_client)
    id = "SyoufNkJiHRn24LpuJ7RXb"  # str | Contact id.
    contact_update_request = ContactUpdateRequest(
        email="user01@pandadoc.com",
        first_name="John",
        last_name="Doe",
        company="John Doe Inc.",
        job_title="CTO",
        phone="+14842634627",
        state="Texas",
        street_address="1313 Mockingbird Lane",
        city="Austin",
        postal_code="75001",
    )  # ContactUpdateRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Update contact by id
        api_response = api_instance.contact_update(id, contact_update_request)
        pprint(api_response)
    except pandadoc_client.ApiException as e:
        print("Exception when calling ContactsApi->contact_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Contact id. |
 **contact_update_request** | [**ContactUpdateRequest**](ContactUpdateRequest.md)|  |

### Return type

[**ContactDetailsResponse**](ContactDetailsResponse.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Authentication error |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

