# pandadoc_client.CommunicationPreferencesApi

All URIs are relative to *https://api.pandadoc.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_recent_sms_opt_outs**](CommunicationPreferencesApi.md#list_recent_sms_opt_outs) | **GET** /public/v1/sms-opt-outs | Recent SMS Opt-out


# **list_recent_sms_opt_outs**
> ListSmsOptOutChangelogResponse list_recent_sms_opt_outs(timestamp_from=timestamp_from, timestamp_to=timestamp_to)

Recent SMS Opt-out

Retrieves a list of the most recent SMS opt-out changes for each phone numbers used in your workspace.

> 📘 You can filter results by time range using `timestamp_from` and `timestamp_to`.


### Example

* Api Key Authentication (apiKey):
* OAuth Authentication (oauth2):

```python
import pandadoc_client
from pandadoc_client.models.list_sms_opt_out_changelog_response import ListSmsOptOutChangelogResponse
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
    api_instance = pandadoc_client.CommunicationPreferencesApi(api_client)
    timestamp_from = '2025-01-28T00:00:00Z' # datetime | The start of the timestamp.   If no timestamp is provided, 1 hour before the current time will be used.  (optional)
    timestamp_to = '2025-01-28T23:59:59Z' # datetime | The end of the timestamp range.   If no timestamp is provided the current time will be used.  (optional)

    try:
        # Recent SMS Opt-out
        api_response = api_instance.list_recent_sms_opt_outs(timestamp_from=timestamp_from, timestamp_to=timestamp_to)
        print("The response of CommunicationPreferencesApi->list_recent_sms_opt_outs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommunicationPreferencesApi->list_recent_sms_opt_outs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp_from** | **datetime**| The start of the timestamp.   If no timestamp is provided, 1 hour before the current time will be used.  | [optional] 
 **timestamp_to** | **datetime**| The end of the timestamp range.   If no timestamp is provided the current time will be used.  | [optional] 

### Return type

[**ListSmsOptOutChangelogResponse**](ListSmsOptOutChangelogResponse.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of phone numbers, their SMS current opt-out statuses and timestamp of the last change. |  -  |
**400** | Bad Request |  -  |
**401** | Authentication error |  -  |
**403** | Permission error |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

