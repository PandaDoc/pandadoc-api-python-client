# pandadoc_client.OAuth20AuthenticationApi

All URIs are relative to *https://api.pandadoc.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**access_token**](OAuth20AuthenticationApi.md#access_token) | **POST** /oauth2/access_token | Create/Refresh Access Token


# **access_token**
> OAuth2AccessTokenResponse access_token()

Create/Refresh Access Token

### Example

* Api Key Authentication (apiKey):
* OAuth Authentication (oauth2):

```python
import pandadoc_client
from pandadoc_client.api import o_auth_2_0_authentication_api
from pandadoc_client.model.o_auth2_access_token_response import OAuth2AccessTokenResponse
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
    api_instance = o_auth_2_0_authentication_api.OAuth20AuthenticationApi(api_client)
    grant_type = "refresh_token"  # str | This value must be set to `refresh_token`. (optional) if omitted the server will use the default value of "refresh_token"
    client_id = "479a3c7ba4a8d3cf28702"  # str | Client ID that is automatically generated after application creation in the Developer Dashboard. (optional)
    client_secret = "a66515d3caf9183b8cad3eee546bcba892b45b01"  # str | Client secret that is automatically generated after application creation in the Developer Dashboard. (optional)
    code = "a9a60d4dabb61ade665c712d2b41766e7bb9a2f9"  # str | `auth_code` from the server on the previous step (Authorize a PandaDoc User).  (optional)
    scope = "read+write"  # str | Requested permissions. Use `read+write` as our default value to send documents. (optional)
    refresh_token = "f61cc0cffd437c9a596f0acc8eb6f502a7a429d7"  # str | `refresh_token` you received and stored from the server when initially creating an `access_token`.  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create/Refresh Access Token
        api_response = api_instance.access_token(
            grant_type=grant_type,
            client_id=client_id,
            client_secret=client_secret,
            code=code,
            scope=scope,
            refresh_token=refresh_token,
        )
        pprint(api_response)
    except pandadoc_client.ApiException as e:
        print("Exception when calling OAuth20AuthenticationApi->access_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **grant_type** | **str**| This value must be set to &#x60;refresh_token&#x60;. | [optional] if omitted the server will use the default value of "refresh_token"
 **client_id** | **str**| Client ID that is automatically generated after application creation in the Developer Dashboard. | [optional]
 **client_secret** | **str**| Client secret that is automatically generated after application creation in the Developer Dashboard. | [optional]
 **code** | **str**| &#x60;auth_code&#x60; from the server on the previous step (Authorize a PandaDoc User).  | [optional]
 **scope** | **str**| Requested permissions. Use &#x60;read+write&#x60; as our default value to send documents. | [optional]
 **refresh_token** | **str**| &#x60;refresh_token&#x60; you received and stored from the server when initially creating an &#x60;access_token&#x60;.  | [optional]

### Return type

[**OAuth2AccessTokenResponse**](OAuth2AccessTokenResponse.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

