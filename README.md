# The Official PandaDoc Python client SDK
PandaDoc SDK spans a broad range of functionality to help you build incredible documents automation experiences inside your product.

## Docs
- [Official public API documentation](https://developers.pandadoc.com/reference/about)

## Requirements
Python >= 3.6

## Installation
#### pip install
If the python package is hosted on a repository, you can install directly using:
```sh
pip install pandadoc-python-client
```
(you may need to run `pip` with root permission: `sudo pip install pandadoc-python-client`)

Then import the package:
```python
import pandadoc_client
```

## Getting Started

```python
from pprint import pprint

import pandadoc_client
from pandadoc_client.api import templates_api

# Configure API key authorization: apiKey
api_key = "YOUR_API_KEY"

# Defining the host is optional and defaults to https://api.pandadoc.com
# See configuration.py for a list of all supported configuration parameters.
cfg = pandadoc_client.Configuration(
    host="https://api.pandadoc.com",
    api_key={"apiKey": f"API-Key {api_key}"},
)

# Enter a context with an instance of the API client
with pandadoc_client.ApiClient(cfg) as api_client:
    # Create an instance of the API class
    api_instance = templates_api.TemplatesApi(api_client)

    try:
        resp = api_instance.list_templates(tag=["doe-inc-proposals"])
        pprint(resp)
    except pandadoc_client.ApiException as e:
        pprint("Exception when calling TemplatesApi->list_templates: %s\n" % e)
```

## Authorization
### apiKey
- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header
### oauth2
- **Type**: OAuth
- **Flow**: accessCode
- **Authorization URL**: https://app.pandadoc.com/oauth2/authorize
- **Scopes**: 
 - **read+write**: Use `read+write` to create, send, delete, and download documents, and `read` to view templates and document details.

## Examples

- [Create and send document from a template](https://github.com/PandaDoc/pandadoc-api-python-client/blob/main/examples/create_from_template_and_send.py)
- [Create and send document from the pdf url](https://github.com/PandaDoc/pandadoc-api-python-client/blob/main/examples/create_from_pdf_by_url_and_send.py)

## Docs
### Official PandaDoc public API docs
https://developers.pandadoc.com/reference/about

### Documentation for API Endpoints

All URIs are relative to *https://api.pandadoc.com*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*APILogsApi* | [**details_log**](docs/APILogsApi.md#details_log) | **GET** /public/v1/logs/{id} | Details API Log
*APILogsApi* | [**list_logs**](docs/APILogsApi.md#list_logs) | **GET** /public/v1/logs | List API Log
*ContactsApi* | [**create_contact**](docs/ContactsApi.md#create_contact) | **POST** /public/v1/contacts | Create contact
*ContactsApi* | [**delete_contact**](docs/ContactsApi.md#delete_contact) | **DELETE** /public/v1/contacts/{id} | Delete contact by id
*ContactsApi* | [**details_contact**](docs/ContactsApi.md#details_contact) | **GET** /public/v1/contacts/{id} | Get contact details by id
*ContactsApi* | [**list_contacts**](docs/ContactsApi.md#list_contacts) | **GET** /public/v1/contacts | List contacts
*ContactsApi* | [**update_contact**](docs/ContactsApi.md#update_contact) | **PATCH** /public/v1/contacts/{id} | Update contact by id
*ContentLibraryItemsApi* | [**details_content_library_item**](docs/ContentLibraryItemsApi.md#details_content_library_item) | **GET** /public/v1/content-library-items/{id}/details | Details Content Library Item
*ContentLibraryItemsApi* | [**list_content_library_items**](docs/ContentLibraryItemsApi.md#list_content_library_items) | **GET** /public/v1/content-library-items | List Content Library Item
*DocumentAttachmentsApi* | [**create_document_attachment**](docs/DocumentAttachmentsApi.md#create_document_attachment) | **POST** /public/v1/documents/{id}/attachments | Document Attachment Create
*DocumentAttachmentsApi* | [**delete_document_attachment**](docs/DocumentAttachmentsApi.md#delete_document_attachment) | **DELETE** /public/v1/documents/{id}/attachments/{attachment_id} | Document Attachment Delete
*DocumentAttachmentsApi* | [**details_document_attachment**](docs/DocumentAttachmentsApi.md#details_document_attachment) | **GET** /public/v1/documents/{id}/attachments/{attachment_id} | Document Attachment Details
*DocumentAttachmentsApi* | [**download_document_attachment**](docs/DocumentAttachmentsApi.md#download_document_attachment) | **GET** /public/v1/documents/{id}/attachments/{attachment_id}/download | Document Attachment Download
*DocumentAttachmentsApi* | [**list_document_attachments**](docs/DocumentAttachmentsApi.md#list_document_attachments) | **GET** /public/v1/documents/{id}/attachments | Document Attachment List
*DocumentsApi* | [**change_document_status**](docs/DocumentsApi.md#change_document_status) | **PATCH** /public/v1/documents/{id}/status | Document status change
*DocumentsApi* | [**create_document**](docs/DocumentsApi.md#create_document) | **POST** /public/v1/documents | Create document
*DocumentsApi* | [**create_document_link**](docs/DocumentsApi.md#create_document_link) | **POST** /public/v1/documents/{id}/session | Create a Document Link
*DocumentsApi* | [**create_linked_object**](docs/DocumentsApi.md#create_linked_object) | **POST** /public/v1/documents/{id}/linked-objects | Create Linked Object
*DocumentsApi* | [**delete_document**](docs/DocumentsApi.md#delete_document) | **DELETE** /public/v1/documents/{id} | Delete document by id
*DocumentsApi* | [**delete_linked_object**](docs/DocumentsApi.md#delete_linked_object) | **DELETE** /public/v1/documents/{id}/linked-objects/{linked_object_id} | Delete Linked Object
*DocumentsApi* | [**details_document**](docs/DocumentsApi.md#details_document) | **GET** /public/v1/documents/{id}/details | Document details
*DocumentsApi* | [**document_move_to_folder**](docs/DocumentsApi.md#document_move_to_folder) | **POST** /public/v1/documents/{id}/move-to-folder/{folder_id} | Document move to folder
*DocumentsApi* | [**download_document**](docs/DocumentsApi.md#download_document) | **GET** /public/v1/documents/{id}/download | Document download
*DocumentsApi* | [**download_protected_document**](docs/DocumentsApi.md#download_protected_document) | **GET** /public/v1/documents/{id}/download-protected | Download document protected
*DocumentsApi* | [**list_documents**](docs/DocumentsApi.md#list_documents) | **GET** /public/v1/documents | List documents
*DocumentsApi* | [**list_linked_objects**](docs/DocumentsApi.md#list_linked_objects) | **GET** /public/v1/documents/{id}/linked-objects | List Linked Objects
*DocumentsApi* | [**send_document**](docs/DocumentsApi.md#send_document) | **POST** /public/v1/documents/{id}/send | Send Document
*DocumentsApi* | [**status_document**](docs/DocumentsApi.md#status_document) | **GET** /public/v1/documents/{id} | Document status
*DocumentsApi* | [**transfer_all_documents_ownership**](docs/DocumentsApi.md#transfer_all_documents_ownership) | **PATCH** /public/v1/documents/ownership | Transfer all documents ownership
*DocumentsApi* | [**transfer_document_ownership**](docs/DocumentsApi.md#transfer_document_ownership) | **PATCH** /public/v1/documents/{id}/ownership | Update document ownership
*DocumentsApi* | [**update_document**](docs/DocumentsApi.md#update_document) | **PATCH** /public/v1/documents/{id} | Update Document only in the draft status
*FoldersAPIApi* | [**create_document_folder**](docs/FoldersAPIApi.md#create_document_folder) | **POST** /public/v1/documents/folders | Create Documents Folder
*FoldersAPIApi* | [**create_template_folder**](docs/FoldersAPIApi.md#create_template_folder) | **POST** /public/v1/templates/folders | Create Templates Folder
*FoldersAPIApi* | [**list_document_folders**](docs/FoldersAPIApi.md#list_document_folders) | **GET** /public/v1/documents/folders | List Documents Folders
*FoldersAPIApi* | [**list_template_folders**](docs/FoldersAPIApi.md#list_template_folders) | **GET** /public/v1/templates/folders | List Templates Folders
*FoldersAPIApi* | [**rename_document_folder**](docs/FoldersAPIApi.md#rename_document_folder) | **PUT** /public/v1/documents/folders/{id} | Rename Documents Folder
*FoldersAPIApi* | [**rename_template_folder**](docs/FoldersAPIApi.md#rename_template_folder) | **PUT** /public/v1/templates/folders/{id} | Rename Templates Folder
*FormsApi* | [**list_form**](docs/FormsApi.md#list_form) | **GET** /public/v1/forms | Forms
*MembersApi* | [**details_current_member**](docs/MembersApi.md#details_current_member) | **GET** /public/v1/members/current | Current member details
*MembersApi* | [**details_member**](docs/MembersApi.md#details_member) | **GET** /public/v1/members/{id} | Member details
*MembersApi* | [**list_members**](docs/MembersApi.md#list_members) | **GET** /public/v1/members | List members
*OAuth20AuthenticationApi* | [**access_token**](docs/OAuth20AuthenticationApi.md#access_token) | **POST** /oauth2/access_token | Create/Refresh Access Token
*TemplatesApi* | [**delete_template**](docs/TemplatesApi.md#delete_template) | **DELETE** /public/v1/templates/{id} | Delete Template
*TemplatesApi* | [**details_template**](docs/TemplatesApi.md#details_template) | **GET** /public/v1/templates/{id}/details | Details Template
*TemplatesApi* | [**list_templates**](docs/TemplatesApi.md#list_templates) | **GET** /public/v1/templates | List Templates
*WebhookEventsApi* | [**details_webhook_event**](docs/WebhookEventsApi.md#details_webhook_event) | **GET** /public/v1/webhook-events/{id} | Get webhook event by uuid
*WebhookEventsApi* | [**list_webhook_event**](docs/WebhookEventsApi.md#list_webhook_event) | **GET** /public/v1/webhook-events | Get webhook event page
*WebhookSubscriptionsApi* | [**create_webhook_subscription**](docs/WebhookSubscriptionsApi.md#create_webhook_subscription) | **POST** /public/v1/webhook-subscriptions | Create webhook subscription
*WebhookSubscriptionsApi* | [**delete_webhook_subscription**](docs/WebhookSubscriptionsApi.md#delete_webhook_subscription) | **DELETE** /public/v1/webhook-subscriptions/{id} | Delete webhook subscription
*WebhookSubscriptionsApi* | [**details_webhook_subscription**](docs/WebhookSubscriptionsApi.md#details_webhook_subscription) | **GET** /public/v1/webhook-subscriptions/{id} | Get webhook subscription by uuid
*WebhookSubscriptionsApi* | [**list_webhook_subscriptions**](docs/WebhookSubscriptionsApi.md#list_webhook_subscriptions) | **GET** /public/v1/webhook-subscriptions | Get all webhook subscriptions
*WebhookSubscriptionsApi* | [**update_webhook_subscription**](docs/WebhookSubscriptionsApi.md#update_webhook_subscription) | **PATCH** /public/v1/webhook-subscriptions/{id} | Update webhook subscription
*WebhookSubscriptionsApi* | [**update_webhook_subscription_shared_key**](docs/WebhookSubscriptionsApi.md#update_webhook_subscription_shared_key) | **PATCH** /public/v1/webhook-subscriptions/{id}/shared-key | Regenerate webhook subscription shared key


## License
SDK is licensed under the following [License](https://github.com/PandaDoc/pandadoc-api-python-client/blob/main/LICENSE).
