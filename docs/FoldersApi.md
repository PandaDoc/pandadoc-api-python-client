# pandadoc_client.FoldersApi

All URIs are relative to *https://api.pandadoc.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_document_folder**](FoldersApi.md#create_document_folder) | **POST** /public/v1/documents/folders | Create Documents Folder
[**create_template_folder**](FoldersApi.md#create_template_folder) | **POST** /public/v1/templates/folders | Create Templates Folder
[**list_document_folders**](FoldersApi.md#list_document_folders) | **GET** /public/v1/documents/folders | List Documents Folders
[**list_template_folders**](FoldersApi.md#list_template_folders) | **GET** /public/v1/templates/folders | List Templates Folders
[**rename_document_folder**](FoldersApi.md#rename_document_folder) | **PUT** /public/v1/documents/folders/{id} | Rename Documents Folder
[**rename_template_folder**](FoldersApi.md#rename_template_folder) | **PUT** /public/v1/templates/folders/{id} | Rename Templates Folder


# **create_document_folder**
> DocumentsFolderCreateResponse create_document_folder(documents_folder_create_request)

Create Documents Folder

Create a new folder to store your documents.

For the full list of folder operations and their limitations, see [Organize Documents and Folders](https://developers.pandadoc.com/docs/organize-folders).


### Example

* Api Key Authentication (apiKey):
* OAuth Authentication (oauth2):

```python
import pandadoc_client
from pandadoc_client.models.documents_folder_create_request import DocumentsFolderCreateRequest
from pandadoc_client.models.documents_folder_create_response import DocumentsFolderCreateResponse
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
    api_instance = pandadoc_client.FoldersApi(api_client)
    documents_folder_create_request = {"name":"A top level folder"} # DocumentsFolderCreateRequest | 

    try:
        # Create Documents Folder
        api_response = api_instance.create_document_folder(documents_folder_create_request)
        print("The response of FoldersApi->create_document_folder:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FoldersApi->create_document_folder: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **documents_folder_create_request** | [**DocumentsFolderCreateRequest**](DocumentsFolderCreateRequest.md)|  | 

### Return type

[**DocumentsFolderCreateResponse**](DocumentsFolderCreateResponse.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |
**400** | Bad Request |  -  |
**401** | Authentication error |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_template_folder**
> TemplatesFolderCreateResponse create_template_folder(templates_folder_create_request)

Create Templates Folder

Create a new folder to store your templates.

For the full list of folder operations and their limitations, see [Organize Templates and Folders](https://developers.pandadoc.com/docs/organize-folders).


### Example

* Api Key Authentication (apiKey):
* OAuth Authentication (oauth2):

```python
import pandadoc_client
from pandadoc_client.models.templates_folder_create_request import TemplatesFolderCreateRequest
from pandadoc_client.models.templates_folder_create_response import TemplatesFolderCreateResponse
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
    api_instance = pandadoc_client.FoldersApi(api_client)
    templates_folder_create_request = {"name":"A new templates folder"} # TemplatesFolderCreateRequest | 

    try:
        # Create Templates Folder
        api_response = api_instance.create_template_folder(templates_folder_create_request)
        print("The response of FoldersApi->create_template_folder:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FoldersApi->create_template_folder: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **templates_folder_create_request** | [**TemplatesFolderCreateRequest**](TemplatesFolderCreateRequest.md)|  | 

### Return type

[**TemplatesFolderCreateResponse**](TemplatesFolderCreateResponse.md)

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

# **list_document_folders**
> DocumentsFolderListResponse list_document_folders(parent_uuid=parent_uuid, count=count, page=page)

List Documents Folders

Get the list of folders which contain Documents in your account.

> 📘 
> 
> The root folder is not listed in the response.

For the full list of folder operations and their limitations, see [Organize Documents and Folders](https://developers.pandadoc.com/docs/organize-folders).


### Example

* Api Key Authentication (apiKey):
* OAuth Authentication (oauth2):

```python
import pandadoc_client
from pandadoc_client.models.documents_folder_list_response import DocumentsFolderListResponse
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
    api_instance = pandadoc_client.FoldersApi(api_client)
    parent_uuid = 'Nq8htXxFssmhRxAPSP4SBP' # str | The UUID of the folder containing folders. To list the folders located in the root folder, remove this parameter in the request. (optional)
    count = 50 # int | Optionally, specify how many folders to return. (optional) (default to 50)
    page = 1 # int | Optionally, specify which page of the dataset to return. (optional)

    try:
        # List Documents Folders
        api_response = api_instance.list_document_folders(parent_uuid=parent_uuid, count=count, page=page)
        print("The response of FoldersApi->list_document_folders:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FoldersApi->list_document_folders: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_uuid** | **str**| The UUID of the folder containing folders. To list the folders located in the root folder, remove this parameter in the request. | [optional] 
 **count** | **int**| Optionally, specify how many folders to return. | [optional] [default to 50]
 **page** | **int**| Optionally, specify which page of the dataset to return. | [optional] 

### Return type

[**DocumentsFolderListResponse**](DocumentsFolderListResponse.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_template_folders**
> TemplatesFolderListResponse list_template_folders(parent_uuid=parent_uuid, count=count, page=page)

List Templates Folders

Get the list of folders that contain Templates in your account.

> 📘 
> 
> The root folder is not listed in the response.

For the full list of folder operations and their limitations, see [Organize Templates and Folders](https://developers.pandadoc.com/docs/organize-folders).


### Example

* Api Key Authentication (apiKey):
* OAuth Authentication (oauth2):

```python
import pandadoc_client
from pandadoc_client.models.templates_folder_list_response import TemplatesFolderListResponse
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
    api_instance = pandadoc_client.FoldersApi(api_client)
    parent_uuid = 'Nq8htXxFssmhRxAPSP4SBP' # str | The UUID of the folder containing folders. To list the folders located in the root folder, remove this parameter in the request. (optional)
    count = 50 # int | Optionally, specify how many folders to return. (optional) (default to 50)
    page = 1 # int | Optionally, specify which page of the dataset to return. (optional)

    try:
        # List Templates Folders
        api_response = api_instance.list_template_folders(parent_uuid=parent_uuid, count=count, page=page)
        print("The response of FoldersApi->list_template_folders:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FoldersApi->list_template_folders: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_uuid** | **str**| The UUID of the folder containing folders. To list the folders located in the root folder, remove this parameter in the request. | [optional] 
 **count** | **int**| Optionally, specify how many folders to return. | [optional] [default to 50]
 **page** | **int**| Optionally, specify which page of the dataset to return. | [optional] 

### Return type

[**TemplatesFolderListResponse**](TemplatesFolderListResponse.md)

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

# **rename_document_folder**
> DocumentsFolderRenameResponse rename_document_folder(id, documents_folder_rename_request)

Rename Documents Folder

Rename Documents Folder.

For the full list of folder operations and their limitations, see [Organize Documents and Folders](https://developers.pandadoc.com/docs/organize-folders).


### Example

* Api Key Authentication (apiKey):
* OAuth Authentication (oauth2):

```python
import pandadoc_client
from pandadoc_client.models.documents_folder_rename_request import DocumentsFolderRenameRequest
from pandadoc_client.models.documents_folder_rename_response import DocumentsFolderRenameResponse
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
    api_instance = pandadoc_client.FoldersApi(api_client)
    id = 'Nq8htXxFssmhRxAPSP4SBP' # str | The UUID of the folder that you are renaming.
    documents_folder_rename_request = {"name":"New folder name"} # DocumentsFolderRenameRequest | 

    try:
        # Rename Documents Folder
        api_response = api_instance.rename_document_folder(id, documents_folder_rename_request)
        print("The response of FoldersApi->rename_document_folder:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FoldersApi->rename_document_folder: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The UUID of the folder that you are renaming. | 
 **documents_folder_rename_request** | [**DocumentsFolderRenameRequest**](DocumentsFolderRenameRequest.md)|  | 

### Return type

[**DocumentsFolderRenameResponse**](DocumentsFolderRenameResponse.md)

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

# **rename_template_folder**
> TemplatesFolderRenameResponse rename_template_folder(id, templates_folder_rename_request)

Rename Templates Folder

Rename a templates folder.

For the full list of folder operations and their limitations, see [Organize Templates and Folders](https://developers.pandadoc.com/docs/organize-folders).


### Example

* Api Key Authentication (apiKey):
* OAuth Authentication (oauth2):

```python
import pandadoc_client
from pandadoc_client.models.templates_folder_rename_request import TemplatesFolderRenameRequest
from pandadoc_client.models.templates_folder_rename_response import TemplatesFolderRenameResponse
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
    api_instance = pandadoc_client.FoldersApi(api_client)
    id = 'Nq8htXxFssmhRxAPSP4SBP' # str | The UUID of the folder which you are renaming.
    templates_folder_rename_request = {"name":"New Folder Name"} # TemplatesFolderRenameRequest | 

    try:
        # Rename Templates Folder
        api_response = api_instance.rename_template_folder(id, templates_folder_rename_request)
        print("The response of FoldersApi->rename_template_folder:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FoldersApi->rename_template_folder: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The UUID of the folder which you are renaming. | 
 **templates_folder_rename_request** | [**TemplatesFolderRenameRequest**](TemplatesFolderRenameRequest.md)|  | 

### Return type

[**TemplatesFolderRenameResponse**](TemplatesFolderRenameResponse.md)

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

