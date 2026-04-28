# pandadoc_client.DocumentSettingsApi

All URIs are relative to *https://api.pandadoc.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**document_settings_get**](DocumentSettingsApi.md#document_settings_get) | **GET** /public/v2/documents/{document_id}/settings | Get document settings
[**document_settings_update**](DocumentSettingsApi.md#document_settings_update) | **PATCH** /public/v2/documents/{document_id}/settings | Update document settings


# **document_settings_get**
> DocumentSettingsResponse document_settings_get(document_id)

Get document settings

Retrieves the settings for a specified document. Supported fields: language, qualified_electronic_signature, expires_in (in days).


### Example

* Api Key Authentication (apiKey):
* OAuth Authentication (oauth2):

```python
import pandadoc_client
from pandadoc_client.models.document_settings_response import DocumentSettingsResponse
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
    api_instance = pandadoc_client.DocumentSettingsApi(api_client)
    document_id = 'BhVzRcxH9Z2LgfPPGXFUBa' # str | Unique identifier of the document to retrieve settings for.

    try:
        # Get document settings
        api_response = api_instance.document_settings_get(document_id)
        print("The response of DocumentSettingsApi->document_settings_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentSettingsApi->document_settings_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_id** | **str**| Unique identifier of the document to retrieve settings for. | 

### Return type

[**DocumentSettingsResponse**](DocumentSettingsResponse.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved document settings. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **document_settings_update**
> DocumentSettingsResponse document_settings_update(document_id, update_document_settings_request)

Update document settings

Updates the settings for a specified document. Supported fields: language, qualified_electronic_signature, expires_in (in days).


### Example

* Api Key Authentication (apiKey):
* OAuth Authentication (oauth2):

```python
import pandadoc_client
from pandadoc_client.models.document_settings_response import DocumentSettingsResponse
from pandadoc_client.models.update_document_settings_request import UpdateDocumentSettingsRequest
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
    api_instance = pandadoc_client.DocumentSettingsApi(api_client)
    document_id = 'BhVzRcxH9Z2LgfPPGXFUBa' # str | Unique identifier of the document to update settings for.
    update_document_settings_request = {"language":"fr-FR","qualified_electronic_signature":true,"expires_in":60} # UpdateDocumentSettingsRequest | 

    try:
        # Update document settings
        api_response = api_instance.document_settings_update(document_id, update_document_settings_request)
        print("The response of DocumentSettingsApi->document_settings_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentSettingsApi->document_settings_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_id** | **str**| Unique identifier of the document to update settings for. | 
 **update_document_settings_request** | [**UpdateDocumentSettingsRequest**](UpdateDocumentSettingsRequest.md)|  | 

### Return type

[**DocumentSettingsResponse**](DocumentSettingsResponse.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully updated document settings. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

