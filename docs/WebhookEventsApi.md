# pandadoc_client.WebhookEventsApi

All URIs are relative to *https://api.pandadoc.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**details_webhook_event**](WebhookEventsApi.md#details_webhook_event) | **GET** /public/v1/webhook-events/{id} | Webhook Event Details
[**list_webhook_event**](WebhookEventsApi.md#list_webhook_event) | **GET** /public/v1/webhook-events | List Webhook Events


# **details_webhook_event**
> WebhookEventDetailsResponse details_webhook_event(id)

Webhook Event Details

This operation fetches detailed information about a specific webhook event using its unique identifier.

### Example

* Api Key Authentication (apiKey):
* OAuth Authentication (oauth2):

```python
import pandadoc_client
from pandadoc_client.models.webhook_event_details_response import WebhookEventDetailsResponse
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
    api_instance = pandadoc_client.WebhookEventsApi(api_client)
    id = '8b61d111-5e0b-406d-a150-e8305fc7e97a' # str | Webhook event uuid.

    try:
        # Webhook Event Details
        api_response = api_instance.details_webhook_event(id)
        print("The response of WebhookEventsApi->details_webhook_event:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhookEventsApi->details_webhook_event: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Webhook event uuid. | 

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
**200** | Get webhook event by uuid. |  -  |
**401** | Authentication error |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_webhook_event**
> WebhookEventPageResponse list_webhook_event(count, page, since=since, to=to, type=type, http_status_code=http_status_code, error=error)

List Webhook Events

This operation retrieves a paginated list of all webhook events.

### Example

* Api Key Authentication (apiKey):
* OAuth Authentication (oauth2):

```python
import pandadoc_client
from pandadoc_client.models.webhook_event_error_enum import WebhookEventErrorEnum
from pandadoc_client.models.webhook_event_http_status_code_group_enum import WebhookEventHttpStatusCodeGroupEnum
from pandadoc_client.models.webhook_event_page_response import WebhookEventPageResponse
from pandadoc_client.models.webhook_event_trigger_enum import WebhookEventTriggerEnum
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
    api_instance = pandadoc_client.WebhookEventsApi(api_client)
    count = 10 # int | Specify how many event results to return.
    page = 1 # int | Specify which page of the dataset to return.
    since = '2022-06-01T00:00:00Z' # datetime | Return results where the event creation time is greater than or equal to this value. (optional)
    to = '2022-06-30T23:59:59Z' # datetime | Return results where the event creation time is less than this value. (optional)
    type = [pandadoc_client.WebhookEventTriggerEnum()] # List[WebhookEventTriggerEnum] | Returns results by the specified event types. (optional)
    http_status_code = [pandadoc_client.WebhookEventHttpStatusCodeGroupEnum()] # List[WebhookEventHttpStatusCodeGroupEnum] | Returns results with the specified HTTP status codes. (optional)
    error = [pandadoc_client.WebhookEventErrorEnum()] # List[WebhookEventErrorEnum] | Returns results with the following errors. (optional)

    try:
        # List Webhook Events
        api_response = api_instance.list_webhook_event(count, page, since=since, to=to, type=type, http_status_code=http_status_code, error=error)
        print("The response of WebhookEventsApi->list_webhook_event:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhookEventsApi->list_webhook_event: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **count** | **int**| Specify how many event results to return. | 
 **page** | **int**| Specify which page of the dataset to return. | 
 **since** | **datetime**| Return results where the event creation time is greater than or equal to this value. | [optional] 
 **to** | **datetime**| Return results where the event creation time is less than this value. | [optional] 
 **type** | [**List[WebhookEventTriggerEnum]**](WebhookEventTriggerEnum.md)| Returns results by the specified event types. | [optional] 
 **http_status_code** | [**List[WebhookEventHttpStatusCodeGroupEnum]**](WebhookEventHttpStatusCodeGroupEnum.md)| Returns results with the specified HTTP status codes. | [optional] 
 **error** | [**List[WebhookEventErrorEnum]**](WebhookEventErrorEnum.md)| Returns results with the following errors. | [optional] 

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
**200** | Page of webhook events. |  -  |
**401** | Authentication error |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

