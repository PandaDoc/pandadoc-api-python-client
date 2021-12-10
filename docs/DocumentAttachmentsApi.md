# pandadoc_client.DocumentAttachmentsApi

All URIs are relative to *https://api.pandadoc.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**document_attachment_create**](DocumentAttachmentsApi.md#document_attachment_create) | **POST** /public/v1/documents/{id}/attachments | Document Attachment Create
[**document_attachment_delete**](DocumentAttachmentsApi.md#document_attachment_delete) | **DELETE** /public/v1/documents/{id}/attachments/{attachment_id} | Document Attachment Delete
[**document_attachment_details**](DocumentAttachmentsApi.md#document_attachment_details) | **GET** /public/v1/documents/{id}/attachments/{attachment_id} | Document Attachment Details
[**document_attachment_download**](DocumentAttachmentsApi.md#document_attachment_download) | **GET** /public/v1/documents/{id}/attachments/{attachment_id}/download | Document Attachment Download
[**document_attachments_list**](DocumentAttachmentsApi.md#document_attachments_list) | **GET** /public/v1/documents/{id}/attachments | Document Attachment List


# **document_attachment_create**
> DocumentAttachmentResponse document_attachment_create(id)

Document Attachment Create

Creates an attachment for a particular document

### Example

* Api Key Authentication (apiKey):
* OAuth Authentication (oauth2):

```python
import pandadoc_client
from pandadoc_client.api import document_attachments_api
from pandadoc_client.model.document_attachment_response import DocumentAttachmentResponse
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
    api_instance = document_attachments_api.DocumentAttachmentsApi(api_client)
    id = "BhVzRcxH9Z2LgfPPGXFUBa"  # str | Document UUID
    file = open('/path/to/file', 'rb')  # file_type | Binary file to be attached to a document (optional)
    source = "https://is3-ssl.mzstatic.com/1e7fbd74-d10c-8e3a-63c3-0beb3ea231a5/512x512bb.jpg"  # str | URL link to the file to be attached to a document (optional)
    name = "Additional agreement"  # str | Optional name to set for uploaded file (optional)

    # example passing only required values which don't have defaults set
    try:
        # Document Attachment Create
        api_response = api_instance.document_attachment_create(id)
        pprint(api_response)
    except pandadoc_client.ApiException as e:
        print("Exception when calling DocumentAttachmentsApi->document_attachment_create: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Document Attachment Create
        api_response = api_instance.document_attachment_create(
            id,
            file=file,
            source=source,
            name=name,
        )
        pprint(api_response)
    except pandadoc_client.ApiException as e:
        print("Exception when calling DocumentAttachmentsApi->document_attachment_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Document UUID |
 **file** | **file_type**| Binary file to be attached to a document | [optional]
 **source** | **str**| URL link to the file to be attached to a document | [optional]
 **name** | **str**| Optional name to set for uploaded file | [optional]

### Return type

[**DocumentAttachmentResponse**](DocumentAttachmentResponse.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Authentication error |  -  |
**404** | Not found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **document_attachment_delete**
> document_attachment_delete(id, attachment_id)

Document Attachment Delete

Deletes specific document's attachment

### Example

* Api Key Authentication (apiKey):
* OAuth Authentication (oauth2):

```python
import pandadoc_client
from pandadoc_client.api import document_attachments_api
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
    api_instance = document_attachments_api.DocumentAttachmentsApi(api_client)
    id = "BhVzRcxH9Z2LgfPPGXFUBa"  # str | Document UUID
    attachment_id = "89ce2f49-10fb-4e9b-b5f3-e28be2a5c042"  # str | Attachment UUID

    # example passing only required values which don't have defaults set
    try:
        # Document Attachment Delete
        api_instance.document_attachment_delete(id, attachment_id)
    except pandadoc_client.ApiException as e:
        print("Exception when calling DocumentAttachmentsApi->document_attachment_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Document UUID |
 **attachment_id** | **str**| Attachment UUID |

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
**204** | No Content |  -  |
**401** | Authentication error |  -  |
**404** | Not found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **document_attachment_details**
> DocumentAttachmentResponse document_attachment_details(id, attachment_id)

Document Attachment Details

Returns details of the specific document's attachment

### Example

* Api Key Authentication (apiKey):
* OAuth Authentication (oauth2):

```python
import pandadoc_client
from pandadoc_client.api import document_attachments_api
from pandadoc_client.model.document_attachment_response import DocumentAttachmentResponse
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
    api_instance = document_attachments_api.DocumentAttachmentsApi(api_client)
    id = "BhVzRcxH9Z2LgfPPGXFUBa"  # str | Document UUID
    attachment_id = "89ce2f49-10fb-4e9b-b5f3-e28be2a5c042"  # str | Attachment UUID

    # example passing only required values which don't have defaults set
    try:
        # Document Attachment Details
        api_response = api_instance.document_attachment_details(id, attachment_id)
        pprint(api_response)
    except pandadoc_client.ApiException as e:
        print("Exception when calling DocumentAttachmentsApi->document_attachment_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Document UUID |
 **attachment_id** | **str**| Attachment UUID |

### Return type

[**DocumentAttachmentResponse**](DocumentAttachmentResponse.md)

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

# **document_attachment_download**
> file_type document_attachment_download(id, attachment_id)

Document Attachment Download

Returns document attachment file for download

### Example

* Api Key Authentication (apiKey):
* OAuth Authentication (oauth2):

```python
import pandadoc_client
from pandadoc_client.api import document_attachments_api
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
    api_instance = document_attachments_api.DocumentAttachmentsApi(api_client)
    id = "BhVzRcxH9Z2LgfPPGXFUBa"  # str | Document UUID
    attachment_id = "89ce2f49-10fb-4e9b-b5f3-e28be2a5c042"  # str | Attachment UUID

    # example passing only required values which don't have defaults set
    try:
        # Document Attachment Download
        api_response = api_instance.document_attachment_download(id, attachment_id)
        pprint(api_response)
    except pandadoc_client.ApiException as e:
        print("Exception when calling DocumentAttachmentsApi->document_attachment_download: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Document UUID |
 **attachment_id** | **str**| Attachment UUID |

### Return type

**file_type**

### Authorization

[apiKey](../README.md#apiKey), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/*, application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Authentication error |  -  |
**404** | Not found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **document_attachments_list**
> [DocumentAttachmentResponse] document_attachments_list(id)

Document Attachment List

Return list of objects attached to particular document

### Example

* Api Key Authentication (apiKey):
* OAuth Authentication (oauth2):

```python
import pandadoc_client
from pandadoc_client.api import document_attachments_api
from pandadoc_client.model.document_attachment_response import DocumentAttachmentResponse
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
    api_instance = document_attachments_api.DocumentAttachmentsApi(api_client)
    id = "BhVzRcxH9Z2LgfPPGXFUBa"  # str | Document UUID

    # example passing only required values which don't have defaults set
    try:
        # Document Attachment List
        api_response = api_instance.document_attachments_list(id)
        pprint(api_response)
    except pandadoc_client.ApiException as e:
        print("Exception when calling DocumentAttachmentsApi->document_attachments_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Document UUID |

### Return type

[**[DocumentAttachmentResponse]**](DocumentAttachmentResponse.md)

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

