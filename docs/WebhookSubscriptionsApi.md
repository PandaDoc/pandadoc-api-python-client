# pandadoc_client.WebhookSubscriptionsApi

All URIs are relative to *https://api.pandadoc.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_webhook_subscription**](WebhookSubscriptionsApi.md#create_webhook_subscription) | **POST** /public/v1/webhook-subscriptions | Create Webhook Subscription
[**delete_webhook_subscription**](WebhookSubscriptionsApi.md#delete_webhook_subscription) | **DELETE** /public/v1/webhook-subscriptions/{id} | Delete Webhook Subscription
[**details_webhook_subscription**](WebhookSubscriptionsApi.md#details_webhook_subscription) | **GET** /public/v1/webhook-subscriptions/{id} | Webhook Subscription Details
[**list_webhook_subscriptions**](WebhookSubscriptionsApi.md#list_webhook_subscriptions) | **GET** /public/v1/webhook-subscriptions | List Webhook Subscriptions
[**update_webhook_subscription**](WebhookSubscriptionsApi.md#update_webhook_subscription) | **PATCH** /public/v1/webhook-subscriptions/{id} | Update Webhook Subscription
[**update_webhook_subscription_shared_key**](WebhookSubscriptionsApi.md#update_webhook_subscription_shared_key) | **PATCH** /public/v1/webhook-subscriptions/{id}/shared-key | Update Webhook Subscription Shared Key


# **create_webhook_subscription**
> WebhookSubscriptionItemResponse create_webhook_subscription(webhook_subscription_create_request)

Create Webhook Subscription

This operation creates a new webhook subscription by specifying its details.

### Example

* Api Key Authentication (apiKey):
* OAuth Authentication (oauth2):

```python
import pandadoc_client
from pandadoc_client.models.webhook_subscription_create_request import WebhookSubscriptionCreateRequest
from pandadoc_client.models.webhook_subscription_item_response import WebhookSubscriptionItemResponse
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
    api_instance = pandadoc_client.WebhookSubscriptionsApi(api_client)
    webhook_subscription_create_request = {"name":"PandaDoc","url":"webhooks_subscription_url","active":true,"payload":["fields","products","metadata","tokens","pricing"],"triggers":["document_deleted","recipient_completed","document_updated","document_state_changed","document_creation_failed"]} # WebhookSubscriptionCreateRequest | 

    try:
        # Create Webhook Subscription
        api_response = api_instance.create_webhook_subscription(webhook_subscription_create_request)
        print("The response of WebhookSubscriptionsApi->create_webhook_subscription:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhookSubscriptionsApi->create_webhook_subscription: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhook_subscription_create_request** | [**WebhookSubscriptionCreateRequest**](WebhookSubscriptionCreateRequest.md)|  | 

### Return type

[**WebhookSubscriptionItemResponse**](WebhookSubscriptionItemResponse.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Webhook subscription created |  -  |
**400** | Bad Request |  -  |
**401** | Authentication error |  -  |
**403** | Permission error |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_webhook_subscription**
> delete_webhook_subscription(id)

Delete Webhook Subscription

This operation deletes a specific webhook subscription identified by its UUID.

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
    api_instance = pandadoc_client.WebhookSubscriptionsApi(api_client)
    id = 'd173751d-0057-4d5c-ab75-49a670a4ca68' # str | Webhook subscription uuid.

    try:
        # Delete Webhook Subscription
        api_instance.delete_webhook_subscription(id)
    except Exception as e:
        print("Exception when calling WebhookSubscriptionsApi->delete_webhook_subscription: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Webhook subscription uuid. | 

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
**204** | Webhook subscription removed |  -  |
**401** | Authentication error |  -  |
**403** | Permission error |  -  |
**404** | Not found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **details_webhook_subscription**
> WebhookSubscriptionItemResponse details_webhook_subscription(id)

Webhook Subscription Details

Get webhook subscription by uuid


### Example

* Api Key Authentication (apiKey):
* OAuth Authentication (oauth2):

```python
import pandadoc_client
from pandadoc_client.models.webhook_subscription_item_response import WebhookSubscriptionItemResponse
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
    api_instance = pandadoc_client.WebhookSubscriptionsApi(api_client)
    id = '4fb6506c-02a0-427e-b445-b9e9ff0c822f' # str | Webhook subscription uuid

    try:
        # Webhook Subscription Details
        api_response = api_instance.details_webhook_subscription(id)
        print("The response of WebhookSubscriptionsApi->details_webhook_subscription:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhookSubscriptionsApi->details_webhook_subscription: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Webhook subscription uuid | 

### Return type

[**WebhookSubscriptionItemResponse**](WebhookSubscriptionItemResponse.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get webhook subscription by uuid |  -  |
**401** | Authentication error |  -  |
**403** | Permission error |  -  |
**404** | Not found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_webhook_subscriptions**
> WebhookSubscriptionListResponse list_webhook_subscriptions()

List Webhook Subscriptions

This operation fetches a paginated list of webhook subscriptions.

### Example

* Api Key Authentication (apiKey):
* OAuth Authentication (oauth2):

```python
import pandadoc_client
from pandadoc_client.models.webhook_subscription_list_response import WebhookSubscriptionListResponse
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
    api_instance = pandadoc_client.WebhookSubscriptionsApi(api_client)

    try:
        # List Webhook Subscriptions
        api_response = api_instance.list_webhook_subscriptions()
        print("The response of WebhookSubscriptionsApi->list_webhook_subscriptions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhookSubscriptionsApi->list_webhook_subscriptions: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**WebhookSubscriptionListResponse**](WebhookSubscriptionListResponse.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List webhook subscriptions |  -  |
**401** | Authentication error |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_webhook_subscription**
> WebhookSubscriptionItemResponse update_webhook_subscription(id, webhook_subscription_patch_request)

Update Webhook Subscription

This operation updates the details of a webhook subscription.

### Example

* Api Key Authentication (apiKey):
* OAuth Authentication (oauth2):

```python
import pandadoc_client
from pandadoc_client.models.webhook_subscription_item_response import WebhookSubscriptionItemResponse
from pandadoc_client.models.webhook_subscription_patch_request import WebhookSubscriptionPatchRequest
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
    api_instance = pandadoc_client.WebhookSubscriptionsApi(api_client)
    id = 'd173751d-0057-4d5c-ab75-49a670a4ca68' # str | Webhook subscription uuid
    webhook_subscription_patch_request = {"name":"PandaDoc","url":"https://pandadoc.com/webhooks","active":true,"payload":["fields","products","metadata","tokens","pricing"],"triggers":["document_deleted","recipient_completed","document_updated","document_state_changed","document_creation_failed"]} # WebhookSubscriptionPatchRequest | 

    try:
        # Update Webhook Subscription
        api_response = api_instance.update_webhook_subscription(id, webhook_subscription_patch_request)
        print("The response of WebhookSubscriptionsApi->update_webhook_subscription:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhookSubscriptionsApi->update_webhook_subscription: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Webhook subscription uuid | 
 **webhook_subscription_patch_request** | [**WebhookSubscriptionPatchRequest**](WebhookSubscriptionPatchRequest.md)|  | 

### Return type

[**WebhookSubscriptionItemResponse**](WebhookSubscriptionItemResponse.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Webhook subscription updated |  -  |
**400** | Bad Request |  -  |
**401** | Authentication error |  -  |
**403** | Permission error |  -  |
**404** | Not found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_webhook_subscription_shared_key**
> WebhookSubscriptionSharedKeyResponse update_webhook_subscription_shared_key(id)

Update Webhook Subscription Shared Key

This operation regenerates the shared key for a specific webhook subscription identified by its UUID.

### Example

* Api Key Authentication (apiKey):
* OAuth Authentication (oauth2):

```python
import pandadoc_client
from pandadoc_client.models.webhook_subscription_shared_key_response import WebhookSubscriptionSharedKeyResponse
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
    api_instance = pandadoc_client.WebhookSubscriptionsApi(api_client)
    id = 'd173751d-0057-4d5c-ab75-49a670a4ca68' # str | Webhook subscription uuid

    try:
        # Update Webhook Subscription Shared Key
        api_response = api_instance.update_webhook_subscription_shared_key(id)
        print("The response of WebhookSubscriptionsApi->update_webhook_subscription_shared_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhookSubscriptionsApi->update_webhook_subscription_shared_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Webhook subscription uuid | 

### Return type

[**WebhookSubscriptionSharedKeyResponse**](WebhookSubscriptionSharedKeyResponse.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Webhook subscription shared key regenerated |  -  |
**401** | Authentication error |  -  |
**403** | Permission error |  -  |
**404** | Not found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

