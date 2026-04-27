# pandadoc_client.APILogsApi

All URIs are relative to *https://api.pandadoc.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**details_log**](APILogsApi.md#details_log) | **GET** /public/v1/logs/{id} | API Log Details
[**details_log_v2**](APILogsApi.md#details_log_v2) | **GET** /public/v2/logs/{id} | API Log Details
[**list_logs**](APILogsApi.md#list_logs) | **GET** /public/v1/logs | List API Log
[**list_logs_v2**](APILogsApi.md#list_logs_v2) | **GET** /public/v2/logs | List API Log


# **details_log**
> APILogDetailsResponse details_log(id)

API Log Details

Returns details of the specific API log event.

### Example

* Api Key Authentication (apiKey):
* OAuth Authentication (oauth2):

```python
import pandadoc_client
from pandadoc_client.models.api_log_details_response import APILogDetailsResponse
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
    api_instance = pandadoc_client.APILogsApi(api_client)
    id = 'AZC86i5PYKMjQjMMMw9e' # str | Log event id.

    try:
        # API Log Details
        api_response = api_instance.details_log(id)
        print("The response of APILogsApi->details_log:\n")
        pprint(api_response)
    except Exception as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **details_log_v2**
> APILogDetailsResponse details_log_v2(id)

API Log Details

Returns details of the specific API log event.

### Example

* Api Key Authentication (apiKey):
* OAuth Authentication (oauth2):

```python
import pandadoc_client
from pandadoc_client.models.api_log_details_response import APILogDetailsResponse
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
    api_instance = pandadoc_client.APILogsApi(api_client)
    id = 'AZC86i5PYKMjQjMMMw9e' # str | Log event id.

    try:
        # API Log Details
        api_response = api_instance.details_log_v2(id)
        print("The response of APILogsApi->details_log_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling APILogsApi->details_log_v2: %s\n" % e)
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
**400** | Bad Request error |  -  |
**401** | Authentication error |  -  |
**404** | Not found error |  -  |
**429** | Too many requests error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_logs**
> APILogListResponse list_logs(since=since, to=to, count=count, page=page, statuses=statuses, methods=methods, search=search, environment_type=environment_type)

List API Log

Get the list of all logs within the selected workspace.\ Optionally filter by date, page, and `#` of items per page.

### Example

* Api Key Authentication (apiKey):
* OAuth Authentication (oauth2):

```python
import pandadoc_client
from pandadoc_client.models.api_log_list_response import APILogListResponse
from pandadoc_client.models.api_log_environment_type_enum import ApiLogEnvironmentTypeEnum
from pandadoc_client.models.api_log_method_enum import ApiLogMethodEnum
from pandadoc_client.models.api_log_status_enum import ApiLogStatusEnum
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
    api_instance = pandadoc_client.APILogsApi(api_client)
    since = '-90d' # str | Determines a point in time from which logs should be fetched. Either a specific ISO 8601 datetime or a relative identifier such as \"-90d\" (for past 90 days). (optional) (default to '-90d')
    to = 'now' # str | Determines a point in time from which logs should be fetched. Either a specific ISO 8601 datetime or a relative identifier such as \"-10d\" (for past 10 days) or a special \"now\" value. (optional)
    count = 100 # int | The amount of items on each page. The total number of accessible items (`count × page`) must not exceed 10,000. (optional) (default to 100)
    page = 1 # int | Returns page of the results by number. The total number of accessible items (`count × page`) must not exceed 10,000. (optional) (default to 1)
    statuses = [pandadoc_client.ApiLogStatusEnum()] # List[ApiLogStatusEnum] | Returns only the predefined status codes. (optional)
    methods = [pandadoc_client.ApiLogMethodEnum()] # List[ApiLogMethodEnum] | Returns only the predefined HTTP methods. Allows GET, POST, PUT, PATCH, and DELETE. (optional)
    search = 'documents/hryJY9mqYZHjQCYQuSjRQg/send' # str | Returns the results containing a string. (optional)
    environment_type = pandadoc_client.ApiLogEnvironmentTypeEnum() # ApiLogEnvironmentTypeEnum | Returns logs for production/sandbox. (optional)

    try:
        # List API Log
        api_response = api_instance.list_logs(since=since, to=to, count=count, page=page, statuses=statuses, methods=methods, search=search, environment_type=environment_type)
        print("The response of APILogsApi->list_logs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling APILogsApi->list_logs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **since** | **str**| Determines a point in time from which logs should be fetched. Either a specific ISO 8601 datetime or a relative identifier such as \&quot;-90d\&quot; (for past 90 days). | [optional] [default to &#39;-90d&#39;]
 **to** | **str**| Determines a point in time from which logs should be fetched. Either a specific ISO 8601 datetime or a relative identifier such as \&quot;-10d\&quot; (for past 10 days) or a special \&quot;now\&quot; value. | [optional] 
 **count** | **int**| The amount of items on each page. The total number of accessible items (&#x60;count × page&#x60;) must not exceed 10,000. | [optional] [default to 100]
 **page** | **int**| Returns page of the results by number. The total number of accessible items (&#x60;count × page&#x60;) must not exceed 10,000. | [optional] [default to 1]
 **statuses** | [**List[ApiLogStatusEnum]**](ApiLogStatusEnum.md)| Returns only the predefined status codes. | [optional] 
 **methods** | [**List[ApiLogMethodEnum]**](ApiLogMethodEnum.md)| Returns only the predefined HTTP methods. Allows GET, POST, PUT, PATCH, and DELETE. | [optional] 
 **search** | **str**| Returns the results containing a string. | [optional] 
 **environment_type** | [**ApiLogEnvironmentTypeEnum**](.md)| Returns logs for production/sandbox. | [optional] 

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_logs_v2**
> APILogListResponse list_logs_v2(since=since, to=to, count=count, page=page, statuses=statuses, methods=methods, search=search, environment_type=environment_type)

List API Log

Get the list of all logs within the selected workspace.\ Optionally filter by date, page, and `#` of items per page.

### Example

* Api Key Authentication (apiKey):
* OAuth Authentication (oauth2):

```python
import pandadoc_client
from pandadoc_client.models.api_log_list_response import APILogListResponse
from pandadoc_client.models.api_log_environment_type_enum import ApiLogEnvironmentTypeEnum
from pandadoc_client.models.api_log_method_enum import ApiLogMethodEnum
from pandadoc_client.models.api_log_status_enum import ApiLogStatusEnum
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
    api_instance = pandadoc_client.APILogsApi(api_client)
    since = '-90d' # str | Determines a point in time from which logs should be fetched. Either a specific ISO 8601 datetime or a relative identifier such as \"-90d\" (for past 90 days). (optional) (default to '-90d')
    to = 'now' # str | Determines a point in time from which logs should be fetched. Either a specific ISO 8601 datetime or a relative identifier such as \"-10d\" (for past 10 days) or a special \"now\" value. (optional)
    count = 100 # int | The amount of items on each page. The total number of accessible items (`count × page`) must not exceed 10,000. (optional) (default to 100)
    page = 1 # int | Returns page of the results by number. The total number of accessible items (`count × page`) must not exceed 10,000. (optional) (default to 1)
    statuses = [pandadoc_client.ApiLogStatusEnum()] # List[ApiLogStatusEnum] | Returns only the predefined status codes. (optional)
    methods = [pandadoc_client.ApiLogMethodEnum()] # List[ApiLogMethodEnum] | Returns only the predefined HTTP methods. Allows GET, POST, PUT, PATCH, and DELETE. (optional)
    search = 'documents/hryJY9mqYZHjQCYQuSjRQg/send' # str | Returns the results containing a string. (optional)
    environment_type = pandadoc_client.ApiLogEnvironmentTypeEnum() # ApiLogEnvironmentTypeEnum | Returns logs for production/sandbox. (optional)

    try:
        # List API Log
        api_response = api_instance.list_logs_v2(since=since, to=to, count=count, page=page, statuses=statuses, methods=methods, search=search, environment_type=environment_type)
        print("The response of APILogsApi->list_logs_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling APILogsApi->list_logs_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **since** | **str**| Determines a point in time from which logs should be fetched. Either a specific ISO 8601 datetime or a relative identifier such as \&quot;-90d\&quot; (for past 90 days). | [optional] [default to &#39;-90d&#39;]
 **to** | **str**| Determines a point in time from which logs should be fetched. Either a specific ISO 8601 datetime or a relative identifier such as \&quot;-10d\&quot; (for past 10 days) or a special \&quot;now\&quot; value. | [optional] 
 **count** | **int**| The amount of items on each page. The total number of accessible items (&#x60;count × page&#x60;) must not exceed 10,000. | [optional] [default to 100]
 **page** | **int**| Returns page of the results by number. The total number of accessible items (&#x60;count × page&#x60;) must not exceed 10,000. | [optional] [default to 1]
 **statuses** | [**List[ApiLogStatusEnum]**](ApiLogStatusEnum.md)| Returns only the predefined status codes. | [optional] 
 **methods** | [**List[ApiLogMethodEnum]**](ApiLogMethodEnum.md)| Returns only the predefined HTTP methods. Allows GET, POST, PUT, PATCH, and DELETE. | [optional] 
 **search** | **str**| Returns the results containing a string. | [optional] 
 **environment_type** | [**ApiLogEnvironmentTypeEnum**](.md)| Returns logs for production/sandbox. | [optional] 

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
**400** | Bad Request error |  -  |
**401** | Authentication error |  -  |
**429** | Too many requests error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

