# pandadoc_client.DocumentFieldsApi

All URIs are relative to *https://api.pandadoc.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_document_fields**](DocumentFieldsApi.md#create_document_fields) | **POST** /public/v1/documents/{id}/fields | Create Document Fields
[**list_document_fields**](DocumentFieldsApi.md#list_document_fields) | **GET** /public/v1/documents/{id}/fields | List Document Fields
[**update_document_fields_assignment**](DocumentFieldsApi.md#update_document_fields_assignment) | **PATCH** /public/v1/documents/{id}/fields | Update Document Fields Assignment


# **create_document_fields**
> CreateDocumentFieldsResponse create_document_fields(id, create_document_fields_request)

Create Document Fields

Creates fields for a particular document.
For CFR11-compliant workspaces (21 CFR Part 11), 
signature fields must have a minimum size of 108×33.


### Example

* Api Key Authentication (apiKey):
* OAuth Authentication (oauth2):

```python
import pandadoc_client
from pandadoc_client.models.create_document_fields_request import CreateDocumentFieldsRequest
from pandadoc_client.models.create_document_fields_response import CreateDocumentFieldsResponse
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
    api_instance = pandadoc_client.DocumentFieldsApi(api_client)
    id = 'BhVzRcxH9Z2LgfPPGXFUBa' # str | Document UUID.
    create_document_fields_request = {"fields":[{"type":"text","layout":{"page":1,"position":{"offset_x":1,"offset_y":1,"anchor_point":"topleft"},"style":{"width":1,"height":1}}}]} # CreateDocumentFieldsRequest | 

    try:
        # Create Document Fields
        api_response = api_instance.create_document_fields(id, create_document_fields_request)
        print("The response of DocumentFieldsApi->create_document_fields:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentFieldsApi->create_document_fields: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Document UUID. | 
 **create_document_fields_request** | [**CreateDocumentFieldsRequest**](CreateDocumentFieldsRequest.md)|  | 

### Return type

[**CreateDocumentFieldsResponse**](CreateDocumentFieldsResponse.md)

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
**404** | Not found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_document_fields**
> ListDocumentFieldsResponse list_document_fields(id)

List Document Fields

Return the list of fields for a particular document.

### Example

* Api Key Authentication (apiKey):
* OAuth Authentication (oauth2):

```python
import pandadoc_client
from pandadoc_client.models.list_document_fields_response import ListDocumentFieldsResponse
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
    api_instance = pandadoc_client.DocumentFieldsApi(api_client)
    id = 'BhVzRcxH9Z2LgfPPGXFUBa' # str | Document UUID.

    try:
        # List Document Fields
        api_response = api_instance.list_document_fields(id)
        print("The response of DocumentFieldsApi->list_document_fields:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentFieldsApi->list_document_fields: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Document UUID. | 

### Return type

[**ListDocumentFieldsResponse**](ListDocumentFieldsResponse.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Authentication error |  -  |
**404** | Not found |  -  |
**409** | Conflict |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_document_fields_assignment**
> update_document_fields_assignment(id, update_document_fields_assignment_request)

Update Document Fields Assignment

Assign, reassign, or unassign document fields to recipients.
Supports bulk operations by accepting multiple field assignment items in a single request.

> 🚧 Before you start
>
> - The document must be in the 'Draft' (`document.draft`) status.
> - You must have the 'Can Edit Document' permission.


### Example

* Api Key Authentication (apiKey):
* OAuth Authentication (oauth2):

```python
import pandadoc_client
from pandadoc_client.models.update_document_fields_assignment_request import UpdateDocumentFieldsAssignmentRequest
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
    api_instance = pandadoc_client.DocumentFieldsApi(api_client)
    id = 'BhVzRcxH9Z2LgfPPGXFUBa' # str | Document UUID.
    update_document_fields_assignment_request = {"fields":[{"field_id":"d6948f39-612a-4626-a439-ca9e0cbbda7c","assigned_to":"tf5dGS3Tmu3cj228ao6fnc"}]} # UpdateDocumentFieldsAssignmentRequest | A list of field assignment operations to apply to the document.

    try:
        # Update Document Fields Assignment
        api_instance.update_document_fields_assignment(id, update_document_fields_assignment_request)
    except Exception as e:
        print("Exception when calling DocumentFieldsApi->update_document_fields_assignment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Document UUID. | 
 **update_document_fields_assignment_request** | [**UpdateDocumentFieldsAssignmentRequest**](UpdateDocumentFieldsAssignmentRequest.md)| A list of field assignment operations to apply to the document. | 

### Return type

void (empty response body)

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

