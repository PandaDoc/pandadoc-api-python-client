# pandadoc_client.DocumentsApi

All URIs are relative to *https://api.pandadoc.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**append_content_library_item_to_document**](DocumentsApi.md#append_content_library_item_to_document) | **POST** /public/v1/documents/{id}/append-content-library-item | Append Content Library Item to a document
[**bulk_delete_documents**](DocumentsApi.md#bulk_delete_documents) | **DELETE** /public/v1/documents | Delete documents (bulk)
[**change_document_status**](DocumentsApi.md#change_document_status) | **PATCH** /public/v1/documents/{id}/status | Document Status Change
[**change_document_status_with_upload**](DocumentsApi.md#change_document_status_with_upload) | **PATCH** /public/v1/documents/{id}/status?upload | Document Status Change with Upload
[**create_document**](DocumentsApi.md#create_document) | **POST** /public/v1/documents | Create Document
[**create_document_editing_session**](DocumentsApi.md#create_document_editing_session) | **POST** /public/v1/documents/{id}/editing-sessions | Create Document Editing Session 
[**create_document_from_upload**](DocumentsApi.md#create_document_from_upload) | **POST** /public/v1/documents?upload | Create Document from File Upload
[**create_document_link**](DocumentsApi.md#create_document_link) | **POST** /public/v1/documents/{id}/session | Create Document Session for Embedded Sign
[**create_export_docx_task**](DocumentsApi.md#create_export_docx_task) | **POST** /public/beta/documents/{document_id}/docx-export-tasks | [Beta] Create DOCX Export Task
[**delete_document**](DocumentsApi.md#delete_document) | **DELETE** /public/v1/documents/{id} | Delete Document
[**details_document**](DocumentsApi.md#details_document) | **GET** /public/v1/documents/{id}/details | Document Details
[**document_e_sign_disclosure**](DocumentsApi.md#document_e_sign_disclosure) | **GET** /public/v1/documents/{document_id}/esign-disclosure | Document eSign disclosure
[**document_move_to_folder**](DocumentsApi.md#document_move_to_folder) | **POST** /public/v1/documents/{id}/move-to-folder/{folder_id} | Document move to folder
[**document_revert_to_draft**](DocumentsApi.md#document_revert_to_draft) | **POST** /public/v1/documents/{id}/draft | Move Document to Draft
[**download_document**](DocumentsApi.md#download_document) | **GET** /public/v1/documents/{id}/download | Document Download
[**download_protected_document**](DocumentsApi.md#download_protected_document) | **GET** /public/v1/documents/{id}/download-protected | Download Completed Document
[**get_docx_export_task**](DocumentsApi.md#get_docx_export_task) | **GET** /public/beta/documents/{document_id}/docx-export-tasks/{task_id} | [Beta] DOCX Export Task
[**list_documents**](DocumentsApi.md#list_documents) | **GET** /public/v1/documents | List Documents
[**send_document**](DocumentsApi.md#send_document) | **POST** /public/v1/documents/{id}/send | Send Document
[**status_document**](DocumentsApi.md#status_document) | **GET** /public/v1/documents/{id} | Document Status
[**transfer_all_documents_ownership**](DocumentsApi.md#transfer_all_documents_ownership) | **PATCH** /public/v1/documents/ownership | Transfer all documents ownership
[**transfer_document_ownership**](DocumentsApi.md#transfer_document_ownership) | **PATCH** /public/v1/documents/{id}/ownership | Update document ownership
[**update_document**](DocumentsApi.md#update_document) | **PATCH** /public/v1/documents/{id} | Update Document


# **append_content_library_item_to_document**
> AppendCLIDataResponse append_content_library_item_to_document(id, append_cli_data_request)

Append Content Library Item to a document

Appends a Content Library Item (CLI) to a document and provides a name mapping for its content blocks.

### Example

* Api Key Authentication (apiKey):
* OAuth Authentication (oauth2):

```python
import pandadoc_client
from pandadoc_client.models.append_cli_data_request import AppendCLIDataRequest
from pandadoc_client.models.append_cli_data_response import AppendCLIDataResponse
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
    api_instance = pandadoc_client.DocumentsApi(api_client)
    id = 'BhVzRcxH9Z2LgfPPGXFUBa' # str | Specify document id.
    append_cli_data_request = pandadoc_client.AppendCLIDataRequest() # AppendCLIDataRequest | 

    try:
        # Append Content Library Item to a document
        api_response = api_instance.append_content_library_item_to_document(id, append_cli_data_request)
        print("The response of DocumentsApi->append_content_library_item_to_document:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentsApi->append_content_library_item_to_document: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Specify document id. | 
 **append_cli_data_request** | [**AppendCLIDataRequest**](AppendCLIDataRequest.md)|  | 

### Return type

[**AppendCLIDataResponse**](AppendCLIDataResponse.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | OK |  -  |
**401** | Authentication error |  -  |
**403** | Permission error |  -  |
**404** | Not found |  -  |
**409** | Conflict |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_delete_documents**
> BulkDeleteDocumentsResponse bulk_delete_documents(bulk_delete_documents_request_item)

Delete documents (bulk)

Delete multiple documents in one request by sending a JSON array. Each element must be an object with an `id` field (the document ID, same value as elsewhere in the Documents API).

The caller must have permission to delete each document. Documents must belong to the authenticated workspace.

This batch operation returns **200 OK** with a JSON body containing an `id` array of deleted document IDs. That differs from [Delete Document](#operation/deleteDocument) (`DELETE /public/v1/documents/{id}`), which returns **204 No Content** for a single document.


### Example

* Api Key Authentication (apiKey):
* OAuth Authentication (oauth2):

```python
import pandadoc_client
from pandadoc_client.models.bulk_delete_documents_request_item import BulkDeleteDocumentsRequestItem
from pandadoc_client.models.bulk_delete_documents_response import BulkDeleteDocumentsResponse
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
    api_instance = pandadoc_client.DocumentsApi(api_client)
    bulk_delete_documents_request_item = [{"id":"XjV64iXRJMerjSpk428QSF"},{"id":"6NbHUUu6uuYN2tqJvgtf9h"}] # List[BulkDeleteDocumentsRequestItem] | 

    try:
        # Delete documents (bulk)
        api_response = api_instance.bulk_delete_documents(bulk_delete_documents_request_item)
        print("The response of DocumentsApi->bulk_delete_documents:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentsApi->bulk_delete_documents: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bulk_delete_documents_request_item** | [**List[BulkDeleteDocumentsRequestItem]**](BulkDeleteDocumentsRequestItem.md)|  | 

### Return type

[**BulkDeleteDocumentsResponse**](BulkDeleteDocumentsResponse.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK — documents were deleted. Response lists deleted document IDs. |  -  |
**400** | Bad Request |  -  |
**401** | Authentication error |  -  |
**403** | Permission error |  -  |
**404** | Not found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_document_status**
> change_document_status(id, document_status_change_request)

Document Status Change

PandaDoc has eight document statuses, but you can manually set your document status to only four:

### Document statuses

- Completed - `document.completed` - API code `2`
- Expired - `document.voided` - code `11`
- Paid - `document.paid` - code `10`. **Important**: You can only set it if you have a payment app connected.
- Declined - `document.declined` - code `12`

> 🚧 Pass a numeric code for the corresponding document status, for example, `2` for `document.completed`.

Find more details in [\[Editor 2.0\] Manually change document status](https://support.pandadoc.com/en/articles/9714842-manually-change-document-status) topic.

| Current Status | To Completed: | To Expired: | To Paid: | To Declined: |
|----------------|---------------|-------------|----------|--------------|
| Draft          | YES           | NO          | YES      | YES          |
| Approved       | NO            | NO          | NO       | NO           |
| Sent           | YES           | YES         | NO       | YES          |
| Viewed         | YES           | YES         | NO       | YES          |
| Completed (Auto) | NO          | NO          | NO       | YES          |
| Waithing for payment | NO      | NO          | YES      | YES          |
| Paid           | NO            | NO          | NO       | NO           |
| Expired        | YES           | NO          | YES      | YES          |
| Declined       | YES           | NO          | YES      | NO           |

> ✅ - from `document.voided` to `document.paid`
>
> ❌ - from `document.paid` to `document.voided`


### Example

* Api Key Authentication (apiKey):
* OAuth Authentication (oauth2):

```python
import pandadoc_client
from pandadoc_client.models.document_status_change_request import DocumentStatusChangeRequest
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
    api_instance = pandadoc_client.DocumentsApi(api_client)
    id = 'iGsFiaV2hEEvQdhr2WAkMk' # str | Specify document ID.
    document_status_change_request = {"status":12,"note":"Change status to Decline","notify_recipients":false} # DocumentStatusChangeRequest | 

    try:
        # Document Status Change
        api_instance.change_document_status(id, document_status_change_request)
    except Exception as e:
        print("Exception when calling DocumentsApi->change_document_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Specify document ID. | 
 **document_status_change_request** | [**DocumentStatusChangeRequest**](DocumentStatusChangeRequest.md)|  | 

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
**401** | Authentication error |  -  |
**403** | Permission error |  -  |
**404** | Not found |  -  |
**409** | Conflict |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_document_status_with_upload**
> change_document_status_with_upload(id, file=file, data=data)

Document Status Change with Upload

PandaDoc has eight document statuses, but you can manually set your document status to only four:

### Document statuses

- Completed - `document.completed` - API code `2`
- Expired - `document.voided` - code `11`
- Paid - `document.paid` - code `10`. **Important**: You can only set it if you have a payment app connected.
- Declined - `document.declined` - code `12`

> 🚧 Pass a numeric code for the corresponding document status, for example, `2` for `document.completed`.

Find more details in [\[Editor 2.0\] Manually change document status](https://support.pandadoc.com/en/articles/9714842-manually-change-document-status) topic.

| Current Status | To Completed: | To Expired: | To Paid: | To Declined: |
|----------------|---------------|-------------|----------|--------------|
| Draft          | YES           | NO          | YES      | YES          |
| Approved       | NO            | NO          | NO       | NO           |
| Sent           | YES           | YES         | NO       | YES          |
| Viewed         | YES           | YES         | NO       | YES          |
| Completed (Auto) | NO          | NO          | NO       | YES          |
| Waithing for payment | NO      | NO          | YES      | YES          |
| Paid           | NO            | NO          | NO       | NO           |
| Expired        | YES           | NO          | YES      | YES          |
| Declined       | YES           | NO          | YES      | NO           |

> ✅ - from `document.voided` to `document.paid`
>
> ❌ - from `document.paid` to `document.voided`


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
    api_instance = pandadoc_client.DocumentsApi(api_client)
    id = 'iGsFiaV2hEEvQdhr2WAkMk' # str | Specify document ID.
    file = None # bytearray | Binary attachment file (optional)
    data = pandadoc_client.DocumentStatusChangeRequest() # DocumentStatusChangeRequest | JSON as a multipart/form-data string. (optional)

    try:
        # Document Status Change with Upload
        api_instance.change_document_status_with_upload(id, file=file, data=data)
    except Exception as e:
        print("Exception when calling DocumentsApi->change_document_status_with_upload: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Specify document ID. | 
 **file** | **bytearray**| Binary attachment file | [optional] 
 **data** | [**DocumentStatusChangeRequest**](DocumentStatusChangeRequest.md)| JSON as a multipart/form-data string. | [optional] 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No content |  -  |
**401** | Authentication error |  -  |
**403** | Permission error |  -  |
**404** | Not found |  -  |
**409** | Conflict |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_document**
> DocumentCreateResponse create_document(document_create_request, editor_ver=editor_ver, use_form_field_properties=use_form_field_properties)

Create Document

## Create from a template
> See the [Create document from template](https://developers.pandadoc.com/docs/create-document-from-template) tutorial for details on how to use this endpoint, as well as a sample template.

## Create from a URL
> See the [Create from public PDF](https://developers.pandadoc.com/docs/create-and-send-a-document-from-a-publicly-available-pdf) guide for info about roles and fields, as well as PDF examples.


### Example

* Api Key Authentication (apiKey):
* OAuth Authentication (oauth2):

```python
import pandadoc_client
from pandadoc_client.models.document_create_request import DocumentCreateRequest
from pandadoc_client.models.document_create_response import DocumentCreateResponse
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
    api_instance = pandadoc_client.DocumentsApi(api_client)
    document_create_request = {"name":"Simple API Sample Document from PandaDoc Template","template_uuid":"onoznwTq4Y3EELMPyvucnc","recipients":[{"email":"josh@example.com","first_name":"Josh","last_name":"Ron","role":"user","phone":"555-5555-5555","signing_order":1,"company":"PandaDoc","default":false,"delivery_methods":{"sms":true,"email":false},"redirect":{"is_enabled":true,"url":"https://super.redirect.url/1"},"verification_settings":{"verification_place":"before_open","passcode_verification":null,"phone_verification":null,"kba_verification":null,"id_verification":{"enabled":true}}}],"tokens":[{"name":"Favorite.Pet","value":"Panda"}],"fields":{"Favorite.Color":{"value":"PandaDoc green"},"Delivery":{"value":"Same Day Delivery"},"Like":{"value":true},"Date":{"value":"2019-12-31T00:00:00.000Z"}},"metadata":{"my_favorite_pet":"Panda"},"tags":["created_via_api","test_document"],"images":[{"name":"Image 1","urls":["https://s3.amazonaws.com/pd-static-content/public-docs/pandadoc-panda-bear.png"]}],"pricing_tables":[{"name":"Pricing Table 1","data_merge":true,"options":{"Tax":{"type":"percent","name":"Tax","value":10},"Fee":{"type":"percent","name":"Fee","value":5}},"sections":[{"title":"Sample Section","default":true,"rows":[{"options":{"optional":true,"optional_selected":true,"qty_editable":true},"data":{"Name":"Toy Panda","Description":"Fluffy!","Price":10,"QTY":3,"Tax":{"value":20,"type":"percent"},"Fee":{"value":5,"type":"percent"}},"custom_fields":{"Fluffiness":"5 / 5"}}]}]}]} # DocumentCreateRequest | 
    editor_ver = 'ev2' # str | Set this parameter as `ev1` if you want to create a document from PDF with Classic Editor when both editors are enabled for the workspace. (optional)
    use_form_field_properties = 'true' # str | Set this parameter as `yes` or `1` or `true` (only when upload pdf with form fields) if you want to  respect form fields properties, like `required`. (optional)

    try:
        # Create Document
        api_response = api_instance.create_document(document_create_request, editor_ver=editor_ver, use_form_field_properties=use_form_field_properties)
        print("The response of DocumentsApi->create_document:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentsApi->create_document: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_create_request** | [**DocumentCreateRequest**](DocumentCreateRequest.md)|  | 
 **editor_ver** | **str**| Set this parameter as &#x60;ev1&#x60; if you want to create a document from PDF with Classic Editor when both editors are enabled for the workspace. | [optional] 
 **use_form_field_properties** | **str**| Set this parameter as &#x60;yes&#x60; or &#x60;1&#x60; or &#x60;true&#x60; (only when upload pdf with form fields) if you want to  respect form fields properties, like &#x60;required&#x60;. | [optional] 

### Return type

[**DocumentCreateResponse**](DocumentCreateResponse.md)

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
**403** | Permission error |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_document_editing_session**
> CreateDocumentEditingSession201Response create_document_editing_session(id, editing_session_request)

Create Document Editing Session 

Creates a new editing session for the Embedded Editor. The response includes an E-Token, which is required to open the document.

> 🚧 **Important:** The Embedded Editor can only open documents that have a `draft` status.

#### Limitations

- **Single Active Session per User-Document Pair** 
  Only one editing session can be active at a time for a specific user and document. Creating a new session for the same user-document pair will automatically invalidate the previous one.

- **Weekly Session Cap** 
  A maximum of **250** editing sessions can be created for a single document per week. Any attempt to exceed this limit will result in a `403 Forbidden` error.


### Example

* Api Key Authentication (apiKey):
* OAuth Authentication (oauth2):

```python
import pandadoc_client
from pandadoc_client.models.create_document_editing_session201_response import CreateDocumentEditingSession201Response
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
    api_instance = pandadoc_client.DocumentsApi(api_client)
    id = 'pSgK5XYZjyg3zXYZxsoUWg' # str | Document ID
    editing_session_request = {"email":"john.doe@pandadoc.com","lifetime":100} # EditingSessionRequest | 

    try:
        # Create Document Editing Session 
        api_response = api_instance.create_document_editing_session(id, editing_session_request)
        print("The response of DocumentsApi->create_document_editing_session:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentsApi->create_document_editing_session: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Document ID | 
 **editing_session_request** | [**EditingSessionRequest**](EditingSessionRequest.md)|  | 

### Return type

[**CreateDocumentEditingSession201Response**](CreateDocumentEditingSession201Response.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Document Editing Session created |  -  |
**400** | Bad request |  -  |
**401** | Authentication error |  -  |
**403** | Permission error |  -  |
**404** | Not found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_document_from_upload**
> DocumentCreateResponse create_document_from_upload(editor_ver=editor_ver, use_form_field_properties=use_form_field_properties, file=file, data=data)

Create Document from File Upload

## Create from an upload
> See the [Create from PDF](https://developers.pandadoc.com/docs/create-document-from-file) tutorial for the usage specifics and sample PDF files.

**Note**: A file you upload is not stored in your PandaDoc account, so you have to upload it with every request.


### Example

* Api Key Authentication (apiKey):
* OAuth Authentication (oauth2):

```python
import pandadoc_client
from pandadoc_client.models.document_create_by_pdf_request import DocumentCreateByPdfRequest
from pandadoc_client.models.document_create_response import DocumentCreateResponse
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
    api_instance = pandadoc_client.DocumentsApi(api_client)
    editor_ver = 'ev2' # str | Set this parameter as `ev1` if you want to create a document from PDF with Classic Editor when both editors are enabled for the workspace. (optional)
    use_form_field_properties = 'true' # str | Set this parameter as `yes` or `1` or `true` (only when upload pdf with form fields) if you want to  respect form fields properties, like `required`. (optional)
    file = None # bytearray | Binary PDF File (optional)
    data = pandadoc_client.DocumentCreateByPdfRequest() # DocumentCreateByPdfRequest |  (optional)

    try:
        # Create Document from File Upload
        api_response = api_instance.create_document_from_upload(editor_ver=editor_ver, use_form_field_properties=use_form_field_properties, file=file, data=data)
        print("The response of DocumentsApi->create_document_from_upload:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentsApi->create_document_from_upload: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **editor_ver** | **str**| Set this parameter as &#x60;ev1&#x60; if you want to create a document from PDF with Classic Editor when both editors are enabled for the workspace. | [optional] 
 **use_form_field_properties** | **str**| Set this parameter as &#x60;yes&#x60; or &#x60;1&#x60; or &#x60;true&#x60; (only when upload pdf with form fields) if you want to  respect form fields properties, like &#x60;required&#x60;. | [optional] 
 **file** | **bytearray**| Binary PDF File | [optional] 
 **data** | [**DocumentCreateByPdfRequest**](DocumentCreateByPdfRequest.md)|  | [optional] 

### Return type

[**DocumentCreateResponse**](DocumentCreateResponse.md)

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

# **create_document_link**
> DocumentCreateLinkResponse create_document_link(id, document_create_link_request)

Create Document Session for Embedded Sign

Creates a document session for a recipient to view and sign a document.

> 📘 How to create an Embedded Sign session
> For more information on how to create an Embedded Sign session, see the [Embedded Signing](https://developers.pandadoc.com/docs/embedded-signing) documentation.


### Example

* Api Key Authentication (apiKey):
* OAuth Authentication (oauth2):

```python
import pandadoc_client
from pandadoc_client.models.document_create_link_request import DocumentCreateLinkRequest
from pandadoc_client.models.document_create_link_response import DocumentCreateLinkResponse
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
    api_instance = pandadoc_client.DocumentsApi(api_client)
    id = 'ZPeAfcpzr9aiVs5vqUf6jg' # str | Document ID
    document_create_link_request = {"recipient":"test@mail.com","lifetime":900} # DocumentCreateLinkRequest | 

    try:
        # Create Document Session for Embedded Sign
        api_response = api_instance.create_document_link(id, document_create_link_request)
        print("The response of DocumentsApi->create_document_link:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentsApi->create_document_link: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Document ID | 
 **document_create_link_request** | [**DocumentCreateLinkRequest**](DocumentCreateLinkRequest.md)|  | 

### Return type

[**DocumentCreateLinkResponse**](DocumentCreateLinkResponse.md)

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
**403** | Permission error |  -  |
**404** | Not found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_export_docx_task**
> DocumentDocxExport create_export_docx_task(document_id)

[Beta] Create DOCX Export Task

> ⏱️ Export as DOCX is a non-blocking (asynchronous) operation
> The document generation process may take some time.
> With a successful request, you receive a response with task ID, status **created** and document id. After process completes, usually in a few minutes, the task status moves to the **done** state.
> You can download documents up to 300 pages. For documents of 301+ pages, you will receive an error “400: The number of pages more then limit 300”


### Example

* Api Key Authentication (apiKey):
* OAuth Authentication (oauth2):

```python
import pandadoc_client
from pandadoc_client.models.document_docx_export import DocumentDocxExport
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
    api_instance = pandadoc_client.DocumentsApi(api_client)
    document_id = 'BhVzRcxH9Z2LgfPPGXFUBa' # str | Specify document id.

    try:
        # [Beta] Create DOCX Export Task
        api_response = api_instance.create_export_docx_task(document_id)
        print("The response of DocumentsApi->create_export_docx_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentsApi->create_export_docx_task: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_id** | **str**| Specify document id. | 

### Return type

[**DocumentDocxExport**](DocumentDocxExport.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Export DOCX task was created. |  -  |
**401** | Authentication error |  -  |
**403** | Permission error |  -  |
**404** | Not found error |  -  |
**429** | Too many requests error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_document**
> delete_document(id)

Delete Document

Delete a document by ID.


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
    api_instance = pandadoc_client.DocumentsApi(api_client)
    id = 'BhVzRcxH9Z2LgfPPGXFUBa' # str | Document ID

    try:
        # Delete Document
        api_instance.delete_document(id)
    except Exception as e:
        print("Exception when calling DocumentsApi->delete_document: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Document ID | 

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
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **details_document**
> DocumentDetailsResponse details_document(id)

Document Details

Return detailed data about a document. Use Document Status for getting just a basic info and status.

Get details about a document by its `id`. Details include:

- Basic document information (name, document state, owner, sender, grand total, etc.)
- Recipients (completion status, signing order, etc.)
- Fields with values (incl. Collect Files field)
- Tokens (variables) with values
- Pricing information (pricing tables, products, quotes, etc.)
- Content block names for table, image, and text blocks (tables, images, texts)
- Metadata
- Tags
- Linked objects
- [Approval flow](https://support.pandadoc.com/en/articles/9714799-approval-workflow) (if present)
- Timestamps associated with a document. Note that `date_modified` means any changes associated with the recipients and document status, while `content_date_modified` reflects any changes in the document content.


### Example

* Api Key Authentication (apiKey):
* OAuth Authentication (oauth2):

```python
import pandadoc_client
from pandadoc_client.models.document_details_response import DocumentDetailsResponse
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
    api_instance = pandadoc_client.DocumentsApi(api_client)
    id = 'BhVzRcxH9Z2LgfPPGXFUBa' # str | Document ID

    try:
        # Document Details
        api_response = api_instance.details_document(id)
        print("The response of DocumentsApi->details_document:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentsApi->details_document: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Document ID | 

### Return type

[**DocumentDetailsResponse**](DocumentDetailsResponse.md)

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
**409** | Conflict |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **document_e_sign_disclosure**
> DocumentESignDisclosure document_e_sign_disclosure(document_id)

Document eSign disclosure

Retrieves the current version of eSign disclosure text for a specified document.


### Example

* Api Key Authentication (apiKey):
* OAuth Authentication (oauth2):

```python
import pandadoc_client
from pandadoc_client.models.document_e_sign_disclosure import DocumentESignDisclosure
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
    api_instance = pandadoc_client.DocumentsApi(api_client)
    document_id = 'BhVzRcxH9Z2LgfPPGXFUBa' # str | The UUID of the document.

    try:
        # Document eSign disclosure
        api_response = api_instance.document_e_sign_disclosure(document_id)
        print("The response of DocumentsApi->document_e_sign_disclosure:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentsApi->document_e_sign_disclosure: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_id** | **str**| The UUID of the document. | 

### Return type

[**DocumentESignDisclosure**](DocumentESignDisclosure.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ESign disclosure text retrieved successfully. |  -  |
**401** | Authentication error |  -  |
**403** | Permission error |  -  |
**404** | Not found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **document_move_to_folder**
> document_move_to_folder(id, folder_id)

Document move to folder

This operation allows you to move a document to a folder by specifying the document ID and folder ID.

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
    api_instance = pandadoc_client.DocumentsApi(api_client)
    id = 'ZPeAfcpzr9aiVs5vqUf6jg' # str | Specify document ID.
    folder_id = 'ZPeAfcpzr9aiVs5vqUf6jg' # str | Specify folder ID.

    try:
        # Document move to folder
        api_instance.document_move_to_folder(id, folder_id)
    except Exception as e:
        print("Exception when calling DocumentsApi->document_move_to_folder: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Specify document ID. | 
 **folder_id** | **str**| Specify folder ID. | 

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
**401** | Authentication error |  -  |
**403** | Permission error |  -  |
**404** | Not found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **document_revert_to_draft**
> DocumentRevertToDraftResponse document_revert_to_draft(id)

Move Document to Draft

Revert your document back to draft to continue editing it.

> 📘 Returning to Draft works for any document status except Removed.

## After you move your document to the Draft status

- `Signature` and `Initials` fields are cleared. All other fields stay filled in.
- Recipients are **not** notified that the document is back in Draft.
- You'll need to resend the document so that recipients can sign the updated version.


### Example

* Api Key Authentication (apiKey):
* OAuth Authentication (oauth2):

```python
import pandadoc_client
from pandadoc_client.models.document_revert_to_draft_response import DocumentRevertToDraftResponse
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
    api_instance = pandadoc_client.DocumentsApi(api_client)
    id = 'iGsFiaV2hEEvQdhr2WAkMk' # str | Specify document ID.

    try:
        # Move Document to Draft
        api_response = api_instance.document_revert_to_draft(id)
        print("The response of DocumentsApi->document_revert_to_draft:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentsApi->document_revert_to_draft: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Specify document ID. | 

### Return type

[**DocumentRevertToDraftResponse**](DocumentRevertToDraftResponse.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_document**
> bytearray download_document(id, watermark_color=watermark_color, watermark_font_size=watermark_font_size, watermark_opacity=watermark_opacity, watermark_text=watermark_text, separate_files=separate_files)

Document Download

Download documents as a PDF.


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
    api_instance = pandadoc_client.DocumentsApi(api_client)
    id = 'BhVzRcxH9Z2LgfPPGXFUBa' # str | Specify document ID.
    watermark_color = '#FF5733' # str | HEX code (for example `#FF5733`). (optional)
    watermark_font_size = 12 # int | Font size of the watermark. (optional)
    watermark_opacity = 0.5 # float | In range 0.0-1.0 (optional)
    watermark_text = 'John Doe inc.' # str | Specify watermark text. (optional)
    separate_files = False # bool | Download document bundle as a zip-archive of separate PDFs (1 file per section). (optional) (default to False)

    try:
        # Document Download
        api_response = api_instance.download_document(id, watermark_color=watermark_color, watermark_font_size=watermark_font_size, watermark_opacity=watermark_opacity, watermark_text=watermark_text, separate_files=separate_files)
        print("The response of DocumentsApi->download_document:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentsApi->download_document: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Specify document ID. | 
 **watermark_color** | **str**| HEX code (for example &#x60;#FF5733&#x60;). | [optional] 
 **watermark_font_size** | **int**| Font size of the watermark. | [optional] 
 **watermark_opacity** | **float**| In range 0.0-1.0 | [optional] 
 **watermark_text** | **str**| Specify watermark text. | [optional] 
 **separate_files** | **bool**| Download document bundle as a zip-archive of separate PDFs (1 file per section). | [optional] [default to False]

### Return type

**bytearray**

### Authorization

[apiKey](../README.md#apiKey), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/pdf, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Authentication error |  -  |
**403** | Permission error |  -  |
**404** | Not found |  -  |
**409** | Conflict |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_protected_document**
> bytearray download_protected_document(id, separate_files=separate_files)

Download Completed Document

Download a completed document as a verifiable PDF (Download Protected Document)
> 🚧 Production key only
> 
> This endpoint only works with a Production key. You'll get a 401 Unauthorized error when trying to use a Sandbox key.

Download a signed PDF of a completed document


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
    api_instance = pandadoc_client.DocumentsApi(api_client)
    id = 'Mebvyy3NGsGBnY2rPLkH84' # str | Specify document ID.
    separate_files = False # bool | Download document bundle as a zip-archive of separate PDFs (1 file per section). (optional) (default to False)

    try:
        # Download Completed Document
        api_response = api_instance.download_protected_document(id, separate_files=separate_files)
        print("The response of DocumentsApi->download_protected_document:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentsApi->download_protected_document: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Specify document ID. | 
 **separate_files** | **bool**| Download document bundle as a zip-archive of separate PDFs (1 file per section). | [optional] [default to False]

### Return type

**bytearray**

### Authorization

[apiKey](../README.md#apiKey), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/pdf, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Authentication error |  -  |
**403** | Permission error |  -  |
**404** | Not found |  -  |
**409** | Conflict |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_docx_export_task**
> DocxExportTaskResponse get_docx_export_task(document_id, task_id)

[Beta] DOCX Export Task

> 📘 This endpoint returns the current state of a DOCX export task for a document.
> The endpoint supports downloading only multiple files if the document contains several sections. Downloading as a single file in this case is not possible.


### Example

* Api Key Authentication (apiKey):
* OAuth Authentication (oauth2):

```python
import pandadoc_client
from pandadoc_client.models.docx_export_task_response import DocxExportTaskResponse
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
    api_instance = pandadoc_client.DocumentsApi(api_client)
    document_id = 'BhVzRcxH9Z2LgfPPGXFUBa' # str | Specify document id.
    task_id = 'nPh2PDhFdDqAES9k64h9qX' # str | Specify Task id.

    try:
        # [Beta] DOCX Export Task
        api_response = api_instance.get_docx_export_task(document_id, task_id)
        print("The response of DocumentsApi->get_docx_export_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentsApi->get_docx_export_task: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_id** | **str**| Specify document id. | 
 **task_id** | **str**| Specify Task id. | 

### Return type

[**DocxExportTaskResponse**](DocxExportTaskResponse.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Got state of export DOCX task. |  -  |
**401** | Authentication error |  -  |
**403** | Permission error |  -  |
**404** | Not found error |  -  |
**429** | Too many requests error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_documents**
> DocumentListResponse list_documents(template_id=template_id, form_id=form_id, folder_uuid=folder_uuid, contact_id=contact_id, count=count, page=page, order_by=order_by, created_from=created_from, created_to=created_to, deleted=deleted, id=id, completed_from=completed_from, completed_to=completed_to, membership_id=membership_id, metadata=metadata, modified_from=modified_from, modified_to=modified_to, q=q, status=status, status__ne=status__ne, tag=tag)

List Documents

This endpoint will let you list and search for the documents.
### [Here](https://developers.pandadoc.com/docs/list-search-documents-api) you can find how to filter, search and order documents.


### Example

* Api Key Authentication (apiKey):
* OAuth Authentication (oauth2):

```python
import pandadoc_client
from pandadoc_client.models.document_list_response import DocumentListResponse
from pandadoc_client.models.document_ordering_fields_enum import DocumentOrderingFieldsEnum
from pandadoc_client.models.document_status_request_enum import DocumentStatusRequestEnum
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
    api_instance = pandadoc_client.DocumentsApi(api_client)
    template_id = 'BhVzRcxH9Z2LgfPPGXFUBa' # str | Filters by parent template. This Parameter can't be used with form_id. (optional)
    form_id = 'BhVzRcxH9Z2LgfPPGXFUBa' # str | Filters by parent form. This parameter can't be used with template_id. (optional)
    folder_uuid = 'BhVzRcxH9Z2LgfPPGXFUBa' # str | Filters by the folder where the documents are stored. (optional)
    contact_id = '9FeAY2NB3C9qDdtQRb4tTL' # str | Filters by recipient or approver with this 'contact_id'. (optional)
    count = 50 # int | Limits the size of the response. Default is 50 documents, maximum is 100 documents. (optional)
    page = 1 # int | Paginates the search result. Increase value to get the next page of results. (optional)
    order_by = date_status_changed # DocumentOrderingFieldsEnum | Defines the sorting of the result. Use `date_created` for ASC and `-date_created` for DESC sorting. (optional) (default to date_status_changed)
    created_from = '2024-10-27T15:22:23.132757Z' # str | Limits results to the documents with the `date_created` greater than or equal to this value. (optional)
    created_to = '2024-10-27T15:22:23.132757Z' # str | Limits results to the documents with the `date_created` less than this value. (optional)
    deleted = false # bool | Returns only the deleted documents. (optional)
    id = 'BhVzRcxH9Z2LgfPPGXFUBa' # str |  (optional)
    completed_from = '2024-10-27T15:22:23.132757Z' # str | Limits results to the documents with the `date_completed` greater than or equal to this value. (optional)
    completed_to = '2024-10-27T15:22:23.132757Z' # str | Limits results to the documents with the `date_completed` less than this value. (optional)
    membership_id = 'BhVzRcxH9Z2LgfPPGXFUBa' # str | Filter documents by the owner's 'membership_id'. (optional)
    metadata = ['[\"metadata_opportunity_id=2181432\",\"metadata_custom_key=custom_value\"]'] # List[str] | Filters documents by metadata. Pass metadata in the format of `metadata_{metadata-key}={metadata-value}` such as `metadata_opportunity_id=2181432`. The `metadata_` prefix is always required. (optional)
    modified_from = '2024-10-27T15:22:23.132757Z' # str | Limits results to the documents with the `date_modified` greater than or equal to this value. (optional)
    modified_to = '2024-10-27T15:22:23.132757Z' # str | Limits results to the documents with the `date_modified` less than this value. (optional)
    q = 'Sample Document' # str | Filters documents by name or reference number (stored on the template level). (optional)
    status = pandadoc_client.DocumentStatusRequestEnum() # DocumentStatusRequestEnum | Filters documents by the status.   * 0: document.draft   * 1: document.sent   * 2: document.completed   * 3: document.uploaded   * 4: document.error   * 5: document.viewed   * 6: document.waiting_approval   * 7: document.approved   * 8: document.rejected   * 9: document.waiting_pay   * 10: document.paid   * 11: document.voided   * 12: document.declined   * 13: document.external_review  (optional)
    status__ne = pandadoc_client.DocumentStatusRequestEnum() # DocumentStatusRequestEnum | Exludes documents with this status.   * 0: document.draft   * 1: document.sent   * 2: document.completed   * 3: document.uploaded   * 4: document.error   * 5: document.viewed   * 6: document.waiting_approval   * 7: document.approved   * 8: document.rejected   * 9: document.waiting_pay   * 10: document.paid   * 11: document.voided   * 12: document.declined   * 13: document.external_review  (optional)
    tag = 'tag_1' # str | Filters documents by tag. (optional)

    try:
        # List Documents
        api_response = api_instance.list_documents(template_id=template_id, form_id=form_id, folder_uuid=folder_uuid, contact_id=contact_id, count=count, page=page, order_by=order_by, created_from=created_from, created_to=created_to, deleted=deleted, id=id, completed_from=completed_from, completed_to=completed_to, membership_id=membership_id, metadata=metadata, modified_from=modified_from, modified_to=modified_to, q=q, status=status, status__ne=status__ne, tag=tag)
        print("The response of DocumentsApi->list_documents:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentsApi->list_documents: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**| Filters by parent template. This Parameter can&#39;t be used with form_id. | [optional] 
 **form_id** | **str**| Filters by parent form. This parameter can&#39;t be used with template_id. | [optional] 
 **folder_uuid** | **str**| Filters by the folder where the documents are stored. | [optional] 
 **contact_id** | **str**| Filters by recipient or approver with this &#39;contact_id&#39;. | [optional] 
 **count** | **int**| Limits the size of the response. Default is 50 documents, maximum is 100 documents. | [optional] 
 **page** | **int**| Paginates the search result. Increase value to get the next page of results. | [optional] 
 **order_by** | [**DocumentOrderingFieldsEnum**](.md)| Defines the sorting of the result. Use &#x60;date_created&#x60; for ASC and &#x60;-date_created&#x60; for DESC sorting. | [optional] [default to date_status_changed]
 **created_from** | **str**| Limits results to the documents with the &#x60;date_created&#x60; greater than or equal to this value. | [optional] 
 **created_to** | **str**| Limits results to the documents with the &#x60;date_created&#x60; less than this value. | [optional] 
 **deleted** | **bool**| Returns only the deleted documents. | [optional] 
 **id** | **str**|  | [optional] 
 **completed_from** | **str**| Limits results to the documents with the &#x60;date_completed&#x60; greater than or equal to this value. | [optional] 
 **completed_to** | **str**| Limits results to the documents with the &#x60;date_completed&#x60; less than this value. | [optional] 
 **membership_id** | **str**| Filter documents by the owner&#39;s &#39;membership_id&#39;. | [optional] 
 **metadata** | [**List[str]**](str.md)| Filters documents by metadata. Pass metadata in the format of &#x60;metadata_{metadata-key}&#x3D;{metadata-value}&#x60; such as &#x60;metadata_opportunity_id&#x3D;2181432&#x60;. The &#x60;metadata_&#x60; prefix is always required. | [optional] 
 **modified_from** | **str**| Limits results to the documents with the &#x60;date_modified&#x60; greater than or equal to this value. | [optional] 
 **modified_to** | **str**| Limits results to the documents with the &#x60;date_modified&#x60; less than this value. | [optional] 
 **q** | **str**| Filters documents by name or reference number (stored on the template level). | [optional] 
 **status** | [**DocumentStatusRequestEnum**](.md)| Filters documents by the status.   * 0: document.draft   * 1: document.sent   * 2: document.completed   * 3: document.uploaded   * 4: document.error   * 5: document.viewed   * 6: document.waiting_approval   * 7: document.approved   * 8: document.rejected   * 9: document.waiting_pay   * 10: document.paid   * 11: document.voided   * 12: document.declined   * 13: document.external_review  | [optional] 
 **status__ne** | [**DocumentStatusRequestEnum**](.md)| Exludes documents with this status.   * 0: document.draft   * 1: document.sent   * 2: document.completed   * 3: document.uploaded   * 4: document.error   * 5: document.viewed   * 6: document.waiting_approval   * 7: document.approved   * 8: document.rejected   * 9: document.waiting_pay   * 10: document.paid   * 11: document.voided   * 12: document.declined   * 13: document.external_review  | [optional] 
 **tag** | **str**| Filters documents by tag. | [optional] 

### Return type

[**DocumentListResponse**](DocumentListResponse.md)

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
**403** | Permission error |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_document**
> DocumentSendResponse send_document(id, document_send_request)

Send Document

> 🚧 Using the Sandbox Key
> 
> When you use a [sandbox API key](https://developers.pandadoc.com/reference/sandbox-key) during the free trial period, the sender and recipient email addresses must be from the same organisation (email domain).

## Document State

- You can only send a document in the `document.draft` status.
- After creating a new document, it usually retains a `document.uploaded` status for 3-5 seconds while the document syncs across PandaDoc servers. When the document is available for further API calls, it moves to the `document.draft` state. Use [Document Status](/reference/document-status) or [Webhooks](/reference/on-document-status-change) to check document status.
- Moving a document to the `document.sent` status finalizes the document structure, before recipients can complete it.
- If a template used for the document creation has an approval workflow turned on, the sent document moves to the `document.waiting_approval` status. Once the document is approved, you need to make the call again to move the document to `document.sent` status.

## Send and Silence Notifications

- By default, PandaDoc sends a notification email to the recipient, as well as notifications the sender has configured. You may disable all notifications for recipients by passing `silent: true`. This is useful when you are using alternative delivery methods such as linking to the document or embedding the document.
- The `silent: true` parameter disables sent, viewed, comment and completed document email notifications. "Document Approval" notification won't be affected by this parameter.
- If you pass `silent: false`, the document is going to be delivered by email and/or SMS. 

![Example email. Branding can be changed in workspace settings](https://files.readme.io/cc5a03e-email2.png)

## Select Approver from Group

If you have previously set up an approval workflow with selectable groups on the UI, you can select a particular approver from this group. Learn more about [selectable groups](https://support.pandadoc.com/en/articles/9714799-approval-workflow#h_01H4GNY5GSGG38BPYY46XV7GB4).  
To set an approver, we recommend to follow these steps:

1. Run the [Document Details](https://developers.pandadoc.com/reference/document-details) request.
2. Copy the `steps` part from the `approval_execution` section of the response into the `selected_approvers` field of the Send Document payload.
3. Modify your payload according to business needs: set `is_selected` to true for one approver.

> 📘 **Note**: You can change the selected approver only if you revert your document back to the `document.draft` status.


### Example

* Api Key Authentication (apiKey):
* OAuth Authentication (oauth2):

```python
import pandadoc_client
from pandadoc_client.models.document_send_request import DocumentSendRequest
from pandadoc_client.models.document_send_response import DocumentSendResponse
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
    api_instance = pandadoc_client.DocumentsApi(api_client)
    id = 'ZPeAfcpzr9aiVs5vqUf6jg' # str | Document ID
    document_send_request = pandadoc_client.DocumentSendRequest() # DocumentSendRequest | 

    try:
        # Send Document
        api_response = api_instance.send_document(id, document_send_request)
        print("The response of DocumentsApi->send_document:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentsApi->send_document: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Document ID | 
 **document_send_request** | [**DocumentSendRequest**](DocumentSendRequest.md)|  | 

### Return type

[**DocumentSendResponse**](DocumentSendResponse.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Authentication error |  -  |
**403** | Permission error |  -  |
**404** | Not found |  -  |
**409** | Conflict |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **status_document**
> DocumentStatusResponse status_document(id)

Document Status

It is useful to request document status to ensure a document is in the expected state before calling additional API methods. 

### Required Document Statuses

Here are some common methods and the `document.status` required to proceed:

| API Method           | Required Document State |
| :------------------- | :---------------------- |
| Send A Document      | `document.draft`        |
| Get Document Details | `document.draft`        |
| Embed A Document     | `document.sent`         |
| Download A Document  | `document.completed`    |

> 📘 Polling vs Webhooks
> 
> If you are using the `GET` document status endpoint for [**polling**](https://en.wikipedia.org/wiki/Polling_(computer_science)), we also support and recommend using **webhooks** for event-driven needs: <https://developers.pandadoc.com/docs/listen-document-status-changes#/>

### Available Document Statuses

The following is a complete list of all possible document statuses returned:

| Document Status             | Status Description                                                                                                                                                                                                               |
| :-------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `document.uploaded`         | The document has just been created or uploaded. It is in processing and will be in `document.draft` state soon.                                                                                                           |
| `document.error`            | The document creation has failed. This status is terminal, you should stop polling after getting it.
| `document.draft`            | The document is in a draft state. All aspects of the document can be edited in this state. Our API does not support edits after the document has been created, but it can still be edited manually on <https://app.pandadoc.com> |
| `document.sent`             | The document has been "sealed" and optionally sent. No further document edits can occur except for document recipient(s) filling out or signing the document.                                                                    |
| `document.viewed`           | Document recipient(s) have viewed the sent document.                                                                                                                                                                             |
| `document.waiting_approval` | The document has an [automatic approval workflow](https://support.pandadoc.com/en/articles/9714799-approval-workflow) and has not yet been approved.                                                      |
| `document.rejected`         | The document has an [automatic approval workflow](https://support.pandadoc.com/en/articles/9714799-approval-workflow) and was rejected.                                                                   |
| `document.approved`         | The document has an [automatic approval workflow](https://support.pandadoc.com/en/articles/9714799-approval-workflow) and was approved.                                                                   |
| `document.waiting_pay`      | The document has a [Stripe payment](https://support.pandadoc.com/en/articles/9714942-stripe-checkout-payments) option and is awaiting payment.                                                                              |
| `document.paid`             | The document has a [Stripe payment](https://support.pandadoc.com/en/articles/9714942-stripe-checkout-payments) option and was paid.                                                                                         |
| `document.completed`        | The document has been completed by all recipients.                                                                                                                                                                               |
| `document.voided`           | The document expired and is no longer available for completion or signature.                                                                                                                                                     |
| `document.declined`         | The document was [manually marked](https://support.pandadoc.com/en/articles/9714842-manually-change-document-status) as "Declined"                                                                                    |
| `document.external_review`  | The document is reviewed by it's recipient using Suggest Edit feature                                                                                                                                                            |


### Example

* Api Key Authentication (apiKey):
* OAuth Authentication (oauth2):

```python
import pandadoc_client
from pandadoc_client.models.document_status_response import DocumentStatusResponse
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
    api_instance = pandadoc_client.DocumentsApi(api_client)
    id = 'fANp5wW5EwY7AkiTkTGekZ' # str | Specify document ID.

    try:
        # Document Status
        api_response = api_instance.status_document(id)
        print("The response of DocumentsApi->status_document:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentsApi->status_document: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Specify document ID. | 

### Return type

[**DocumentStatusResponse**](DocumentStatusResponse.md)

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

# **transfer_all_documents_ownership**
> transfer_all_documents_ownership(document_transfer_all_ownership_request)

Transfer all documents ownership

This method transfers ownership of all documents from one member to another.


### Example

* Api Key Authentication (apiKey):
* OAuth Authentication (oauth2):

```python
import pandadoc_client
from pandadoc_client.models.document_transfer_all_ownership_request import DocumentTransferAllOwnershipRequest
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
    api_instance = pandadoc_client.DocumentsApi(api_client)
    document_transfer_all_ownership_request = pandadoc_client.DocumentTransferAllOwnershipRequest() # DocumentTransferAllOwnershipRequest | 

    try:
        # Transfer all documents ownership
        api_instance.transfer_all_documents_ownership(document_transfer_all_ownership_request)
    except Exception as e:
        print("Exception when calling DocumentsApi->transfer_all_documents_ownership: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_transfer_all_ownership_request** | [**DocumentTransferAllOwnershipRequest**](DocumentTransferAllOwnershipRequest.md)|  | 

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
**401** | Authentication error |  -  |
**403** | Permission error |  -  |
**404** | Not found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transfer_document_ownership**
> transfer_document_ownership(id, document_transfer_ownership_request)

Update document ownership

This operation allows transferring the ownership of a document to another user by specifying the document ID and membership ID.

### Example

* Api Key Authentication (apiKey):
* OAuth Authentication (oauth2):

```python
import pandadoc_client
from pandadoc_client.models.document_transfer_ownership_request import DocumentTransferOwnershipRequest
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
    api_instance = pandadoc_client.DocumentsApi(api_client)
    id = 'BhVzRcxH9Z2LgfPPGXFUBa' # str | Specify document ID.
    document_transfer_ownership_request = pandadoc_client.DocumentTransferOwnershipRequest() # DocumentTransferOwnershipRequest | 

    try:
        # Update document ownership
        api_instance.transfer_document_ownership(id, document_transfer_ownership_request)
    except Exception as e:
        print("Exception when calling DocumentsApi->transfer_document_ownership: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Specify document ID. | 
 **document_transfer_ownership_request** | [**DocumentTransferOwnershipRequest**](DocumentTransferOwnershipRequest.md)|  | 

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
**401** | Authentication error |  -  |
**403** | Permission error |  -  |
**404** | Not found |  -  |
**409** | Conflict |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_document**
> update_document(id, document_update_request)

Update Document

Use the PATCH method to update a PandaDoc document.

> 🚧 Document status
> 
> You can only update a document in the Draft status (`document.draft`). 
> 
> After creating a new document, it usually retains a `document.uploaded` status for 3-5 seconds while the document syncs across PandaDoc servers. When the document is available for further API calls, the document moves to the `document.draft` state. Use [Document Status](https://developers.pandadoc.com/reference/document-status) or Webhooks to check document status.


### Example

* Api Key Authentication (apiKey):
* OAuth Authentication (oauth2):

```python
import pandadoc_client
from pandadoc_client.models.document_update_request import DocumentUpdateRequest
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
    api_instance = pandadoc_client.DocumentsApi(api_client)
    id = 'BhVzRcxH9Z2LgfPPGXFUBa' # str | Document ID
    document_update_request = {"texts":[{"name":"Legal Terms Section","data":"## Terms of Service\nThis document outlines the terms and conditions. \n- **Acceptance:** By using our service, you agree to these terms.\n"},{"name":"Product Description","data":"## Product Description\nGeneral description of the product.\n"}]} # DocumentUpdateRequest | 

    try:
        # Update Document
        api_instance.update_document(id, document_update_request)
    except Exception as e:
        print("Exception when calling DocumentsApi->update_document: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Document ID | 
 **document_update_request** | [**DocumentUpdateRequest**](DocumentUpdateRequest.md)|  | 

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

