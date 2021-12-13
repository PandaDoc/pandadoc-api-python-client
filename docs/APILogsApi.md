# pandadoc_client.APILogsApi

All URIs are relative to *https://api.pandadoc.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**details_log**](APILogsApi.md#details_log) | **GET** /public/v1/logs/{id} | Details API Log
[**list_logs**](APILogsApi.md#list_logs) | **GET** /public/v1/logs | List API Log


# **details_log**
> APILogDetailsResponse details_log(id)

Details API Log

Returns details of the specific API log event.

### Example

* Api Key Authentication (apiKey):
* OAuth Authentication (oauth2):

```python
import pandadoc_client
from pandadoc_client.api import api_logs_api
from pandadoc_client.model.api_log_details_response import APILogDetailsResponse
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
    api_instance = api_logs_api.APILogsApi(api_client)
    id = "AXp2jrHMK2MKv_lRqmQ"  # str | Log event id.

    # example passing only required values which don't have defaults set
    try:
        # Details API Log
        api_response = api_instance.details_log(id)
        pprint(api_response)
    except pandadoc_client.ApiException as e:
        print("Exception when calling APILogsApi->details_log: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Log event id. |

### Return type

[**APILogDetailsResponse**](APILogDetailsResponse.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Authentication error |  -  |
**404** | Not found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **list_logs**
> APILogListResponse list_logs()

List API Log

Get the list of all logs within the selected workspace. Optionally filter by date, page, and `#` of items per page.

### Example

* Api Key Authentication (apiKey):
* OAuth Authentication (oauth2):

```python
import pandadoc_client
from pandadoc_client.api import api_logs_api
from pandadoc_client.model.api_log_list_response import APILogListResponse
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
    api_instance = api_logs_api.APILogsApi(api_client)
    since = "-7d"  # str | Determines a point in time from which logs should be fetched. Either a specific ISO 8601 datetime or a relative identifier such as \"-90d\" (for past 90 days). (optional)
    to = "now"  # str | Determines a point in time from which logs should be fetched. Either a specific ISO 8601 datetime or a relative identifier such as \"-10d\" (for past 10 days) or a special \"now\" value. (optional)
    count = 10  # int | The amount of items on each page. (optional)
    page = 1  # int | Page number of the results returned. (optional)
    statuses = [400,500]  # [int] | Returns only the predefined status codes. Allows 1xx, 2xx, 3xx, 4xx, and 5xx. (optional)
    methods = ["GET","POST"]  # [str] | Returns only the predefined HTTP methods. Allows GET, POST, PUT, PATCH, and DELETE. (optional)
    search = "documents/hryJY9mqYZHjQCYQuSjRQg/send"  # str | Returns the results containing a string. (optional)
    environment_type = "PRODUCTION"  # str | Returns logs for production/sandbox. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List API Log
        api_response = api_instance.list_logs(
            since=since,
            to=to,
            count=count,
            page=page,
            statuses=statuses,
            methods=methods,
            search=search,
            environment_type=environment_type,
        )
        pprint(api_response)
    except pandadoc_client.ApiException as e:
        print("Exception when calling APILogsApi->list_logs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **since** | **str**| Determines a point in time from which logs should be fetched. Either a specific ISO 8601 datetime or a relative identifier such as \&quot;-90d\&quot; (for past 90 days). | [optional]
 **to** | **str**| Determines a point in time from which logs should be fetched. Either a specific ISO 8601 datetime or a relative identifier such as \&quot;-10d\&quot; (for past 10 days) or a special \&quot;now\&quot; value. | [optional]
 **count** | **int**| The amount of items on each page. | [optional]
 **page** | **int**| Page number of the results returned. | [optional]
 **statuses** | **[int]**| Returns only the predefined status codes. Allows 1xx, 2xx, 3xx, 4xx, and 5xx. | [optional]
 **methods** | **[str]**| Returns only the predefined HTTP methods. Allows GET, POST, PUT, PATCH, and DELETE. | [optional]
 **search** | **str**| Returns the results containing a string. | [optional]
 **environment_type** | **str**| Returns logs for production/sandbox. | [optional]

### Return type

[**APILogListResponse**](APILogListResponse.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Authentication error |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

