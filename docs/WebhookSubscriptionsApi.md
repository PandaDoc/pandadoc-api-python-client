# pandadoc_client.WebhookSubscriptionsApi

All URIs are relative to *https://api.pandadoc.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_webhook_subscription**](WebhookSubscriptionsApi.md#create_webhook_subscription) | **POST** /public/v1/webhook-subscriptions | Create webhook subscription
[**delete_webhook_subscription**](WebhookSubscriptionsApi.md#delete_webhook_subscription) | **DELETE** /public/v1/webhook-subscriptions/{id} | Delete webhook subscription
[**details_webhook_subscription**](WebhookSubscriptionsApi.md#details_webhook_subscription) | **GET** /public/v1/webhook-subscriptions/{id} | Get webhook subscription by uuid
[**list_webhook_subscriptions**](WebhookSubscriptionsApi.md#list_webhook_subscriptions) | **GET** /public/v1/webhook-subscriptions | Get all webhook subscriptions
[**update_webhook_subscription**](WebhookSubscriptionsApi.md#update_webhook_subscription) | **PATCH** /public/v1/webhook-subscriptions/{id} | Update webhook subscription
[**update_webhook_subscription_shared_key**](WebhookSubscriptionsApi.md#update_webhook_subscription_shared_key) | **PATCH** /public/v1/webhook-subscriptions/{id}/shared-key | Regenerate webhook subscription shared key


# **create_webhook_subscription**
> WebhookSubscriptionItemResponse create_webhook_subscription(webhook_subscription_create_request)

Create webhook subscription

### Example

* Api Key Authentication (apiKey):
* OAuth Authentication (oauth2):

```python
import pandadoc_client
from pandadoc_client.api import webhook_subscriptions_api
from pandadoc_client.model.webhook_subscription_create_request import WebhookSubscriptionCreateRequest
from pandadoc_client.model.webhook_subscription_item_response import WebhookSubscriptionItemResponse
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
    api_instance = webhook_subscriptions_api.WebhookSubscriptionsApi(api_client)
    webhook_subscription_create_request = WebhookSubscriptionCreateRequest(
        name="My Subscription",
        url="https://example.com",
        payload=[
            WebhookSubscriptionPayloadEnum("pricing"),
        ],
        triggers=[
            WebhookSubscriptionTriggerEnum("document_state_changed"),
        ],
    )  # WebhookSubscriptionCreateRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Create webhook subscription
        api_response = api_instance.create_webhook_subscription(webhook_subscription_create_request)
        pprint(api_response)
    except pandadoc_client.ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **delete_webhook_subscription**
> delete_webhook_subscription(id)

Delete webhook subscription

### Example

* Api Key Authentication (apiKey):
* OAuth Authentication (oauth2):

```python
import pandadoc_client
from pandadoc_client.api import webhook_subscriptions_api
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
    api_instance = webhook_subscriptions_api.WebhookSubscriptionsApi(api_client)
    id = "id_example"  # str | Webhook subscription uuid

    # example passing only required values which don't have defaults set
    try:
        # Delete webhook subscription
        api_instance.delete_webhook_subscription(id)
    except pandadoc_client.ApiException as e:
        print("Exception when calling WebhookSubscriptionsApi->delete_webhook_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Webhook subscription uuid |

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **details_webhook_subscription**
> WebhookSubscriptionItemResponse details_webhook_subscription(id)

Get webhook subscription by uuid

### Example

* Api Key Authentication (apiKey):
* OAuth Authentication (oauth2):

```python
import pandadoc_client
from pandadoc_client.api import webhook_subscriptions_api
from pandadoc_client.model.webhook_subscription_item_response import WebhookSubscriptionItemResponse
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
    api_instance = webhook_subscriptions_api.WebhookSubscriptionsApi(api_client)
    id = "id_example"  # str | Webhook subscription uuid

    # example passing only required values which don't have defaults set
    try:
        # Get webhook subscription by uuid
        api_response = api_instance.details_webhook_subscription(id)
        pprint(api_response)
    except pandadoc_client.ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **list_webhook_subscriptions**
> WebhookSubscriptionListResponse list_webhook_subscriptions()

Get all webhook subscriptions

### Example

* Api Key Authentication (apiKey):
* OAuth Authentication (oauth2):

```python
import pandadoc_client
from pandadoc_client.api import webhook_subscriptions_api
from pandadoc_client.model.webhook_subscription_list_response import WebhookSubscriptionListResponse
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
    api_instance = webhook_subscriptions_api.WebhookSubscriptionsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get all webhook subscriptions
        api_response = api_instance.list_webhook_subscriptions()
        pprint(api_response)
    except pandadoc_client.ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **update_webhook_subscription**
> WebhookSubscriptionItemResponse update_webhook_subscription(id, webhook_subscription_patch_request)

Update webhook subscription

### Example

* Api Key Authentication (apiKey):
* OAuth Authentication (oauth2):

```python
import pandadoc_client
from pandadoc_client.api import webhook_subscriptions_api
from pandadoc_client.model.webhook_subscription_patch_request import WebhookSubscriptionPatchRequest
from pandadoc_client.model.webhook_subscription_item_response import WebhookSubscriptionItemResponse
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
    api_instance = webhook_subscriptions_api.WebhookSubscriptionsApi(api_client)
    id = "id_example"  # str | Webhook subscription uuid
    webhook_subscription_patch_request = WebhookSubscriptionPatchRequest(
        name="My Subscription",
        url="https://example.com",
        active=True,
        payload=[
            WebhookSubscriptionPayloadEnum("pricing"),
        ],
        triggers=[
            WebhookSubscriptionTriggerEnum("document_state_changed"),
        ],
    )  # WebhookSubscriptionPatchRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Update webhook subscription
        api_response = api_instance.update_webhook_subscription(id, webhook_subscription_patch_request)
        pprint(api_response)
    except pandadoc_client.ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **update_webhook_subscription_shared_key**
> WebhookSubscriptionSharedKeyResponse update_webhook_subscription_shared_key(id)

Regenerate webhook subscription shared key

### Example

* Api Key Authentication (apiKey):
* OAuth Authentication (oauth2):

```python
import pandadoc_client
from pandadoc_client.api import webhook_subscriptions_api
from pandadoc_client.model.webhook_subscription_shared_key_response import WebhookSubscriptionSharedKeyResponse
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
    api_instance = webhook_subscriptions_api.WebhookSubscriptionsApi(api_client)
    id = "id_example"  # str | Webhook subscription uuid

    # example passing only required values which don't have defaults set
    try:
        # Regenerate webhook subscription shared key
        api_response = api_instance.update_webhook_subscription_shared_key(id)
        pprint(api_response)
    except pandadoc_client.ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

