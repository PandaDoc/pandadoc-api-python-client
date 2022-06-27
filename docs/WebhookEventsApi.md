# pandadoc_client.WebhookEventsApi

All URIs are relative to *https://api.pandadoc.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**details_webhook_event**](WebhookEventsApi.md#details_webhook_event) | **GET** /public/v1/webhook-events/{id} | Get webhook event by uuid
[**list_webhook_event**](WebhookEventsApi.md#list_webhook_event) | **GET** /public/v1/webhook-events | Get webhook event page


# **details_webhook_event**
> WebhookEventDetailsResponse details_webhook_event(id)

Get webhook event by uuid

### Example

* Api Key Authentication (apiKey):
* OAuth Authentication (oauth2):

```python
import pandadoc_client
from pandadoc_client.api import webhook_events_api
from pandadoc_client.model.webhook_event_details_response import WebhookEventDetailsResponse
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
    api_instance = webhook_events_api.WebhookEventsApi(api_client)
    id = "id_example"  # str | Webhook event uuid

    # example passing only required values which don't have defaults set
    try:
        # Get webhook event by uuid
        api_response = api_instance.details_webhook_event(id)
        pprint(api_response)
    except pandadoc_client.ApiException as e:
        print("Exception when calling WebhookEventsApi->details_webhook_event: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Webhook event uuid |

### Return type

[**WebhookEventDetailsResponse**](WebhookEventDetailsResponse.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get webhook event by uuid |  -  |
**401** | Authentication error |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **list_webhook_event**
> WebhookEventPageResponse list_webhook_event(count, page)

Get webhook event page

### Example

* Api Key Authentication (apiKey):
* OAuth Authentication (oauth2):

```python
import pandadoc_client
from pandadoc_client.api import webhook_events_api
from pandadoc_client.model.webhook_event_trigger_enum import WebhookEventTriggerEnum
from pandadoc_client.model.webhook_event_page_response import WebhookEventPageResponse
from pandadoc_client.model.webhook_event_http_status_code_group_enum import WebhookEventHttpStatusCodeGroupEnum
from pandadoc_client.model.webhook_event_error_enum import WebhookEventErrorEnum
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
    api_instance = webhook_events_api.WebhookEventsApi(api_client)
    count = 0  # int | Number of element in page
    page = 0  # int | Page number
    since = dateutil_parser('1970-01-01T00:00:00.00Z')  # datetime | Filter option: all events from specified timestamp (optional)
    to = dateutil_parser('1970-01-01T00:00:00.00Z')  # datetime | Filter option: all events up to specified timestamp (optional)
    type = [
        WebhookEventTriggerEnum("document_state_changed"),
    ]  # [WebhookEventTriggerEnum] | Filter option: all events of type (optional)
    http_status_code = [
        WebhookEventHttpStatusCodeGroupEnum(400),
    ]  # [WebhookEventHttpStatusCodeGroupEnum] | Filter option: all events of http status code (optional)
    error = [
        WebhookEventErrorEnum("TIMEOUT_ERROR"),
    ]  # [WebhookEventErrorEnum] | Filter option: all events with following error (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get webhook event page
        api_response = api_instance.list_webhook_event(count, page)
        pprint(api_response)
    except pandadoc_client.ApiException as e:
        print("Exception when calling WebhookEventsApi->list_webhook_event: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get webhook event page
        api_response = api_instance.list_webhook_event(
            count,
            page,
            since=since,
            to=to,
            type=type,
            http_status_code=http_status_code,
            error=error,
        )
        pprint(api_response)
    except pandadoc_client.ApiException as e:
        print("Exception when calling WebhookEventsApi->list_webhook_event: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **count** | **int**| Number of element in page |
 **page** | **int**| Page number |
 **since** | **datetime**| Filter option: all events from specified timestamp | [optional]
 **to** | **datetime**| Filter option: all events up to specified timestamp | [optional]
 **type** | [**[WebhookEventTriggerEnum]**](WebhookEventTriggerEnum.md)| Filter option: all events of type | [optional]
 **http_status_code** | [**[WebhookEventHttpStatusCodeGroupEnum]**](WebhookEventHttpStatusCodeGroupEnum.md)| Filter option: all events of http status code | [optional]
 **error** | [**[WebhookEventErrorEnum]**](WebhookEventErrorEnum.md)| Filter option: all events with following error | [optional]

### Return type

[**WebhookEventPageResponse**](WebhookEventPageResponse.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Page of webhook events |  -  |
**401** | Authentication error |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

