# pandadoc_client.DocumentAttachmentsApi

All URIs are relative to *https://api.pandadoc.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_document_attachment**](DocumentAttachmentsApi.md#create_document_attachment) | **POST** /public/v1/documents/{id}/attachments | Create Document Attachment
[**create_document_attachment_from_file_upload**](DocumentAttachmentsApi.md#create_document_attachment_from_file_upload) | **POST** /public/v1/documents/{id}/attachments?upload | Create Document Attachment From Upload
[**delete_document_attachment**](DocumentAttachmentsApi.md#delete_document_attachment) | **DELETE** /public/v1/documents/{id}/attachments/{attachment_id} | Delete Document Attachment
[**details_document_attachment**](DocumentAttachmentsApi.md#details_document_attachment) | **GET** /public/v1/documents/{id}/attachments/{attachment_id} | Document Attachment Details
[**download_document_attachment**](DocumentAttachmentsApi.md#download_document_attachment) | **GET** /public/v1/documents/{id}/attachments/{attachment_id}/download | Download Document Attachment
[**list_document_attachments**](DocumentAttachmentsApi.md#list_document_attachments) | **GET** /public/v1/documents/{id}/attachments | List Document Attachments


# **create_document_attachment**
> DocumentAttachmentResponse create_document_attachment(id, document_attachment_request)

Create Document Attachment

Creates an attachment for a particular document

### Example

* Api Key Authentication (apiKey):
* OAuth Authentication (oauth2):

```python
import pandadoc_client
from pandadoc_client.models.document_attachment_request import DocumentAttachmentRequest
from pandadoc_client.models.document_attachment_response import DocumentAttachmentResponse
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
    api_instance = pandadoc_client.DocumentAttachmentsApi(api_client)
    id = 'BhVzRcxH9Z2LgfPPGXFUBa' # str | Document UUID
    document_attachment_request = {"source":"https://upload.wikimedia.org/wikipedia/en/thumb/8/80/Wikipedia-logo-v2.svg/1920px-Wikipedia-logo-v2.svg.png","name":"Wikipedia logo"} # DocumentAttachmentRequest | 

    try:
        # Create Document Attachment
        api_response = api_instance.create_document_attachment(id, document_attachment_request)
        print("The response of DocumentAttachmentsApi->create_document_attachment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentAttachmentsApi->create_document_attachment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Document UUID | 
 **document_attachment_request** | [**DocumentAttachmentRequest**](DocumentAttachmentRequest.md)|  | 

### Return type

[**DocumentAttachmentResponse**](DocumentAttachmentResponse.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Authentication error |  -  |
**404** | Not found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_document_attachment_from_file_upload**
> DocumentAttachmentResponse create_document_attachment_from_file_upload(id, file=file, name=name)

Create Document Attachment From Upload

Creates an attachment for a particular document

### Example

* Api Key Authentication (apiKey):
* OAuth Authentication (oauth2):

```python
import pandadoc_client
from pandadoc_client.models.document_attachment_response import DocumentAttachmentResponse
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
    api_instance = pandadoc_client.DocumentAttachmentsApi(api_client)
    id = 'BhVzRcxH9Z2LgfPPGXFUBa' # str | Document UUID
    file = None # bytearray | Binary file to be attached to a document (optional)
    name = 'name_example' # str | Optional name to set for uploaded file (optional)

    try:
        # Create Document Attachment From Upload
        api_response = api_instance.create_document_attachment_from_file_upload(id, file=file, name=name)
        print("The response of DocumentAttachmentsApi->create_document_attachment_from_file_upload:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentAttachmentsApi->create_document_attachment_from_file_upload: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Document UUID | 
 **file** | **bytearray**| Binary file to be attached to a document | [optional] 
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_document_attachment**
> delete_document_attachment(id, attachment_id)

Delete Document Attachment

Deletes an attachment from the document.

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
    api_instance = pandadoc_client.DocumentAttachmentsApi(api_client)
    id = 'BhVzRcxH9Z2LgfPPGXFUBa' # str | Document UUID.
    attachment_id = '89ce2f49-10fb-4e9b-b5f3-e28be2a5c042' # str | Attachment UUID.

    try:
        # Delete Document Attachment
        api_instance.delete_document_attachment(id, attachment_id)
    except Exception as e:
        print("Exception when calling DocumentAttachmentsApi->delete_document_attachment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Document UUID. | 
 **attachment_id** | **str**| Attachment UUID. | 

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **details_document_attachment**
> DocumentAttachmentResponse details_document_attachment(id, attachment_id)

Document Attachment Details

Returns details of the specific document's attachment.

### Example

* Api Key Authentication (apiKey):
* OAuth Authentication (oauth2):

```python
import pandadoc_client
from pandadoc_client.models.document_attachment_response import DocumentAttachmentResponse
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
    api_instance = pandadoc_client.DocumentAttachmentsApi(api_client)
    id = 'BhVzRcxH9Z2LgfPPGXFUBa' # str | Document UUID.
    attachment_id = '89ce2f49-10fb-4e9b-b5f3-e28be2a5c042' # str | Attachment UUID.

    try:
        # Document Attachment Details
        api_response = api_instance.details_document_attachment(id, attachment_id)
        print("The response of DocumentAttachmentsApi->details_document_attachment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentAttachmentsApi->details_document_attachment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Document UUID. | 
 **attachment_id** | **str**| Attachment UUID. | 

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
**409** | Conflict |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_document_attachment**
> bytearray download_document_attachment(id, attachment_id)

Download Document Attachment

Download an attachment by ID.

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
    api_instance = pandadoc_client.DocumentAttachmentsApi(api_client)
    id = 'BhVzRcxH9Z2LgfPPGXFUBa' # str | Document UUID.
    attachment_id = '89ce2f49-10fb-4e9b-b5f3-e28be2a5c042' # str | Attachment UUID.

    try:
        # Download Document Attachment
        api_response = api_instance.download_document_attachment(id, attachment_id)
        print("The response of DocumentAttachmentsApi->download_document_attachment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentAttachmentsApi->download_document_attachment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Document UUID. | 
 **attachment_id** | **str**| Attachment UUID. | 

### Return type

**bytearray**

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
**409** | Conflict |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_document_attachments**
> List[DocumentAttachmentResponse] list_document_attachments(id)

List Document Attachments

Returns a list of attachments associated with a specified document.

### Example

* Api Key Authentication (apiKey):
* OAuth Authentication (oauth2):

```python
import pandadoc_client
from pandadoc_client.models.document_attachment_response import DocumentAttachmentResponse
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
    api_instance = pandadoc_client.DocumentAttachmentsApi(api_client)
    id = 'BhVzRcxH9Z2LgfPPGXFUBa' # str | Document UUID

    try:
        # List Document Attachments
        api_response = api_instance.list_document_attachments(id)
        print("The response of DocumentAttachmentsApi->list_document_attachments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentAttachmentsApi->list_document_attachments: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Document UUID | 

### Return type

[**List[DocumentAttachmentResponse]**](DocumentAttachmentResponse.md)

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
**409** | Conflict |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

