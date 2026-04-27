# pandadoc_client.ContentLibraryItemsApi

All URIs are relative to *https://api.pandadoc.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_content_library_item**](ContentLibraryItemsApi.md#create_content_library_item) | **POST** /public/v1/content-library-items | Create Content Library Item
[**create_content_library_item_from_upload**](ContentLibraryItemsApi.md#create_content_library_item_from_upload) | **POST** /public/v1/content-library-items?upload | Create Content Library Item from File Upload
[**details_content_library_item**](ContentLibraryItemsApi.md#details_content_library_item) | **GET** /public/v1/content-library-items/{id}/details | Content Library Item Details
[**list_content_library_items**](ContentLibraryItemsApi.md#list_content_library_items) | **GET** /public/v1/content-library-items | List Content Library Item
[**status_content_library_item**](ContentLibraryItemsApi.md#status_content_library_item) | **GET** /public/v1/content-library-items/{id} | Content Library Item Status


# **create_content_library_item**
> ContentLibraryResponse create_content_library_item(content_library_item_create_from_url_request)

Create Content Library Item

This API endpoint allows users to create an empty item in the content library.
No actual content or data is required to be provided in the initial creation.


### Example

* Api Key Authentication (apiKey):
* OAuth Authentication (oauth2):

```python
import pandadoc_client
from pandadoc_client.models.content_library_item_create_from_url_request import ContentLibraryItemCreateFromUrlRequest
from pandadoc_client.models.content_library_response import ContentLibraryResponse
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
    api_instance = pandadoc_client.ContentLibraryItemsApi(api_client)
    content_library_item_create_from_url_request = {"name":"CLI name example"} # ContentLibraryItemCreateFromUrlRequest | 

    try:
        # Create Content Library Item
        api_response = api_instance.create_content_library_item(content_library_item_create_from_url_request)
        print("The response of ContentLibraryItemsApi->create_content_library_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContentLibraryItemsApi->create_content_library_item: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_library_item_create_from_url_request** | [**ContentLibraryItemCreateFromUrlRequest**](ContentLibraryItemCreateFromUrlRequest.md)|  | 

### Return type

[**ContentLibraryResponse**](ContentLibraryResponse.md)

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
**403** | Permission error |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_content_library_item_from_upload**
> ContentLibraryResponse create_content_library_item_from_upload(file=file, data=data)

Create Content Library Item from File Upload

This asynchronous endpoint allows users to create a new CLI by uploading a file.
The uploaded file is processed in the background to generate the CLI.
The maximum allowable file size for upload is 100 MB.
Field tags and form fields are not supported yet.
Once the file is uploaded, the processing will happen asynchronously, and users need to check the status of the CLI creation.


### Example

* Api Key Authentication (apiKey):
* OAuth Authentication (oauth2):

```python
import pandadoc_client
from pandadoc_client.models.content_library_response import ContentLibraryResponse
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
    api_instance = pandadoc_client.ContentLibraryItemsApi(api_client)
    file = None # bytearray | Binary PDF File (optional)
    data = pandadoc_client.ContentLibraryItemCreateRequest() # ContentLibraryItemCreateRequest | JSON as a multipart/form-data request. (optional)

    try:
        # Create Content Library Item from File Upload
        api_response = api_instance.create_content_library_item_from_upload(file=file, data=data)
        print("The response of ContentLibraryItemsApi->create_content_library_item_from_upload:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContentLibraryItemsApi->create_content_library_item_from_upload: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **bytearray**| Binary PDF File | [optional] 
 **data** | [**ContentLibraryItemCreateRequest**](ContentLibraryItemCreateRequest.md)| JSON as a multipart/form-data request. | [optional] 

### Return type

[**ContentLibraryResponse**](ContentLibraryResponse.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Authentication error |  -  |
**403** | Permission error |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **details_content_library_item**
> ContentLibraryItemResponse details_content_library_item(id)

Content Library Item Details

Retrieve detailed information about a specific content library item using its ID. The details include:

- **Roles**
- **All fields with values**
- **All tokens with values**
- **Pricing information (pricing tables, products, etc)**
- **Metadata**
- **Tags**
- **Modification Timestamps**: note that `date_modified` means any changes associated with the CLI, while `content_date_modified` logs any changes in CLI content.


### Example

* Api Key Authentication (apiKey):
* OAuth Authentication (oauth2):

```python
import pandadoc_client
from pandadoc_client.models.content_library_item_response import ContentLibraryItemResponse
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
    api_instance = pandadoc_client.ContentLibraryItemsApi(api_client)
    id = 'UXdP7Lnbvvr4WEb2wzM2hc' # str | Content Library Item ID

    try:
        # Content Library Item Details
        api_response = api_instance.details_content_library_item(id)
        print("The response of ContentLibraryItemsApi->details_content_library_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContentLibraryItemsApi->details_content_library_item: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Content Library Item ID | 

### Return type

[**ContentLibraryItemResponse**](ContentLibraryItemResponse.md)

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
**403** | Permission error |  -  |
**404** | Not found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_content_library_items**
> ContentLibraryItemListResponse list_content_library_items(q=q, id=id, deleted=deleted, folder_uuid=folder_uuid, count=count, page=page, tag=tag)

List Content Library Item

The endpoint retrieves items from the content library in PandaDoc. This endpoint supports filtering options to narrow down the results, allowing users to search by query, tags, folder, and more.

> ### ⚠️ Please avoid empty values for the parameters
> API returns "400" error when any of the parameters has an empty value. Please remove such a parameter from the request or add a value.


### Example

* Api Key Authentication (apiKey):
* OAuth Authentication (oauth2):

```python
import pandadoc_client
from pandadoc_client.models.content_library_item_list_response import ContentLibraryItemListResponse
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
    api_instance = pandadoc_client.ContentLibraryItemsApi(api_client)
    q = 'Sample Pricing Table' # str | Search query. Filter by content library item name. (optional)
    id = 'UXdP7Lnbvvr4WEb2wzM2hc' # str | Specify content library item ID. (optional)
    deleted = false # bool | Returns only the deleted content library items. (optional)
    folder_uuid = 'S6xX7saJfA44mtJxGWd95L' # str | The UUID of the folder where the content library items are stored. (optional)
    count = 10 # int | Specify how many content library items to return. Default is 50 content library items, maximum is 100 content library items. (optional)
    page = 1 # int | Specify which page of the dataset to return. (optional)
    tag = 'pricing_tables' # str | Search tag. Filter by content library item tag. (optional)

    try:
        # List Content Library Item
        api_response = api_instance.list_content_library_items(q=q, id=id, deleted=deleted, folder_uuid=folder_uuid, count=count, page=page, tag=tag)
        print("The response of ContentLibraryItemsApi->list_content_library_items:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContentLibraryItemsApi->list_content_library_items: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**| Search query. Filter by content library item name. | [optional] 
 **id** | **str**| Specify content library item ID. | [optional] 
 **deleted** | **bool**| Returns only the deleted content library items. | [optional] 
 **folder_uuid** | **str**| The UUID of the folder where the content library items are stored. | [optional] 
 **count** | **int**| Specify how many content library items to return. Default is 50 content library items, maximum is 100 content library items. | [optional] 
 **page** | **int**| Specify which page of the dataset to return. | [optional] 
 **tag** | **str**| Search tag. Filter by content library item tag. | [optional] 

### Return type

[**ContentLibraryItemListResponse**](ContentLibraryItemListResponse.md)

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
**401** | Authentication error |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **status_content_library_item**
> ContentLibraryResponse status_content_library_item(id)

Content Library Item Status

Requesting the CLI status helps verify that a CLI is in the expected state before invoking additional API methods.

## Available CLI Statuses

The following is a complete list of all possible CLI statuses returned:

| CLI Status | Status Description |
|-----------------|--------------------|
| `cli.UPLOADED`  | The CLI upload process has been initiated and is currently in progress. It will soon transition to the `cli.PROCESSED` state. |
| `cli.PROCESSED` | The CLI has been successfully uploaded and created. At this stage, all aspects of the CLI are editable. |
| `cli.ERROR`     | The CLI upload process has failed. Please refer to the error details in the response for more information. |


### Example

* Api Key Authentication (apiKey):
* OAuth Authentication (oauth2):

```python
import pandadoc_client
from pandadoc_client.models.content_library_response import ContentLibraryResponse
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
    api_instance = pandadoc_client.ContentLibraryItemsApi(api_client)
    id = 'EE8yUNg5HztqVAuH85He8V' # str | Content Library Item ID

    try:
        # Content Library Item Status
        api_response = api_instance.status_content_library_item(id)
        print("The response of ContentLibraryItemsApi->status_content_library_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContentLibraryItemsApi->status_content_library_item: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Content Library Item ID | 

### Return type

[**ContentLibraryResponse**](ContentLibraryResponse.md)

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
**403** | Permission error |  -  |
**404** | Not found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

