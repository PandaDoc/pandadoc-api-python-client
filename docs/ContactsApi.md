# pandadoc_client.ContactsApi

All URIs are relative to *https://api.pandadoc.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_contact**](ContactsApi.md#create_contact) | **POST** /public/v1/contacts | Create contact
[**delete_contact**](ContactsApi.md#delete_contact) | **DELETE** /public/v1/contacts/{id} | Delete contact by id
[**details_contact**](ContactsApi.md#details_contact) | **GET** /public/v1/contacts/{id} | Get contact details by id
[**list_contacts**](ContactsApi.md#list_contacts) | **GET** /public/v1/contacts | List contacts
[**update_contact**](ContactsApi.md#update_contact) | **PATCH** /public/v1/contacts/{id} | Update contact by id


# **create_contact**
> ContactDetailsResponse create_contact(contact_create_request)

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
        api_response = api_instance.create_contact(contact_create_request)
        pprint(api_response)
    except pandadoc_client.ApiException as e:
        print("Exception when calling ContactsApi->create_contact: %s\n" % e)
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

# **delete_contact**
> delete_contact(id)

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
        api_instance.delete_contact(id)
    except pandadoc_client.ApiException as e:
        print("Exception when calling ContactsApi->delete_contact: %s\n" % e)
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

# **details_contact**
> ContactDetailsResponse details_contact(id)

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
        api_response = api_instance.details_contact(id)
        pprint(api_response)
    except pandadoc_client.ApiException as e:
        print("Exception when calling ContactsApi->details_contact: %s\n" % e)
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

# **list_contacts**
> ContactListResponse list_contacts()

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
    email = "josh@example.com"  # str | Optional search parameter. Filter results by exact match. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List contacts
        api_response = api_instance.list_contacts(
            email=email,
        )
        pprint(api_response)
    except pandadoc_client.ApiException as e:
        print("Exception when calling ContactsApi->list_contacts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| Optional search parameter. Filter results by exact match. | [optional]

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

# **update_contact**
> ContactDetailsResponse update_contact(id, contact_update_request)

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
        api_response = api_instance.update_contact(id, contact_update_request)
        pprint(api_response)
    except pandadoc_client.ApiException as e:
        print("Exception when calling ContactsApi->update_contact: %s\n" % e)
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

