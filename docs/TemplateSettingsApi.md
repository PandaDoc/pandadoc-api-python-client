# pandadoc_client.TemplateSettingsApi

All URIs are relative to *https://api.pandadoc.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**template_settings_get**](TemplateSettingsApi.md#template_settings_get) | **GET** /public/v2/templates/{template_id}/settings | Get template settings
[**template_settings_update**](TemplateSettingsApi.md#template_settings_update) | **PATCH** /public/v2/templates/{template_id}/settings | Update template settings


# **template_settings_get**
> TemplateSettingsResponse template_settings_get(template_id)

Get template settings

Retrieves the settings for a specified template. Only the language field is currently supported.


### Example

* Api Key Authentication (apiKey):
* OAuth Authentication (oauth2):

```python
import pandadoc_client
from pandadoc_client.models.template_settings_response import TemplateSettingsResponse
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
    api_instance = pandadoc_client.TemplateSettingsApi(api_client)
    template_id = 'BhVzRcxH9Z2LgfPPGXFUBa' # str | Unique identifier of the template to retrieve settings for.

    try:
        # Get template settings
        api_response = api_instance.template_settings_get(template_id)
        print("The response of TemplateSettingsApi->template_settings_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemplateSettingsApi->template_settings_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**| Unique identifier of the template to retrieve settings for. | 

### Return type

[**TemplateSettingsResponse**](TemplateSettingsResponse.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved template settings. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **template_settings_update**
> TemplateSettingsResponse template_settings_update(template_id, update_template_settings_request)

Update template settings

Updates the settings for a specified template. Only the language field is currently supported.


### Example

* Api Key Authentication (apiKey):
* OAuth Authentication (oauth2):

```python
import pandadoc_client
from pandadoc_client.models.template_settings_response import TemplateSettingsResponse
from pandadoc_client.models.update_template_settings_request import UpdateTemplateSettingsRequest
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
    api_instance = pandadoc_client.TemplateSettingsApi(api_client)
    template_id = 'BhVzRcxH9Z2LgfPPGXFUBa' # str | Unique identifier of the template to update settings for.
    update_template_settings_request = {"language":"fr-FR"} # UpdateTemplateSettingsRequest | 

    try:
        # Update template settings
        api_response = api_instance.template_settings_update(template_id, update_template_settings_request)
        print("The response of TemplateSettingsApi->template_settings_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemplateSettingsApi->template_settings_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**| Unique identifier of the template to update settings for. | 
 **update_template_settings_request** | [**UpdateTemplateSettingsRequest**](UpdateTemplateSettingsRequest.md)|  | 

### Return type

[**TemplateSettingsResponse**](TemplateSettingsResponse.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully updated template settings. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

