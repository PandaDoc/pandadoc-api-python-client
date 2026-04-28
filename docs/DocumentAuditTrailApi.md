# pandadoc_client.DocumentAuditTrailApi

All URIs are relative to *https://api.pandadoc.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_document_audit_trail**](DocumentAuditTrailApi.md#list_document_audit_trail) | **GET** /public/v2/documents/{document_id}/audit-trail | List Document Audit Trail


# **list_document_audit_trail**
> DocumentAuditTrailResponse list_document_audit_trail(document_id, limit=limit, offset=offset)

List Document Audit Trail

Retrieves the full audit trail for a specified document. The audit trail includes detailed user actions
such as sending, viewing, signing, and editing, along with metadata like timestamps, IP addresses, and user identity.
This endpoint is accessible to authorized workspace administrators only.


### Example

* Api Key Authentication (apiKey):
* OAuth Authentication (oauth2):

```python
import pandadoc_client
from pandadoc_client.models.document_audit_trail_response import DocumentAuditTrailResponse
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
    api_instance = pandadoc_client.DocumentAuditTrailApi(api_client)
    document_id = 'BhVzRcxH9Z2LgfPPGXFUBa' # str | Unique identifier of the document to retrieve the audit trail for.
    limit = 20 # int | Maximum number of items to return. (optional) (default to 20)
    offset = 0 # int | Number of items to skip before starting to collect the result set. (optional) (default to 0)

    try:
        # List Document Audit Trail
        api_response = api_instance.list_document_audit_trail(document_id, limit=limit, offset=offset)
        print("The response of DocumentAuditTrailApi->list_document_audit_trail:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentAuditTrailApi->list_document_audit_trail: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_id** | **str**| Unique identifier of the document to retrieve the audit trail for. | 
 **limit** | **int**| Maximum number of items to return. | [optional] [default to 20]
 **offset** | **int**| Number of items to skip before starting to collect the result set. | [optional] [default to 0]

### Return type

[**DocumentAuditTrailResponse**](DocumentAuditTrailResponse.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved audit trail. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

