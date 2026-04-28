# pandadoc_client.FormsApi

All URIs are relative to *https://api.pandadoc.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_form**](FormsApi.md#list_form) | **GET** /public/v1/forms | List Forms


# **list_form**
> FormListResponse list_form(count=count, page=page, status=status, order_by=order_by, asc=asc, name=name)

List Forms

Retrieve a paginated list of forms with optional filtering and sorting options.

### Example

* Api Key Authentication (apiKey):
* OAuth Authentication (oauth2):

```python
import pandadoc_client
from pandadoc_client.models.form_list_response import FormListResponse
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
    api_instance = pandadoc_client.FormsApi(api_client)
    count = 10 # int | Specify how many forms to return. Default is 50 forms, maximum is 100 forms. (optional)
    page = 1 # int | Specify which page of the dataset to return. (optional)
    status = ['[\"draft\",\"active\"]'] # List[str] | Specify which status of the forms dataset to return. (optional)
    order_by = 'name' # str | Specify the form dataset order to return. (optional)
    asc = true # bool | Specify sorting the result-set in ascending or descending order. (optional)
    name = 'New Form' # str | Specify the form name. (optional)

    try:
        # List Forms
        api_response = api_instance.list_form(count=count, page=page, status=status, order_by=order_by, asc=asc, name=name)
        print("The response of FormsApi->list_form:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FormsApi->list_form: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **count** | **int**| Specify how many forms to return. Default is 50 forms, maximum is 100 forms. | [optional] 
 **page** | **int**| Specify which page of the dataset to return. | [optional] 
 **status** | [**List[str]**](str.md)| Specify which status of the forms dataset to return. | [optional] 
 **order_by** | **str**| Specify the form dataset order to return. | [optional] 
 **asc** | **bool**| Specify sorting the result-set in ascending or descending order. | [optional] 
 **name** | **str**| Specify the form name. | [optional] 

### Return type

[**FormListResponse**](FormListResponse.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Bad Request |  -  |
**401** | Authentication error |  -  |
**403** | Permission error |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

