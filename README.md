# The Official PandaDoc Python client SDK
PandaDoc SDK spans a broad range of functionality to help you build incredible documents automation experiences inside your product.

## Docs
- [Official public API documentation](https://developers.pandadoc.com/reference/about)

## Requirements
python >= 3.6

## Installation
#### pip install
If the python package is hosted on a repository, you can install directly using:
```sh
pip install git+https://github.com/PandaDoc/pandadoc-api-python-client.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/PandaDoc/pandadoc-api-python-client.git`)

Then import the package:
```python
import pandadoc_client
```

## Getting Started

```python
from pprint import pprint

import openapi_client
from openapi_client.api import templates_api

# Configure API key authorization: apiKey
api_key = "YOUR_API_KEY"

# Defining the host is optional and defaults to https://api.pandadoc.com
# See configuration.py for a list of all supported configuration parameters.
cfg = openapi_client.Configuration(
    host = "https://api.pandadoc.com",
    api_key={"apiKey": f"API-Key {api_key}"},
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(cfg) as api_client:
    # Create an instance of the API class
    api_instance = templates_api.TemplatesApi(api_client)

    try:
        resp = api_instance.list_templates(tag="doe-inc-proposals")
        pprint(resp)
    except openapi_client.ApiException as e:
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
 - **read+write**: default

## Examples

- [Create and send document from a template](examples/create_from_template_and_send.py)
- [Create and send document from the pdf url](examples/create_from_pdf_by_url_and_send.py)

## Docs
### Official PandaDoc public API docs
https://developers.pandadoc.com/reference/about

### Documentation for API Endpoints

All URIs are relative to *https://api.pandadoc.com*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*APILogsApi* | [**details_api_log**](docs/APILogsApi.md#details_api_log) | **GET** /public/v1/logs/{id} | Details API Log
*APILogsApi* | [**list_api_logs**](docs/APILogsApi.md#list_api_logs) | **GET** /public/v1/logs | List API Log
*ContentLibraryItemsApi* | [**details_content_library_item**](docs/ContentLibraryItemsApi.md#details_content_library_item) | **GET** /public/v1/content-library-items/{id}/details | Details Content Library Item
*ContentLibraryItemsApi* | [**list_content_library_items**](docs/ContentLibraryItemsApi.md#list_content_library_items) | **GET** /public/v1/content-library-items | List Content Library Item
*DocumentsApi* | [**delete_document**](docs/DocumentsApi.md#delete_document) | **DELETE** /public/v1/documents/{id} | Delete document by id
*DocumentsApi* | [**document_create**](docs/DocumentsApi.md#document_create) | **POST** /public/v1/documents | Create document
*DocumentsApi* | [**document_create_link**](docs/DocumentsApi.md#document_create_link) | **POST** /public/v1/documents/{id}/session | Create a Document Link
*DocumentsApi* | [**document_details**](docs/DocumentsApi.md#document_details) | **GET** /public/v1/documents/{id}/details | Document details
*DocumentsApi* | [**document_list**](docs/DocumentsApi.md#document_list) | **GET** /public/v1/documents | List documents
*DocumentsApi* | [**document_status**](docs/DocumentsApi.md#document_status) | **GET** /public/v1/documents/{id} | Document status
*DocumentsApi* | [**download_document**](docs/DocumentsApi.md#download_document) | **GET** /public/v1/documents/{id}/download | Document download
*DocumentsApi* | [**download_protected_document**](docs/DocumentsApi.md#download_protected_document) | **GET** /public/v1/documents/{id}/download-protected | Download document protected
*DocumentsApi* | [**linked_object_delete**](docs/DocumentsApi.md#linked_object_delete) | **DELETE** /public/v1/documents/{id}/linked-objects/{linked_object_id} | Delete Linked Object
*DocumentsApi* | [**linked_object_list**](docs/DocumentsApi.md#linked_object_list) | **GET** /public/v1/documents/{id}/linked-objects | List Linked Objects
*DocumentsApi* | [**linked_objects_create**](docs/DocumentsApi.md#linked_objects_create) | **POST** /public/v1/documents/{id}/linked-objects | Create Linked Object
*DocumentsApi* | [**send_document**](docs/DocumentsApi.md#send_document) | **POST** /public/v1/documents/{id}/send | Send Document
*FoldersAPIApi* | [**create_document_folder**](docs/FoldersAPIApi.md#create_document_folder) | **POST** /public/v1/documents/folders | Create Documents Folder
*FoldersAPIApi* | [**create_template_folder**](docs/FoldersAPIApi.md#create_template_folder) | **POST** /public/v1/templates/folders | Create Templates Folder
*FoldersAPIApi* | [**list_document_folders**](docs/FoldersAPIApi.md#list_document_folders) | **GET** /public/v1/documents/folders | List Documents Folders
*FoldersAPIApi* | [**list_template_folders**](docs/FoldersAPIApi.md#list_template_folders) | **GET** /public/v1/templates/folders | List Templates Folders
*FoldersAPIApi* | [**rename_document_folder**](docs/FoldersAPIApi.md#rename_document_folder) | **PUT** /public/v1/documents/folders/{id} | Rename Documents Folder
*FoldersAPIApi* | [**rename_template_folder**](docs/FoldersAPIApi.md#rename_template_folder) | **PUT** /public/v1/templates/folders/{id} | Rename Templates Folder
*FormsApi* | [**list_form**](docs/FormsApi.md#list_form) | **GET** /public/v1/forms | Forms
*OAuth20AuthenticationApi* | [**access_token**](docs/OAuth20AuthenticationApi.md#access_token) | **POST** /oauth2/access_token | Create/Refresh Access Token
*TemplatesApi* | [**delete_template**](docs/TemplatesApi.md#delete_template) | **DELETE** /public/v1/templates/{id} | Delete Template
*TemplatesApi* | [**details_temaplate**](docs/TemplatesApi.md#details_temaplate) | **GET** /public/v1/templates/{id}/details | Details Template
*TemplatesApi* | [**list_templates**](docs/TemplatesApi.md#list_templates) | **GET** /public/v1/templates | List Templates

## License
SDK is licensed under the following [License](LICENSE).