# pandadoc_client.DocumentLinkToCRMApi

All URIs are relative to *https://api.pandadoc.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_linked_object**](DocumentLinkToCRMApi.md#create_linked_object) | **POST** /public/v1/documents/{id}/linked-objects | Create Linked Object
[**delete_linked_object**](DocumentLinkToCRMApi.md#delete_linked_object) | **DELETE** /public/v1/documents/{id}/linked-objects/{linked_object_id} | Delete Linked Object
[**list_documents_by_linked_object**](DocumentLinkToCRMApi.md#list_documents_by_linked_object) | **GET** /public/v1/documents/linked-objects | List Documents by Linked Object
[**list_linked_objects**](DocumentLinkToCRMApi.md#list_linked_objects) | **GET** /public/v1/documents/{id}/linked-objects | List Linked Objects


# **create_linked_object**
> LinkedObjectCreateResponse create_linked_object(id, linked_object_create_request)

Create Linked Object

Create a linked object in the document.

> 🚧 
> 
> You can only link each document to each CRM once. This ensures the consistent functionality of the [two-way CRM sync](https://support.pandadoc.com/en/articles/9714877-hubspot-crm#h_3a3344e8-2a6e-4fd8-86be-0da8c121e4ac).
> 
> You can, however, link one document to several external systems.


### Example

* Api Key Authentication (apiKey):
* OAuth Authentication (oauth2):

```python
import pandadoc_client
from pandadoc_client.models.linked_object_create_request import LinkedObjectCreateRequest
from pandadoc_client.models.linked_object_create_response import LinkedObjectCreateResponse
from pandadoc_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.pandadoc.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pandadoc_client.Configuration(
    host = "https://api.pandadoc.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with pandadoc_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pandadoc_client.DocumentLinkToCRMApi(api_client)
    id = 'ZPeAfcpzr9aiVs5vqUf6jg' # str | Specify document ID.
    linked_object_create_request = {"provider":"pipedrive","entity_type":"deal","entity_id":"134"} # LinkedObjectCreateRequest | 

    try:
        # Create Linked Object
        api_response = api_instance.create_linked_object(id, linked_object_create_request)
        print("The response of DocumentLinkToCRMApi->create_linked_object:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentLinkToCRMApi->create_linked_object: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Specify document ID. | 
 **linked_object_create_request** | [**LinkedObjectCreateRequest**](LinkedObjectCreateRequest.md)|  | 

### Return type

[**LinkedObjectCreateResponse**](LinkedObjectCreateResponse.md)

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
**403** | Permission error |  -  |
**404** | Not found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_linked_object**
> delete_linked_object(id, linked_object_id)

Delete Linked Object

Delete a linked object associated with a document.

### Example

* Api Key Authentication (apiKey):
* OAuth Authentication (oauth2):

```python
import pandadoc_client
from pandadoc_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.pandadoc.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pandadoc_client.Configuration(
    host = "https://api.pandadoc.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with pandadoc_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pandadoc_client.DocumentLinkToCRMApi(api_client)
    id = 'ZPeAfcpzr9aiVs5vqUf6jg' # str | Specify document ID.
    linked_object_id = 'deb0d530-d759-4189-a422-8d2265e01b2e' # str | Specify linked object ID.

    try:
        # Delete Linked Object
        api_instance.delete_linked_object(id, linked_object_id)
    except Exception as e:
        print("Exception when calling DocumentLinkToCRMApi->delete_linked_object: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Specify document ID. | 
 **linked_object_id** | **str**| Specify linked object ID. | 

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
**204** | No content |  -  |
**401** | Authentication error |  -  |
**403** | Permission error |  -  |
**404** | Not found |  -  |
**409** | Conflict |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_documents_by_linked_object**
> List[ListDocumentsByLinkedObjectsResponseInner] list_documents_by_linked_object(entity_id, entity_type, provider, order_by=order_by, owner_ids=owner_ids)

List Documents by Linked Object

Get a list of documents connected to a linked object - an entity from an integration.

### Example

* Api Key Authentication (apiKey):
* OAuth Authentication (oauth2):

```python
import pandadoc_client
from pandadoc_client.models.list_documents_by_linked_objects_response_inner import ListDocumentsByLinkedObjectsResponseInner
from pandadoc_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.pandadoc.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pandadoc_client.Configuration(
    host = "https://api.pandadoc.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with pandadoc_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pandadoc_client.DocumentLinkToCRMApi(api_client)
    entity_id = '12345' # str | You can get entity id from your integration, for example, from a url of a HubSpot deal.
    entity_type = 'deal' # str | See the available entity types: https://developers.pandadoc.com/reference/link-service#examples-of-the-most-popular-crms 
    provider = 'hubspot' # str | See the available providers: https://developers.pandadoc.com/reference/link-service#examples-of-the-most-popular-crms 
    order_by = '-date_created' # str |  (optional) (default to '-date_created')
    owner_ids = ["[]"] # List[str] |  (optional) (default to ["[]"])

    try:
        # List Documents by Linked Object
        api_response = api_instance.list_documents_by_linked_object(entity_id, entity_type, provider, order_by=order_by, owner_ids=owner_ids)
        print("The response of DocumentLinkToCRMApi->list_documents_by_linked_object:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentLinkToCRMApi->list_documents_by_linked_object: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_id** | **str**| You can get entity id from your integration, for example, from a url of a HubSpot deal. | 
 **entity_type** | **str**| See the available entity types: https://developers.pandadoc.com/reference/link-service#examples-of-the-most-popular-crms  | 
 **provider** | **str**| See the available providers: https://developers.pandadoc.com/reference/link-service#examples-of-the-most-popular-crms  | 
 **order_by** | **str**|  | [optional] [default to &#39;-date_created&#39;]
 **owner_ids** | [**List[str]**](str.md)|  | [optional] [default to [&quot;[]&quot;]]

### Return type

[**List[ListDocumentsByLinkedObjectsResponseInner]**](ListDocumentsByLinkedObjectsResponseInner.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 |  -  |
**401** | Authentication error |  -  |
**403** | Permission error |  -  |
**404** | Not found |  -  |
**409** | Conflict |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_linked_objects**
> LinkedObjectListResponse list_linked_objects(id)

List Linked Objects

Get a list of linked objects for the document.


### Example

* Api Key Authentication (apiKey):
* OAuth Authentication (oauth2):

```python
import pandadoc_client
from pandadoc_client.models.linked_object_list_response import LinkedObjectListResponse
from pandadoc_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.pandadoc.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pandadoc_client.Configuration(
    host = "https://api.pandadoc.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with pandadoc_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pandadoc_client.DocumentLinkToCRMApi(api_client)
    id = 'ZPeAfcpzr9aiVs5vqUf6jg' # str | Specify document ID.

    try:
        # List Linked Objects
        api_response = api_instance.list_linked_objects(id)
        print("The response of DocumentLinkToCRMApi->list_linked_objects:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentLinkToCRMApi->list_linked_objects: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Specify document ID. | 

### Return type

[**LinkedObjectListResponse**](LinkedObjectListResponse.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success response |  -  |
**401** | Authentication error |  -  |
**403** | Permission error |  -  |
**404** | Not found |  -  |
**409** | Conflict |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

