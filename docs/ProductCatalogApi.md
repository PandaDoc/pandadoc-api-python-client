# pandadoc_client.ProductCatalogApi

All URIs are relative to *https://api.pandadoc.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_catalog_item**](ProductCatalogApi.md#create_catalog_item) | **POST** /public/v2/product-catalog/items | Create Catalog Item
[**delete_catalog_item**](ProductCatalogApi.md#delete_catalog_item) | **DELETE** /public/v2/product-catalog/items/{item_uuid} | Delete Catalog Item
[**get_catalog_item**](ProductCatalogApi.md#get_catalog_item) | **GET** /public/v2/product-catalog/items/{item_uuid} | Catalog Item Details
[**search_catalog_items**](ProductCatalogApi.md#search_catalog_items) | **GET** /public/v2/product-catalog/items/search | List Catalog Items Search
[**update_catalog_item**](ProductCatalogApi.md#update_catalog_item) | **PATCH** /public/v2/product-catalog/items/{item_uuid} | Update Catalog Item


# **create_catalog_item**
> ProductCatalogItemResponse create_catalog_item(product_catalog_item_request)

Create Catalog Item

Create a new catalog item.

### Example

* Api Key Authentication (apiKey):
* OAuth Authentication (oauth2):

```python
import pandadoc_client
from pandadoc_client.models.product_catalog_item_request import ProductCatalogItemRequest
from pandadoc_client.models.product_catalog_item_response import ProductCatalogItemResponse
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
    api_instance = pandadoc_client.ProductCatalogApi(api_client)
    product_catalog_item_request = {"type":"regular","title":"New Product","category_id":null,"sku":"","description":null,"price_configuration":{"currency":"EUR","price":1,"cost":null,"pricing_method":0,"tiers":null,"billing_type":"one_time","billing_cycle":null},"custom_fields":[],"images":[],"bundle_items":[]} # ProductCatalogItemRequest | 

    try:
        # Create Catalog Item
        api_response = api_instance.create_catalog_item(product_catalog_item_request)
        print("The response of ProductCatalogApi->create_catalog_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductCatalogApi->create_catalog_item: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_catalog_item_request** | [**ProductCatalogItemRequest**](ProductCatalogItemRequest.md)|  | 

### Return type

[**ProductCatalogItemResponse**](ProductCatalogItemResponse.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully created a new catalog item |  -  |
**403** | Permission error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_catalog_item**
> delete_catalog_item(item_uuid)

Delete Catalog Item

Delete catalog item.

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
    api_instance = pandadoc_client.ProductCatalogApi(api_client)
    item_uuid = '2e39c7e0-acb0-4ff2-b4cd-ea3141f95db8' # str | Catalog item UUID

    try:
        # Delete Catalog Item
        api_instance.delete_catalog_item(item_uuid)
    except Exception as e:
        print("Exception when calling ProductCatalogApi->delete_catalog_item: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_uuid** | **str**| Catalog item UUID | 

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
**200** | No content |  -  |
**403** | Permission error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_catalog_item**
> ProductCatalogItemResponse get_catalog_item(item_uuid)

Catalog Item Details

Get catalog item.

### Example

* Api Key Authentication (apiKey):
* OAuth Authentication (oauth2):

```python
import pandadoc_client
from pandadoc_client.models.product_catalog_item_response import ProductCatalogItemResponse
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
    api_instance = pandadoc_client.ProductCatalogApi(api_client)
    item_uuid = '2e39c7e0-acb0-4ff2-b4cd-ea3141f95db8' # str | Catalog item UUID

    try:
        # Catalog Item Details
        api_response = api_instance.get_catalog_item(item_uuid)
        print("The response of ProductCatalogApi->get_catalog_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductCatalogApi->get_catalog_item: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_uuid** | **str**| Catalog item UUID | 

### Return type

[**ProductCatalogItemResponse**](ProductCatalogItemResponse.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get Catalog Item |  -  |
**403** | Permission error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_catalog_items**
> ListCatalogItemsSearchResponse search_catalog_items(page=page, per_page=per_page, query=query, order_by=order_by, types=types, billing_types=billing_types, exclude_uuids=exclude_uuids, category_id=category_id, no_category=no_category)

List Catalog Items Search

This method searches for items in your [product catalog](https://support.pandadoc.com/en/articles/9714691-product-catalog).

Use the `query` parameter to search in title, SKU, description, category name, custom fields name and value. You can also search for items by their type, billing type, and category id.

Order search results, in both ascending and descending order, by these item properties:

- SKU
- Name
- Price
- Modification date

Use the `exclude_uuids` parameter to exclude particular uuids from the search request.


### Example

* Api Key Authentication (apiKey):
* OAuth Authentication (oauth2):

```python
import pandadoc_client
from pandadoc_client.models.list_catalog_items_search_response import ListCatalogItemsSearchResponse
from pandadoc_client.models.product_catalog_type_enum import ProductCatalogTypeEnum
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
    api_instance = pandadoc_client.ProductCatalogApi(api_client)
    page = 1 # float | Page number. (optional)
    per_page = 10 # float | Items per page. (optional)
    query = 'coffee' # str | Search query. Searches the following fields: Title, SKU, description, category name, custom fields name and value.  (optional)
    order_by = '-date_modified' # str | Ordering principle for displaying search results. (optional)
    types = [pandadoc_client.ProductCatalogTypeEnum()] # List[ProductCatalogTypeEnum] | Filter by catalog item types. (optional)
    billing_types = ['[\"one_time\"]'] # List[str] | Filter by billing types. (optional)
    exclude_uuids = ['[\"1725f759-3a1c-64e3-2daa-f67eafa589d7\",\"06cb0ce9-094b-1f38-2fe6-0a9d226cd22c\"]'] # List[str] | A list of item uuids to be excluded from search. (optional)
    category_id = '06cb0ce9-094b-1f38-2fe6-0a9d226cd22c' # str | Category id. (optional)
    no_category = true # bool |  (optional)

    try:
        # List Catalog Items Search
        api_response = api_instance.search_catalog_items(page=page, per_page=per_page, query=query, order_by=order_by, types=types, billing_types=billing_types, exclude_uuids=exclude_uuids, category_id=category_id, no_category=no_category)
        print("The response of ProductCatalogApi->search_catalog_items:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductCatalogApi->search_catalog_items: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **float**| Page number. | [optional] 
 **per_page** | **float**| Items per page. | [optional] 
 **query** | **str**| Search query. Searches the following fields: Title, SKU, description, category name, custom fields name and value.  | [optional] 
 **order_by** | **str**| Ordering principle for displaying search results. | [optional] 
 **types** | [**List[ProductCatalogTypeEnum]**](ProductCatalogTypeEnum.md)| Filter by catalog item types. | [optional] 
 **billing_types** | [**List[str]**](str.md)| Filter by billing types. | [optional] 
 **exclude_uuids** | [**List[str]**](str.md)| A list of item uuids to be excluded from search. | [optional] 
 **category_id** | **str**| Category id. | [optional] 
 **no_category** | **bool**|  | [optional] 

### Return type

[**ListCatalogItemsSearchResponse**](ListCatalogItemsSearchResponse.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Paginated catalog items |  -  |
**400** | Bad Request error |  -  |
**401** | Authentication error |  -  |
**403** | Permission error |  -  |
**429** | Too many requests error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_catalog_item**
> ProductCatalogItemResponse update_catalog_item(item_uuid, product_catalog_item_patch_request)

Update Catalog Item

Update catalog item.

### Example

* Api Key Authentication (apiKey):
* OAuth Authentication (oauth2):

```python
import pandadoc_client
from pandadoc_client.models.product_catalog_item_patch_request import ProductCatalogItemPatchRequest
from pandadoc_client.models.product_catalog_item_response import ProductCatalogItemResponse
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
    api_instance = pandadoc_client.ProductCatalogApi(api_client)
    item_uuid = '2e39c7e0-acb0-4ff2-b4cd-ea3141f95db8' # str | Catalog item UUID
    product_catalog_item_patch_request = {"type":"regular","title":"New name","category_id":null,"product_variant":{"sku":"211813881147","description":"<p>New description</p>","custom_fields":[{"name":"Field","value":"Value"}],"price_configuration":{"price":99,"currency":"USD","cost":1,"pricing_method":1,"tiers":[{"min_qty":1,"value":10},{"min_qty":2,"value":8}],"billing_type":"one_time","billing_cycle":null},"images":[]},"bundle_items":[]} # ProductCatalogItemPatchRequest | 

    try:
        # Update Catalog Item
        api_response = api_instance.update_catalog_item(item_uuid, product_catalog_item_patch_request)
        print("The response of ProductCatalogApi->update_catalog_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductCatalogApi->update_catalog_item: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_uuid** | **str**| Catalog item UUID | 
 **product_catalog_item_patch_request** | [**ProductCatalogItemPatchRequest**](ProductCatalogItemPatchRequest.md)|  | 

### Return type

[**ProductCatalogItemResponse**](ProductCatalogItemResponse.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Update Catalog item |  -  |
**403** | Permission error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

