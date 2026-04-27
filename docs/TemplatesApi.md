# pandadoc_client.TemplatesApi

All URIs are relative to *https://api.pandadoc.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_template**](TemplatesApi.md#create_template) | **POST** /public/v1/templates | Create Template
[**create_template_editing_session**](TemplatesApi.md#create_template_editing_session) | **POST** /public/v1/templates/{id}/editing-sessions | Create Template Editing Session 
[**create_template_with_upload**](TemplatesApi.md#create_template_with_upload) | **POST** /public/v1/templates?upload | Create Template from File Upload
[**delete_template**](TemplatesApi.md#delete_template) | **DELETE** /public/v1/templates/{id} | Delete Template
[**details_template**](TemplatesApi.md#details_template) | **GET** /public/v1/templates/{id}/details | Template Details
[**list_templates**](TemplatesApi.md#list_templates) | **GET** /public/v1/templates | List Templates
[**status_template**](TemplatesApi.md#status_template) | **GET** /public/v1/templates/{id} | Template Status
[**update_template**](TemplatesApi.md#update_template) | **PATCH** /public/v1/templates/{id} | Template Update


# **create_template**
> TemplateCreateResponse create_template(create_template_from_url_request, fields=fields)

Create Template

This operation allows you to create a new template by providing the necessary template details.

### Example

* Api Key Authentication (apiKey):
* OAuth Authentication (oauth2):

```python
import pandadoc_client
from pandadoc_client.models.create_template_from_url_request import CreateTemplateFromUrlRequest
from pandadoc_client.models.template_create_response import TemplateCreateResponse
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
    api_instance = pandadoc_client.TemplatesApi(api_client)
    create_template_from_url_request = {"name":"Sample Template","folder_uuid":"EE8yUNg5HztqVAuH85He8V","owner":{"email":"john.doe@example.com"},"metadata":{"my_favorite_pet":"Panda"}} # CreateTemplateFromUrlRequest | 
    fields = ['[\"content_date_modified\"]'] # List[str] | A comma-separated list of additional fields to include in the response. (optional)

    try:
        # Create Template
        api_response = api_instance.create_template(create_template_from_url_request, fields=fields)
        print("The response of TemplatesApi->create_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemplatesApi->create_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_template_from_url_request** | [**CreateTemplateFromUrlRequest**](CreateTemplateFromUrlRequest.md)|  | 
 **fields** | [**List[str]**](str.md)| A comma-separated list of additional fields to include in the response. | [optional] 

### Return type

[**TemplateCreateResponse**](TemplateCreateResponse.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Authentication error |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_template_editing_session**
> CreateTemplateEditingSession201Response create_template_editing_session(id, editing_session_request)

Create Template Editing Session 

Creates a new editing session for the Embedded Editor. The response includes an E-Token, which is required to open the template.

#### Limitations

- **Single Active Session per User-Template Pair** 
  Only one editing session can be active at a time for a specific user and template. Creating a new session for the same user-template pair will automatically invalidate the previous one.

- **Weekly Session Cap** 
  A maximum of **250** editing sessions can be created for a single template per week. Any attempt to exceed this limit will result in a `403 Forbidden` error.


### Example

* Api Key Authentication (apiKey):
* OAuth Authentication (oauth2):

```python
import pandadoc_client
from pandadoc_client.models.create_template_editing_session201_response import CreateTemplateEditingSession201Response
from pandadoc_client.models.editing_session_request import EditingSessionRequest
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
    api_instance = pandadoc_client.TemplatesApi(api_client)
    id = 'a53a2f96b91d47f99ee33f' # str | Template ID
    editing_session_request = {"email":"john.doe@pandadoc.com","lifetime":100} # EditingSessionRequest | 

    try:
        # Create Template Editing Session 
        api_response = api_instance.create_template_editing_session(id, editing_session_request)
        print("The response of TemplatesApi->create_template_editing_session:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemplatesApi->create_template_editing_session: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Template ID | 
 **editing_session_request** | [**EditingSessionRequest**](EditingSessionRequest.md)|  | 

### Return type

[**CreateTemplateEditingSession201Response**](CreateTemplateEditingSession201Response.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Template Editing Session created |  -  |
**400** | Bad request |  -  |
**401** | Authentication error |  -  |
**403** | Permission error |  -  |
**404** | Not found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_template_with_upload**
> TemplateCreateResponse create_template_with_upload(fields=fields, file=file, data=data)

Create Template from File Upload

This asynchronous endpoint allows users to create a new template by uploading a file.

The uploaded file is processed in the background to generate the template.
The maximum allowable file size for upload is 100 MB.
Field tags and form fields are not supported yet.

Once the file is uploaded, the processing will happen asynchronously, and users need to check [the status of the template](https://developers.pandadoc.com/reference/template-status) creation.


### Example

* Api Key Authentication (apiKey):
* OAuth Authentication (oauth2):

```python
import pandadoc_client
from pandadoc_client.models.template_create_response import TemplateCreateResponse
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
    api_instance = pandadoc_client.TemplatesApi(api_client)
    fields = ['[\"content_date_modified\"]'] # List[str] | A comma-separated list of additional fields to include in the response. (optional)
    file = None # bytearray | Binary PDF/DocX/RTF File. (optional)
    data = pandadoc_client.CreateTemplateRequest() # CreateTemplateRequest | JSON as a multipart/form-data string. (optional)

    try:
        # Create Template from File Upload
        api_response = api_instance.create_template_with_upload(fields=fields, file=file, data=data)
        print("The response of TemplatesApi->create_template_with_upload:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemplatesApi->create_template_with_upload: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | [**List[str]**](str.md)| A comma-separated list of additional fields to include in the response. | [optional] 
 **file** | **bytearray**| Binary PDF/DocX/RTF File. | [optional] 
 **data** | [**CreateTemplateRequest**](CreateTemplateRequest.md)| JSON as a multipart/form-data string. | [optional] 

### Return type

[**TemplateCreateResponse**](TemplateCreateResponse.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Authentication error |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_template**
> delete_template(id)

Delete Template

Delete a template

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
    api_instance = pandadoc_client.TemplatesApi(api_client)
    id = 'EE8yUNg5HztqVAuH85He8V' # str | Template ID

    try:
        # Delete Template
        api_instance.delete_template(id)
    except Exception as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **details_template**
> TemplateDetailsResponse details_template(id)

Template Details

Get details about a template by `id`. Details include:

- Basic template information (name, author, etc)
- Roles
- All fields with values
- All tokens with values
- Pricing information (pricing tables, products, quotes)
- Template metadata
- Template tags
- Content placeholders
- Modification timestamps. Note that `date_modified` means any changes associated with the template roles, while `content_date_modified` logs any changes in the template content.


### Example

* Api Key Authentication (apiKey):
* OAuth Authentication (oauth2):

```python
import pandadoc_client
from pandadoc_client.models.template_details_response import TemplateDetailsResponse
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
    api_instance = pandadoc_client.TemplatesApi(api_client)
    id = 'vibuun3DXG8QDDLfXm27Ne' # str | Template ID

    try:
        # Template Details
        api_response = api_instance.details_template(id)
        print("The response of TemplatesApi->details_template:\n")
        pprint(api_response)
    except Exception as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_templates**
> TemplateListResponse list_templates(q=q, shared=shared, deleted=deleted, count=count, page=page, id=id, folder_uuid=folder_uuid, tag=tag, fields=fields)

List Templates

Retrieves a list of templates. You can filter results by a search query, tags, or fields.

### Example

* Api Key Authentication (apiKey):
* OAuth Authentication (oauth2):

```python
import pandadoc_client
from pandadoc_client.models.template_list_response import TemplateListResponse
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
    api_instance = pandadoc_client.TemplatesApi(api_client)
    q = 'Sample onboarding template' # str | Search query. Filter by template name. (optional)
    shared = false # bool | Returns only the shared templates. (optional)
    deleted = false # bool | Returns only the deleted templates. (optional)
    count = 50 # int | Specify how many templates to return. (optional) (default to 50)
    page = 1 # int | Specify which page of the dataset to return. (optional)
    id = 'e9LxBesSL73AeZMzeYdfvV' # str | Specify template ID. (optional)
    folder_uuid = 'xDKHoJ8DkwhiTQSUzNveCJ' # str | UUID of the folder where the templates are stored. (optional)
    tag = ['[\"onboarding\"]'] # List[str] | Search tag. Filter by template tag. (optional)
    fields = ['[\"content_date_modified\"]'] # List[str] | A comma-separated list of additional fields to include in the response. (optional)

    try:
        # List Templates
        api_response = api_instance.list_templates(q=q, shared=shared, deleted=deleted, count=count, page=page, id=id, folder_uuid=folder_uuid, tag=tag, fields=fields)
        print("The response of TemplatesApi->list_templates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemplatesApi->list_templates: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**| Search query. Filter by template name. | [optional] 
 **shared** | **bool**| Returns only the shared templates. | [optional] 
 **deleted** | **bool**| Returns only the deleted templates. | [optional] 
 **count** | **int**| Specify how many templates to return. | [optional] [default to 50]
 **page** | **int**| Specify which page of the dataset to return. | [optional] 
 **id** | **str**| Specify template ID. | [optional] 
 **folder_uuid** | **str**| UUID of the folder where the templates are stored. | [optional] 
 **tag** | [**List[str]**](str.md)| Search tag. Filter by template tag. | [optional] 
 **fields** | [**List[str]**](str.md)| A comma-separated list of additional fields to include in the response. | [optional] 

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **status_template**
> TemplateStatusResponse status_template(id)

Template Status

## Available Template Statuses

The following is a complete list of all possible template statuses returned:

| Template Status      | Status Description                                                                                                                      |
| :------------------- | :-------------------------------------------------------------------------------------------------------------------------------------- |
| `template.UPLOADED`  | The template upload process has been initiated and is currently in progress. It will soon transition to the `template.PROCESSED` state. |
| `template.PROCESSED` | The template has been successfully uploaded and created. At this stage, all aspects of the template are editable.                       |
| `template.ERROR`     | The template upload process has failed. Please refer to the error details in the response for more information.                         |


### Example

* Api Key Authentication (apiKey):
* OAuth Authentication (oauth2):

```python
import pandadoc_client
from pandadoc_client.models.template_status_response import TemplateStatusResponse
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
    api_instance = pandadoc_client.TemplatesApi(api_client)
    id = 'vibuun3DXG8QDDLfXm27Ne' # str | Template ID

    try:
        # Template Status
        api_response = api_instance.status_template(id)
        print("The response of TemplatesApi->status_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemplatesApi->status_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Template ID | 

### Return type

[**TemplateStatusResponse**](TemplateStatusResponse.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_template**
> update_template(id, template_update_request)

Template Update

> 🚧 Template status
> 
> You can only update a template in the PROCESSED status (`template.PROCESSED`). 
> 
> After creating a new template, it usually retains a `template.uploaded` status for 3-5 seconds while the template syncs across PandaDoc servers. When the template is available for further API calls, the template moves to the `template.PROCESSED` state. Use [Template Status](https://developers.pandadoc.com/reference/template-status) or Webhooks to check template status.


### Example

* Api Key Authentication (apiKey):
* OAuth Authentication (oauth2):

```python
import pandadoc_client
from pandadoc_client.models.template_update_request import TemplateUpdateRequest
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
    api_instance = pandadoc_client.TemplatesApi(api_client)
    id = 'BhVzRcxH9Z2LgfPPGXFUBa' # str | Template ID
    template_update_request = pandadoc_client.TemplateUpdateRequest() # TemplateUpdateRequest | 

    try:
        # Template Update
        api_instance.update_template(id, template_update_request)
    except Exception as e:
        print("Exception when calling TemplatesApi->update_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Template ID | 
 **template_update_request** | [**TemplateUpdateRequest**](TemplateUpdateRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

