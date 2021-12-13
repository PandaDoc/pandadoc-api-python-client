# pandadoc_client.TemplatesApi

All URIs are relative to *https://api.pandadoc.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_template**](TemplatesApi.md#delete_template) | **DELETE** /public/v1/templates/{id} | Delete Template
[**details_template**](TemplatesApi.md#details_template) | **GET** /public/v1/templates/{id}/details | Details Template
[**list_templates**](TemplatesApi.md#list_templates) | **GET** /public/v1/templates | List Templates


# **delete_template**
> delete_template(id)

Delete Template

Delete a template

### Example

* Api Key Authentication (apiKey):
* OAuth Authentication (oauth2):

```python
import pandadoc_client
from pandadoc_client.api import templates_api
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
    api_instance = templates_api.TemplatesApi(api_client)
    id = "EE8yUNg5HztqVAuH85He8V"  # str | Template ID

    # example passing only required values which don't have defaults set
    try:
        # Delete Template
        api_instance.delete_template(id)
    except pandadoc_client.ApiException as e:
        print("Exception when calling TemplatesApi->delete_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Template ID |

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
**204** | No content |  -  |
**400** | Bad Request |  -  |
**401** | Authentication error |  -  |
**403** | Permission error |  -  |
**404** | Not found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **details_template**
> TemplateDetailsResponse details_template(id)

Details Template

Return detailed data about a template.

### Example

* Api Key Authentication (apiKey):
* OAuth Authentication (oauth2):

```python
import pandadoc_client
from pandadoc_client.api import templates_api
from pandadoc_client.model.template_details_response import TemplateDetailsResponse
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
    api_instance = templates_api.TemplatesApi(api_client)
    id = "EE8yUNg5HztqVAuH85He8V"  # str | Template ID

    # example passing only required values which don't have defaults set
    try:
        # Details Template
        api_response = api_instance.details_template(id)
        pprint(api_response)
    except pandadoc_client.ApiException as e:
        print("Exception when calling TemplatesApi->details_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Template ID |

### Return type

[**TemplateDetailsResponse**](TemplateDetailsResponse.md)

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
**403** | Permission error |  -  |
**404** | Not found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **list_templates**
> TemplateListResponse list_templates()

List Templates

Optionally, filter by a search query or tags.

### Example

* Api Key Authentication (apiKey):
* OAuth Authentication (oauth2):

```python
import pandadoc_client
from pandadoc_client.api import templates_api
from pandadoc_client.model.template_list_response import TemplateListResponse
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
    api_instance = templates_api.TemplatesApi(api_client)
    q = "Sample onboarding template"  # str | Optional search query. Filter by template name. (optional)
    shared = True  # bool | Returns only the shared templates. (optional)
    deleted = True  # bool | Optional. Returns only the deleted templates. (optional)
    count = 10  # int | Optionally, specify how many templates to return. Default is 50 templates, maximum is 100 templates. (optional)
    page = 1  # int | Optionally, specify which page of the dataset to return. (optional)
    id = "e9LxBesSL73AeZMzeYdfvV"  # str | Optionally, specify template ID. (optional)
    folder_uuid = "xDKHoJ8DkwhiTQSUzNveCJ"  # str | UUID of the folder where the templates are stored. (optional)
    tag = [
        "tag_example",
    ]  # [str] | Optional search tag. Filter by template tag. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List Templates
        api_response = api_instance.list_templates(
            q=q,
            shared=shared,
            deleted=deleted,
            count=count,
            page=page,
            id=id,
            folder_uuid=folder_uuid,
            tag=tag,
        )
        pprint(api_response)
    except pandadoc_client.ApiException as e:
        print("Exception when calling TemplatesApi->list_templates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**| Optional search query. Filter by template name. | [optional]
 **shared** | **bool**| Returns only the shared templates. | [optional]
 **deleted** | **bool**| Optional. Returns only the deleted templates. | [optional]
 **count** | **int**| Optionally, specify how many templates to return. Default is 50 templates, maximum is 100 templates. | [optional]
 **page** | **int**| Optionally, specify which page of the dataset to return. | [optional]
 **id** | **str**| Optionally, specify template ID. | [optional]
 **folder_uuid** | **str**| UUID of the folder where the templates are stored. | [optional]
 **tag** | **[str]**| Optional search tag. Filter by template tag. | [optional]

### Return type

[**TemplateListResponse**](TemplateListResponse.md)

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
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

