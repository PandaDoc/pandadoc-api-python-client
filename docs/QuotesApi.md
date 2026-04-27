# pandadoc_client.QuotesApi

All URIs are relative to *https://api.pandadoc.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**quote_update**](QuotesApi.md#quote_update) | **PUT** /public/v1/documents/{document_id}/quotes/{quote_id} | Quote update


# **quote_update**
> QuoteResponse quote_update(document_id, quote_id, quote_update_request)

Quote update

This operation updates the details of a specific quote within a document by specifying the document ID and quote ID.

### Example

* Api Key Authentication (apiKey):
* OAuth Authentication (oauth2):

```python
import pandadoc_client
from pandadoc_client.models.quote_response import QuoteResponse
from pandadoc_client.models.quote_update_request import QuoteUpdateRequest
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
    api_instance = pandadoc_client.QuotesApi(api_client)
    document_id = 'BhVzRcxH9Z2LgfPPGXFUBa' # str | Document ID
    quote_id = '99aaa4f9-3250-4f5b-a953-6d7bfc5d8c9e' # str | Quote ID
    quote_update_request = pandadoc_client.QuoteUpdateRequest() # QuoteUpdateRequest | 

    try:
        # Quote update
        api_response = api_instance.quote_update(document_id, quote_id, quote_update_request)
        print("The response of QuotesApi->quote_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuotesApi->quote_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_id** | **str**| Document ID | 
 **quote_id** | **str**| Quote ID | 
 **quote_update_request** | [**QuoteUpdateRequest**](QuoteUpdateRequest.md)|  | 

### Return type

[**QuoteResponse**](QuoteResponse.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Authentication error |  -  |
**403** | Permission error |  -  |
**404** | Not found |  -  |
**409** | Conflict |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

