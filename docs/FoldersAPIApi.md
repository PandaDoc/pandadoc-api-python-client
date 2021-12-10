# pandadoc_client.FoldersAPIApi

All URIs are relative to *https://api.pandadoc.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_document_folder**](FoldersAPIApi.md#create_document_folder) | **POST** /public/v1/documents/folders | Create Documents Folder
[**create_template_folder**](FoldersAPIApi.md#create_template_folder) | **POST** /public/v1/templates/folders | Create Templates Folder
[**list_document_folders**](FoldersAPIApi.md#list_document_folders) | **GET** /public/v1/documents/folders | List Documents Folders
[**list_template_folders**](FoldersAPIApi.md#list_template_folders) | **GET** /public/v1/templates/folders | List Templates Folders
[**rename_document_folder**](FoldersAPIApi.md#rename_document_folder) | **PUT** /public/v1/documents/folders/{id} | Rename Documents Folder
[**rename_template_folder**](FoldersAPIApi.md#rename_template_folder) | **PUT** /public/v1/templates/folders/{id} | Rename Templates Folder


# **create_document_folder**
> DocumentsFolderCreateResponse create_document_folder(documents_folder_create_request)

Create Documents Folder

Create a new folder to store your documents.

### Example

* Api Key Authentication (apiKey):
* OAuth Authentication (oauth2):

```python
import pandadoc_client
from pandadoc_client.api import folders_api_api
from pandadoc_client.model.documents_folder_create_request import DocumentsFolderCreateRequest
from pandadoc_client.model.documents_folder_create_response import DocumentsFolderCreateResponse
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
    api_instance = folders_api_api.FoldersAPIApi(api_client)
    documents_folder_create_request = DocumentsFolderCreateRequest(
        name="A new document folder",
        parent_uuid="Nq8htXxFssmhRxAPSP4SBP",
    )  # DocumentsFolderCreateRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Create Documents Folder
        api_response = api_instance.create_document_folder(documents_folder_create_request)
        pprint(api_response)
    except pandadoc_client.ApiException as e:
        print("Exception when calling FoldersAPIApi->create_document_folder: %s\n" % e)
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **create_template_folder**
> TemplatesFolderCreateResponse create_template_folder(templates_folder_create_request)

Create Templates Folder

Create a new folder to store your templates.

### Example

* Api Key Authentication (apiKey):
* OAuth Authentication (oauth2):

```python
import pandadoc_client
from pandadoc_client.api import folders_api_api
from pandadoc_client.model.templates_folder_create_request import TemplatesFolderCreateRequest
from pandadoc_client.model.templates_folder_create_response import TemplatesFolderCreateResponse
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
    api_instance = folders_api_api.FoldersAPIApi(api_client)
    templates_folder_create_request = TemplatesFolderCreateRequest(
        name="A new template folder",
        parent_uuid="Nq8htXxFssmhRxAPSP4SBP",
    )  # TemplatesFolderCreateRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Create Templates Folder
        api_response = api_instance.create_template_folder(templates_folder_create_request)
        pprint(api_response)
    except pandadoc_client.ApiException as e:
        print("Exception when calling FoldersAPIApi->create_template_folder: %s\n" % e)
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **list_document_folders**
> DocumentsFolderListResponse list_document_folders()

List Documents Folders

Get the list of folders that contain Documents in your account.

### Example

* Api Key Authentication (apiKey):
* OAuth Authentication (oauth2):

```python
import pandadoc_client
from pandadoc_client.api import folders_api_api
from pandadoc_client.model.documents_folder_list_response import DocumentsFolderListResponse
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
    api_instance = folders_api_api.FoldersAPIApi(api_client)
    parent_uuid = "Nq8htXxFssmhRxAPSP4SBP"  # str | The UUID of the folder containing folders. To list the folders located in the root folder, remove this parameter in the request. (optional)
    count = 10  # int | Optionally, specify how many folders to return. Default is 50 folders, maximum is 100 folders. (optional)
    page = 1  # int | Optionally, specify which page of the dataset to return. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List Documents Folders
        api_response = api_instance.list_document_folders(
            parent_uuid=parent_uuid,
            count=count,
            page=page,
        )
        pprint(api_response)
    except pandadoc_client.ApiException as e:
        print("Exception when calling FoldersAPIApi->list_document_folders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_uuid** | **str**| The UUID of the folder containing folders. To list the folders located in the root folder, remove this parameter in the request. | [optional]
 **count** | **int**| Optionally, specify how many folders to return. Default is 50 folders, maximum is 100 folders. | [optional]
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **list_template_folders**
> TemplatesFolderListResponse list_template_folders()

List Templates Folders

Get the list of folders that contain Templates in your account.

### Example

* Api Key Authentication (apiKey):
* OAuth Authentication (oauth2):

```python
import pandadoc_client
from pandadoc_client.api import folders_api_api
from pandadoc_client.model.templates_folder_list_response import TemplatesFolderListResponse
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
    api_instance = folders_api_api.FoldersAPIApi(api_client)
    parent_uuid = "Nq8htXxFssmhRxAPSP4SBP"  # str | The UUID of the folder containing folders. To list the folders located in the root folder, remove this parameter in the request. (optional)
    count = 10  # int | Optionally, specify how many folders to return. Default is 50 folders, maximum is 100 folders. (optional)
    page = 1  # int | Optionally, specify which page of the dataset to return. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List Templates Folders
        api_response = api_instance.list_template_folders(
            parent_uuid=parent_uuid,
            count=count,
            page=page,
        )
        pprint(api_response)
    except pandadoc_client.ApiException as e:
        print("Exception when calling FoldersAPIApi->list_template_folders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_uuid** | **str**| The UUID of the folder containing folders. To list the folders located in the root folder, remove this parameter in the request. | [optional]
 **count** | **int**| Optionally, specify how many folders to return. Default is 50 folders, maximum is 100 folders. | [optional]
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **rename_document_folder**
> DocumentsFolderRenameResponse rename_document_folder(id, documents_folder_rename_request)

Rename Documents Folder

Rename Documents Folder.

### Example

* Api Key Authentication (apiKey):
* OAuth Authentication (oauth2):

```python
import pandadoc_client
from pandadoc_client.api import folders_api_api
from pandadoc_client.model.documents_folder_rename_response import DocumentsFolderRenameResponse
from pandadoc_client.model.documents_folder_rename_request import DocumentsFolderRenameRequest
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
    api_instance = folders_api_api.FoldersAPIApi(api_client)
    id = "Nq8htXxFssmhRxAPSP4SBP"  # str | The UUID of the folder that you are renaming.
    documents_folder_rename_request = DocumentsFolderRenameRequest(
        name="Another document folder",
    )  # DocumentsFolderRenameRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Rename Documents Folder
        api_response = api_instance.rename_document_folder(id, documents_folder_rename_request)
        pprint(api_response)
    except pandadoc_client.ApiException as e:
        print("Exception when calling FoldersAPIApi->rename_document_folder: %s\n" % e)
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **rename_template_folder**
> TemplatesFolderRenameResponse rename_template_folder(id, templates_folder_rename_request)

Rename Templates Folder

Rename a templates folder.

### Example

* Api Key Authentication (apiKey):
* OAuth Authentication (oauth2):

```python
import pandadoc_client
from pandadoc_client.api import folders_api_api
from pandadoc_client.model.templates_folder_rename_response import TemplatesFolderRenameResponse
from pandadoc_client.model.templates_folder_rename_request import TemplatesFolderRenameRequest
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
    api_instance = folders_api_api.FoldersAPIApi(api_client)
    id = "Nq8htXxFssmhRxAPSP4SBP"  # str | The UUID of the folder which you are renaming.
    templates_folder_rename_request = TemplatesFolderRenameRequest(
        name="Another template folder",
    )  # TemplatesFolderRenameRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Rename Templates Folder
        api_response = api_instance.rename_template_folder(id, templates_folder_rename_request)
        pprint(api_response)
    except pandadoc_client.ApiException as e:
        print("Exception when calling FoldersAPIApi->rename_template_folder: %s\n" % e)
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

