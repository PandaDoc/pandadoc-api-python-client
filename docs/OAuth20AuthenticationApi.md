# pandadoc_client.OAuth20AuthenticationApi

All URIs are relative to *https://api.pandadoc.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**access_token**](OAuth20AuthenticationApi.md#access_token) | **POST** /oauth2/access_token | Create/Refresh Access Token


# **access_token**
> OAuth2AccessTokenResponse access_token(grant_type=grant_type, client_id=client_id, client_secret=client_secret, code=code, scope=scope, refresh_token=refresh_token)

Create/Refresh Access Token

Create or refresh an access token to make requests on behalf of a user. This endpoint is used to obtain an `access_token` and `refresh_token` for the first time, and to refresh the `access_token` when it expires.
This endpoint is part of OAuth 2.0 implementation. You need to configure OAuth App to obtain `client_id` and `client_secret`. Read more about [OAuth 2.0 implementation](https://developers.pandadoc.com/reference/authentication-process).
Make sure you're sending the header `Content-Type: application/x-www-form-urlencoded`. 

## Create Access Token
As a result of the OAuth 2.0 user authentication process, you should get a `code` that can be exchanged for an `access_token`. Use this endpoint to do this exchange, and to refresh the token later.

> 🚧 Invalid Grant?
> 
> If you receive an `invalid grant` response it is likely because you used the same `code` more than once from the [Authorize a PandaDoc User](ref:authorize-a-user) step above. The `code` parameter is generated for one-time use. A new `code` value must be generated if you wish to change API users, permissions, or simply generate a new `code` value for the same PandaDoc user.

> 📘 expires_in
> 
> `expires_in` is based in seconds. Currently, a token expires in 31535999 seconds = 1 year.

## Refresh Access Token
Eventually, `access_token` expires and accessing an API method returns **401 unauthorized**. Your application needs to refresh the OAuth2 token with the stored `refresh_token` returned when initially creating an access token.

Once refreshed, calls on behalf of the originally authorized user can resume immediately. Use the newly returned `access_token` for all future API requests.

> 🚧 Invalid Grant?
> 
> If you receive an `invalid grant` response, it is likely because your `refresh_token` is invalid.


### Example


```python
import pandadoc_client
from pandadoc_client.models.o_auth2_access_token_response import OAuth2AccessTokenResponse
from pandadoc_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.pandadoc.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pandadoc_client.Configuration(
    host = "https://api.pandadoc.com"
)


# Enter a context with an instance of the API client
with pandadoc_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pandadoc_client.OAuth20AuthenticationApi(api_client)
    grant_type = 'refresh_token' # str | This value must be set to `refresh_token`. (optional) (default to 'refresh_token')
    client_id = 'client_id_example' # str | Client ID that is automatically generated after application creation in the Developer Dashboard. (optional)
    client_secret = 'client_secret_example' # str | Client secret that is automatically generated after application creation in the Developer Dashboard. (optional)
    code = 'code_example' # str | `auth_code` from the server on the previous step (Authorize a PandaDoc User).  (optional)
    scope = 'scope_example' # str | Requested permissions. Use `read+write` as our default value to send documents. (optional)
    refresh_token = 'refresh_token_example' # str | `refresh_token` you received and stored from the server when initially creating an `access_token`.  (optional)

    try:
        # Create/Refresh Access Token
        api_response = api_instance.access_token(grant_type=grant_type, client_id=client_id, client_secret=client_secret, code=code, scope=scope, refresh_token=refresh_token)
        print("The response of OAuth20AuthenticationApi->access_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OAuth20AuthenticationApi->access_token: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **grant_type** | **str**| This value must be set to &#x60;refresh_token&#x60;. | [optional] [default to &#39;refresh_token&#39;]
 **client_id** | **str**| Client ID that is automatically generated after application creation in the Developer Dashboard. | [optional] 
 **client_secret** | **str**| Client secret that is automatically generated after application creation in the Developer Dashboard. | [optional] 
 **code** | **str**| &#x60;auth_code&#x60; from the server on the previous step (Authorize a PandaDoc User).  | [optional] 
 **scope** | **str**| Requested permissions. Use &#x60;read+write&#x60; as our default value to send documents. | [optional] 
 **refresh_token** | **str**| &#x60;refresh_token&#x60; you received and stored from the server when initially creating an &#x60;access_token&#x60;.  | [optional] 

### Return type

[**OAuth2AccessTokenResponse**](OAuth2AccessTokenResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

