# pandadoc_client.FormsApi

All URIs are relative to *https://api.pandadoc.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_form**](FormsApi.md#list_form) | **GET** /public/v1/forms | Forms


# **list_form**
> FormListResponse list_form()

Forms

List forms.

### Example

* Api Key Authentication (apiKey):
* OAuth Authentication (oauth2):

```python
import pandadoc_client
from pandadoc_client.api import forms_api
from pandadoc_client.model.form_list_response import FormListResponse
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
    api_instance = forms_api.FormsApi(api_client)
    count = 10  # int | Optionally, specify how many forms to return. Default is 50 forms, maximum is 100 forms. (optional)
    page = 1  # int | Optionally, specify which page of the dataset to return. (optional)
    status = [
        "draft",
    ]  # [str] | Optionally, specify which status of the forms dataset to return. (optional)
    order_by = "name"  # str | Optionally, specify the form dataset order to return. (optional)
    asc = True  # bool | Optionally, specify sorting the result-set in ascending or descending order. (optional)
    name = "New Form"  # str | Specify the form name. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Forms
        api_response = api_instance.list_form(
            count=count,
            page=page,
            status=status,
            order_by=order_by,
            asc=asc,
            name=name,
        )
        pprint(api_response)
    except pandadoc_client.ApiException as e:
        print("Exception when calling FormsApi->list_form: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **count** | **int**| Optionally, specify how many forms to return. Default is 50 forms, maximum is 100 forms. | [optional]
 **page** | **int**| Optionally, specify which page of the dataset to return. | [optional]
 **status** | **[str]**| Optionally, specify which status of the forms dataset to return. | [optional]
 **order_by** | **str**| Optionally, specify the form dataset order to return. | [optional]
 **asc** | **bool**| Optionally, specify sorting the result-set in ascending or descending order. | [optional]
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
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

