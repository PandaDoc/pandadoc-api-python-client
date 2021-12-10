# pandadoc_client.ContentLibraryItemsApi

All URIs are relative to *https://api.pandadoc.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**details_content_library_item**](ContentLibraryItemsApi.md#details_content_library_item) | **GET** /public/v1/content-library-items/{id}/details | Details Content Library Item
[**list_content_library_items**](ContentLibraryItemsApi.md#list_content_library_items) | **GET** /public/v1/content-library-items | List Content Library Item


# **details_content_library_item**
> ContentLibraryItemResponse details_content_library_item(id)

Details Content Library Item

Return detailed data about a content library item.

### Example

* Api Key Authentication (apiKey):
* OAuth Authentication (oauth2):

```python
import pandadoc_client
from pandadoc_client.api import content_library_items_api
from pandadoc_client.model.content_library_item_response import ContentLibraryItemResponse
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
    api_instance = content_library_items_api.ContentLibraryItemsApi(api_client)
    id = "UXdP7Lnbvvr4WEb2wzM2hc"  # str | Content Library Item ID

    # example passing only required values which don't have defaults set
    try:
        # Details Content Library Item
        api_response = api_instance.details_content_library_item(id)
        pprint(api_response)
    except pandadoc_client.ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **list_content_library_items**
> ContentLibraryItemListResponse list_content_library_items()

List Content Library Item

Optionally filter by a search query or tags.

### Example

* Api Key Authentication (apiKey):
* OAuth Authentication (oauth2):

```python
import pandadoc_client
from pandadoc_client.api import content_library_items_api
from pandadoc_client.model.content_library_item_list_response import ContentLibraryItemListResponse
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
    api_instance = content_library_items_api.ContentLibraryItemsApi(api_client)
    q = "Sample Pricing Table"  # str | Search query. Filter by content library item name. (optional)
    id = "UXdP7Lnbvvr4WEb2wzM2hc"  # str | Specify content library item ID. (optional)
    deleted = True  # bool | Returns only the deleted content library items. (optional)
    folder_uuid = "S6xX7saJfA44mtJxGWd95L"  # str | The UUID of the folder where the content library items are stored. (optional)
    count = 10  # int | Specify how many content library items to return. Default is 50 content library items, maximum is 100 content library items. (optional)
    page = 1  # int | Specify which page of the dataset to return. (optional)
    tag = "pricing_tables"  # str | Search tag. Filter by content library item tag. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List Content Library Item
        api_response = api_instance.list_content_library_items(
            q=q,
            id=id,
            deleted=deleted,
            folder_uuid=folder_uuid,
            count=count,
            page=page,
            tag=tag,
        )
        pprint(api_response)
    except pandadoc_client.ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

