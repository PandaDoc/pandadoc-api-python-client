# pandadoc_client.DocumentRecipientsApi

All URIs are relative to *https://api.pandadoc.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_document_recipient**](DocumentRecipientsApi.md#add_document_recipient) | **POST** /public/v1/documents/{id}/recipients | Add Document Recipient
[**delete_document_recipient**](DocumentRecipientsApi.md#delete_document_recipient) | **DELETE** /public/v1/documents/{id}/recipients/{recipient_id} | Delete Document Recipient
[**edit_document_recipient**](DocumentRecipientsApi.md#edit_document_recipient) | **PATCH** /public/v1/documents/{id}/recipients/recipient/{recipient_id} | Update Document Recipient
[**reassign_document_recipient**](DocumentRecipientsApi.md#reassign_document_recipient) | **POST** /public/v1/documents/{id}/recipients/{recipient_id}/reassign | Change Signer (Reassign Document Recipient)


# **add_document_recipient**
> DocumentRecipientResponse add_document_recipient(id, document_recipient_create_request)

Add Document Recipient

Add a CC recipient to a document.

> 🚧 Before you start
> 
> To add a CC recipient, please ensure that:
> 
> - You have the 'Can Manage Recipients' permission.
> - This recipient is already created in your contacts. If not, add them using the [Create Contact](https://developers.pandadoc.com/reference/create-contact) endpoint.

To add a new CC recipient to a document, two parameters must be included in the request body:

- `kind`: Set this parameter to `contact` to specify an individual contact.
- `id`:  Input the ID of the desired contact.

To retrieve the contact's ID, use the [List Contacts](https://developers.pandadoc.com/reference/list-contacts) endpoint to access a list of all contacts, and then locate the desired contact by searching using the name or email address within the returned list.

### Document status

You can add CC recipients in any document status except for the 'Expired' (`document.voided`) and 'Declined' (`document.declined`).

> 📘 Email notification to access the document
> 
> **Note**: When a document is in one of the following statuses: 'Sent' (`document.sent`), 'Viewed' (`document.viewed`), 'Completed' (`document.completed`), 'Waiting for Payment' (`document.waiting_pay`), or 'Paid' (`document.paid`), any added CC recipient will receive an instant notification at their email address, allowing them access to the document.


### Example

* Api Key Authentication (apiKey):
* OAuth Authentication (oauth2):

```python
import pandadoc_client
from pandadoc_client.models.document_recipient_create_request import DocumentRecipientCreateRequest
from pandadoc_client.models.document_recipient_response import DocumentRecipientResponse
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
    api_instance = pandadoc_client.DocumentRecipientsApi(api_client)
    id = 'BhVzRcxH9Z2LgfPPGXFUBa' # str | Document UUID
    document_recipient_create_request = {"id":"pGkLnJUAx99JpXJy5DVD30","kind":"contact"} # DocumentRecipientCreateRequest | 

    try:
        # Add Document Recipient
        api_response = api_instance.add_document_recipient(id, document_recipient_create_request)
        print("The response of DocumentRecipientsApi->add_document_recipient:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentRecipientsApi->add_document_recipient: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Document UUID | 
 **document_recipient_create_request** | [**DocumentRecipientCreateRequest**](DocumentRecipientCreateRequest.md)|  | 

### Return type

[**DocumentRecipientResponse**](DocumentRecipientResponse.md)

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
**403** | Permission error |  -  |
**404** | Not found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_document_recipient**
> delete_document_recipient(id, recipient_id)

Delete Document Recipient

Remove a recipient from a document.

> 🚧 Before you start
> 
> Please ensure that you have the 'Can Manage Recipients' permission.

To remove a recipient from a document, you must specify their ID in the path parameter (note that this is different from their contact's ID). The recipient's ID can be retrieved via the [Document Details](https://developers.pandadoc.com/reference/document-details) endpoint.

### Document status

- Removing a signer is only possible when the document is in the 'Draft' (`document.draft`) status and this action will unassign all fields associated with that signer.
- Removing a CC recipient is allowed in any document status except for the 'Expired' (`document.voided`) and 'Declined' (`document.declined`). If a CC recipient is removed, their access will be revoked.


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
    api_instance = pandadoc_client.DocumentRecipientsApi(api_client)
    id = 'BhVzRcxH9Z2LgfPPGXFUBa' # str | Document UUID
    recipient_id = 'tf5dGS3Tmu3cj228ao6fnc' # str | Recipient UUID

    try:
        # Delete Document Recipient
        api_instance.delete_document_recipient(id, recipient_id)
    except Exception as e:
        print("Exception when calling DocumentRecipientsApi->delete_document_recipient: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Document UUID | 
 **recipient_id** | **str**| Recipient UUID | 

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

# **edit_document_recipient**
> edit_document_recipient(id, recipient_id, document_recipient_edit_request)

Update Document Recipient

Modify recipient's personal details.

> 🚧 Before you start
> 
> To edit a recipient, please ensure that you have the 'Can Edit Document' permission.

Use this endpoint to easily fix typos in a recipient's name or email, or to change any other recipient information in a sent document. 

> 📘 Please note that changes made to a recipient within a document will also update their `Contact` information. However, these changes will not update information about this recipient in other documents where they have already been added.

### Document status

- You can edit a signer in the following document statuses:
  - 'Draft' (`document.draft`),
  - 'Waiting Approval' (`document.waiting_approval`),
  - 'Approved' (`document.approved`),
  - 'Rejected' (`document.rejected`),
  - 'Sent' (`document.sent`),
  - 'Viewed' (`document.viewed`), but only until they have signed the document.
- You can edit a CC recipient in any document status **except**:
  - 'Expired' (`document.voided`),
  - 'Declined' (`document.declined`).

> 📘 Updating a recipient's email after sending a document
> 
> **Note**: If you update a recipient's email address after sending a document, they will receive an instant notification at the new email address, allowing them access to the document. Access via the previous email will be revoked.

### Restrictions for updating a recipient's email

- You cannot change emails of PandaDoc users.
- You cannot use the email addresses of existing contacts. If you need to use an email from an existing contact, use the [Change Signer](https://developers.pandadoc.com/reference/change-signer) endpoint to replace a signer with this contact.


### Example

* Api Key Authentication (apiKey):
* OAuth Authentication (oauth2):

```python
import pandadoc_client
from pandadoc_client.models.document_recipient_edit_request import DocumentRecipientEditRequest
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
    api_instance = pandadoc_client.DocumentRecipientsApi(api_client)
    id = 'BhVzRcxH9Z2LgfPPGXFUBa' # str | Document UUID.
    recipient_id = 'tf5dGS3Tmu3cj228ao6fnc' # str | Recipient UUID.
    document_recipient_edit_request = {"first_name":"New First Name","last_name":"New Last Name","phone":"+3511111111111","company":"PandaDoc","title":"","street_address":"","city":"","state":"","postal_code":"","country":""} # DocumentRecipientEditRequest | 

    try:
        # Update Document Recipient
        api_instance.edit_document_recipient(id, recipient_id, document_recipient_edit_request)
    except Exception as e:
        print("Exception when calling DocumentRecipientsApi->edit_document_recipient: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Document UUID. | 
 **recipient_id** | **str**| Recipient UUID. | 
 **document_recipient_edit_request** | [**DocumentRecipientEditRequest**](DocumentRecipientEditRequest.md)|  | 

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

# **reassign_document_recipient**
> DocumentRecipientResponse reassign_document_recipient(id, recipient_id, document_recipient_create_request)

Change Signer (Reassign Document Recipient)

Reassign fields to another signer.

> 🚧 Before you start
> 
> To change a signer in a document, please ensure that:
> 
> - You have the 'Can Manage Recipients' permission.
> - New signer is already created in your contacts. If not, add them using the [Create Contact](https://developers.pandadoc.com/reference/create-contact) endpoint.

You can reassign fields to another signer before the original signer has signed the document. You can choose any person except those recipients who have already signed the document.

The endpoint path includes the `recipient_id` of the original signer and the request body must include the following two parameters:

- `kind`: Set this parameter to `contact` to specify an individual contact.
- `id`: Input the ID of the contact you want to use as a replacement for the original signer.

To retrieve the contact's ID, use the [List Contacts](https://developers.pandadoc.com/reference/list-contacts) endpoint to access a list of all contacts, and then locate the desired contact by searching using the name or email address within the returned list.

Once you execute the call to change the signer, the original signer will be entirely removed from the document. If you wish to retain the original signer as a CC recipient, you can re-add them using the [Add CC Recipient](https://developers.pandadoc.com/reference/add-new-recipient-cc) endpoint.

> 🚧 Pre-filled fields
> 
> If you change the signer in a document that has already been sent, the signer's pre-filled fields will be completely reset. In the 'Draft' (`document.draft`) status, pre-filled fields will remain.


### Example

* Api Key Authentication (apiKey):
* OAuth Authentication (oauth2):

```python
import pandadoc_client
from pandadoc_client.models.document_recipient_create_request import DocumentRecipientCreateRequest
from pandadoc_client.models.document_recipient_response import DocumentRecipientResponse
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
    api_instance = pandadoc_client.DocumentRecipientsApi(api_client)
    id = 'BhVzRcxH9Z2LgfPPGXFUBa' # str | Document UUID
    recipient_id = 'tf5dGS3Tmu3cj228ao6fnc' # str | Recipient UUID
    document_recipient_create_request = {"kind":"contact","id":"pGkLnJUAx99JpXJy5DVD30"} # DocumentRecipientCreateRequest | 

    try:
        # Change Signer (Reassign Document Recipient)
        api_response = api_instance.reassign_document_recipient(id, recipient_id, document_recipient_create_request)
        print("The response of DocumentRecipientsApi->reassign_document_recipient:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentRecipientsApi->reassign_document_recipient: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Document UUID | 
 **recipient_id** | **str**| Recipient UUID | 
 **document_recipient_create_request** | [**DocumentRecipientCreateRequest**](DocumentRecipientCreateRequest.md)|  | 

### Return type

[**DocumentRecipientResponse**](DocumentRecipientResponse.md)

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
**403** | Permission error |  -  |
**404** | Not found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

