# pandadoc_client.DocumentsApi

All URIs are relative to *https://api.pandadoc.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**change_document_status**](DocumentsApi.md#change_document_status) | **PATCH** /public/v1/documents/{id}/status | Document status change
[**create_document**](DocumentsApi.md#create_document) | **POST** /public/v1/documents | Create document
[**create_document_link**](DocumentsApi.md#create_document_link) | **POST** /public/v1/documents/{id}/session | Create a Document Link
[**create_linked_object**](DocumentsApi.md#create_linked_object) | **POST** /public/v1/documents/{id}/linked-objects | Create Linked Object
[**delete_document**](DocumentsApi.md#delete_document) | **DELETE** /public/v1/documents/{id} | Delete document by id
[**delete_linked_object**](DocumentsApi.md#delete_linked_object) | **DELETE** /public/v1/documents/{id}/linked-objects/{linked_object_id} | Delete Linked Object
[**details_document**](DocumentsApi.md#details_document) | **GET** /public/v1/documents/{id}/details | Document details
[**download_document**](DocumentsApi.md#download_document) | **GET** /public/v1/documents/{id}/download | Document download
[**download_protected_document**](DocumentsApi.md#download_protected_document) | **GET** /public/v1/documents/{id}/download-protected | Download document protected
[**list_documents**](DocumentsApi.md#list_documents) | **GET** /public/v1/documents | List documents
[**list_linked_objects**](DocumentsApi.md#list_linked_objects) | **GET** /public/v1/documents/{id}/linked-objects | List Linked Objects
[**send_document**](DocumentsApi.md#send_document) | **POST** /public/v1/documents/{id}/send | Send Document
[**status_document**](DocumentsApi.md#status_document) | **GET** /public/v1/documents/{id} | Document status
[**transfer_all_documents_ownership**](DocumentsApi.md#transfer_all_documents_ownership) | **PATCH** /public/v1/documents/ownership | Transfer all documents ownership
[**transfer_document_ownership**](DocumentsApi.md#transfer_document_ownership) | **PATCH** /public/v1/documents/{id}/ownership | Update document ownership


# **change_document_status**
> change_document_status(id, document_status_change_request)

Document status change

### Example

* Api Key Authentication (apiKey):
* OAuth Authentication (oauth2):

```python
import pandadoc_client
from pandadoc_client.api import documents_api
from pandadoc_client.model.document_status_change_request import DocumentStatusChangeRequest
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
    api_instance = documents_api.DocumentsApi(api_client)
    id = "BhVzRcxH9Z2LgfPPGXFUBa"  # str | Specify document ID.
    document_status_change_request = DocumentStatusChangeRequest(
        status=DocumentStatusEnum(12),
        note="A private note",
        notify_recipients=True,
    )  # DocumentStatusChangeRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Document status change
        api_instance.change_document_status(id, document_status_change_request)
    except pandadoc_client.ApiException as e:
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

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No content |  -  |
**401** | Authentication error |  -  |
**403** | Permission error |  -  |
**404** | Not found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **create_document**
> DocumentCreateResponse create_document(document_create_request)

Create document

### Example

* Api Key Authentication (apiKey):
* OAuth Authentication (oauth2):

```python
import pandadoc_client
from pandadoc_client.api import documents_api
from pandadoc_client.model.document_create_response import DocumentCreateResponse
from pandadoc_client.model.document_create_request import DocumentCreateRequest
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
    api_instance = documents_api.DocumentsApi(api_client)
    document_create_request = DocumentCreateRequest(
        name="API Sample Document from PandaDoc Template",
        template_uuid="hryJY9mqYZHjQCYQuSjRQg",
        folder_uuid="QMDSzwabfFzTgjW4kUijqQ",
        recipients=[
            DocumentCreateRequestRecipients(
                email="josh@example.com",
                first_name="Josh",
                last_name="Ron",
                role="user",
                signing_order=1,
            ),
        ],
        tokens=[
            DocumentCreateByTemplateRequestTokens(
                name="Favorite.Pet",
                value="Panda",
            ),
        ],
        fields={},
        metadata={},
        tags=["created_via_api","test_document"],
        images=[
            DocumentCreateRequestImages(
                urls=["https://s3.amazonaws.com/pd-static-content/public-docs/pandadoc-panda-bear.png"],
                name="Image 1",
            ),
        ],
        pricing_tables=[
            PricingTableRequest(
                name="Pricing Table 1",
                data_merge=True,
                options=PricingTableRequestOptions(
                    currency="USD",
                    discount=PricingTableRequestOptionsDiscount(
                        type="absolute",
                        name="Global Discount",
                        value=2.26,
                    ),
                    tax_first=PricingTableRequestOptionsTaxFirst(
                        type="percent",
                        name="Tax First",
                        value=2.26,
                    ),
                    tax_second=PricingTableRequestOptionsTaxSecond(
                        type="percent",
                        name="Tax Second",
                        value=2.26,
                    ),
                ),
                sections=[
                    PricingTableRequestSections(
                        title="Sample Section",
                        default=True,
                        multichoice_enabled=False,
                        rows=[
                            PricingTableRequestRows(
                                options=PricingTableRequestOptions1(
                                    qty_editable=True,
                                    optional_selected=True,
                                    optional=True,
                                ),
                                data=PricingTableRequestData(
                                    name="Toy Panda",
                                    description="Fluffy!",
                                    price=10,
                                    cost=8.5,
                                    qty=3,
                                    sku="toy_panda",
                                    discount=PricingTableRequestDataDiscount(
                                        value=7.5,
                                        type="percent",
                                    ),
                                    tax_first=PricingTableRequestDataDiscount(
                                        value=7.5,
                                        type="percent",
                                    ),
                                    tax_second=PricingTableRequestDataDiscount(
                                        value=7.5,
                                        type="percent",
                                    ),
                                ),
                                custom_fields={},
                            ),
                        ],
                    ),
                ],
            ),
        ],
        content_placeholders=[
            DocumentCreateRequestContentPlaceholders(
                block_id="Content Placeholder 1",
                content_library_items=[
                    DocumentCreateRequestContentLibraryItems(
                        id="hryJY9mqYZHjQCYQuSjRQg",
                        pricing_tables=[
                            PricingTableRequest(
                                name="Pricing Table 1",
                                data_merge=True,
                                options=PricingTableRequestOptions(
                                    currency="USD",
                                    discount=PricingTableRequestOptionsDiscount(
                                        type="absolute",
                                        name="Global Discount",
                                        value=2.26,
                                    ),
                                    tax_first=PricingTableRequestOptionsTaxFirst(
                                        type="percent",
                                        name="Tax First",
                                        value=2.26,
                                    ),
                                    tax_second=PricingTableRequestOptionsTaxSecond(
                                        type="percent",
                                        name="Tax Second",
                                        value=2.26,
                                    ),
                                ),
                                sections=[
                                    PricingTableRequestSections(
                                        title="Sample Section",
                                        default=True,
                                        multichoice_enabled=False,
                                        rows=[
                                            PricingTableRequestRows(
                                                options=PricingTableRequestOptions1(
                                                    qty_editable=True,
                                                    optional_selected=True,
                                                    optional=True,
                                                ),
                                                data=PricingTableRequestData(
                                                    name="Toy Panda",
                                                    description="Fluffy!",
                                                    price=10,
                                                    cost=8.5,
                                                    qty=3,
                                                    sku="toy_panda",
                                                    discount=PricingTableRequestDataDiscount(
                                                        value=7.5,
                                                        type="percent",
                                                    ),
                                                    tax_first=PricingTableRequestDataDiscount(
                                                        value=7.5,
                                                        type="percent",
                                                    ),
                                                    tax_second=PricingTableRequestDataDiscount(
                                                        value=7.5,
                                                        type="percent",
                                                    ),
                                                ),
                                                custom_fields={},
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                        ],
                        fields={},
                        recipients=[
                            DocumentCreateByTemplateRequestRecipients(
                                email="josh@example.com",
                                first_name="Josh",
                                last_name="Ron",
                                role="user",
                                signing_order=1,
                            ),
                        ],
                    ),
                ],
            ),
        ],
        url="https://s3.amazonaws.com/pd-static-content/public-docs/pandadoc-panda-bear.png",
        parse_form_fields=True,
    )  # DocumentCreateRequest | Use a PandaDoc template or an existing PDF to create a document. See the creation request examples [by template](#/schemas/DocumentCreateByTemplateRequest) and [by pdf](#/schemas/DocumentCreateByPdfRequest) 
    editor_ver = "ev2"  # str | Set this parameter as `ev1` if you want to create a document from PDF with Classic Editor when both editors are enabled for the workspace. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create document
        api_response = api_instance.create_document(document_create_request)
        pprint(api_response)
    except pandadoc_client.ApiException as e:
        print("Exception when calling DocumentsApi->create_document: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create document
        api_response = api_instance.create_document(
            document_create_request,
            editor_ver=editor_ver,
        )
        pprint(api_response)
    except pandadoc_client.ApiException as e:
        print("Exception when calling DocumentsApi->create_document: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_create_request** | [**DocumentCreateRequest**](DocumentCreateRequest.md)| Use a PandaDoc template or an existing PDF to create a document. See the creation request examples [by template](#/schemas/DocumentCreateByTemplateRequest) and [by pdf](#/schemas/DocumentCreateByPdfRequest)  |
 **editor_ver** | **str**| Set this parameter as &#x60;ev1&#x60; if you want to create a document from PDF with Classic Editor when both editors are enabled for the workspace. | [optional]

### Return type

[**DocumentCreateResponse**](DocumentCreateResponse.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Authentication error |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **create_document_link**
> DocumentCreateLinkResponse create_document_link(id, document_create_link_request)

Create a Document Link

### Example

* Api Key Authentication (apiKey):
* OAuth Authentication (oauth2):

```python
import pandadoc_client
from pandadoc_client.api import documents_api
from pandadoc_client.model.document_create_link_response import DocumentCreateLinkResponse
from pandadoc_client.model.document_create_link_request import DocumentCreateLinkRequest
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
    api_instance = documents_api.DocumentsApi(api_client)
    id = "ZPeAfcpzr9aiVs5vqUf6jg"  # str | Document ID
    document_create_link_request = DocumentCreateLinkRequest(
        recipient="josh@example.com",
        lifetime=900,
    )  # DocumentCreateLinkRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Create a Document Link
        api_response = api_instance.create_document_link(id, document_create_link_request)
        pprint(api_response)
    except pandadoc_client.ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **create_linked_object**
> LinkedObjectCreateResponse create_linked_object(id, linked_object_create_request)

Create Linked Object

### Example

* Api Key Authentication (apiKey):
* OAuth Authentication (oauth2):

```python
import pandadoc_client
from pandadoc_client.api import documents_api
from pandadoc_client.model.linked_object_create_response import LinkedObjectCreateResponse
from pandadoc_client.model.linked_object_create_request import LinkedObjectCreateRequest
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
    api_instance = documents_api.DocumentsApi(api_client)
    id = "ZPeAfcpzr9aiVs5vqUf6jg"  # str | Specify document ID.
    linked_object_create_request = LinkedObjectCreateRequest(
        provider="pipedrive",
        entity_type="deal",
        entity_id="9372",
    )  # LinkedObjectCreateRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Create Linked Object
        api_response = api_instance.create_linked_object(id, linked_object_create_request)
        pprint(api_response)
    except pandadoc_client.ApiException as e:
        print("Exception when calling DocumentsApi->create_linked_object: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Specify document ID. |
 **linked_object_create_request** | [**LinkedObjectCreateRequest**](LinkedObjectCreateRequest.md)|  |

### Return type

[**LinkedObjectCreateResponse**](LinkedObjectCreateResponse.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **delete_document**
> delete_document(id)

Delete document by id

### Example

* Api Key Authentication (apiKey):
* OAuth Authentication (oauth2):

```python
import pandadoc_client
from pandadoc_client.api import documents_api
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
    api_instance = documents_api.DocumentsApi(api_client)
    id = "BhVzRcxH9Z2LgfPPGXFUBa"  # str | Document ID

    # example passing only required values which don't have defaults set
    try:
        # Delete document by id
        api_instance.delete_document(id)
    except pandadoc_client.ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **delete_linked_object**
> delete_linked_object(id, linked_object_id)

Delete Linked Object

### Example

* Api Key Authentication (apiKey):
* OAuth Authentication (oauth2):

```python
import pandadoc_client
from pandadoc_client.api import documents_api
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
    api_instance = documents_api.DocumentsApi(api_client)
    id = "ZPeAfcpzr9aiVs5vqUf6jg"  # str | Specify document ID.
    linked_object_id = "deb0d530-d759-4189-a422-8d2265e01b2e"  # str | Specify linked object ID.

    # example passing only required values which don't have defaults set
    try:
        # Delete Linked Object
        api_instance.delete_linked_object(id, linked_object_id)
    except pandadoc_client.ApiException as e:
        print("Exception when calling DocumentsApi->delete_linked_object: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Specify document ID. |
 **linked_object_id** | **str**| Specify linked object ID. |

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **details_document**
> DocumentDetailsResponse details_document(id)

Document details

### Example

* Api Key Authentication (apiKey):
* OAuth Authentication (oauth2):

```python
import pandadoc_client
from pandadoc_client.api import documents_api
from pandadoc_client.model.document_details_response import DocumentDetailsResponse
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
    api_instance = documents_api.DocumentsApi(api_client)
    id = "BhVzRcxH9Z2LgfPPGXFUBa"  # str | Document ID

    # example passing only required values which don't have defaults set
    try:
        # Document details
        api_response = api_instance.details_document(id)
        pprint(api_response)
    except pandadoc_client.ApiException as e:
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
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **download_document**
> file_type download_document(id)

Document download

### Example

* Api Key Authentication (apiKey):
* OAuth Authentication (oauth2):

```python
import pandadoc_client
from pandadoc_client.api import documents_api
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
    api_instance = documents_api.DocumentsApi(api_client)
    id = "BhVzRcxH9Z2LgfPPGXFUBa"  # str | Specify document ID.
    watermark_color = "#FF5733"  # str | HEX code (for example `#FF5733`). (optional)
    watermark_font_size = 12  # int | Font size of the watermark. (optional)
    watermark_opacity = 0.5  # float | In range 0.0-1.0 (optional)
    watermark_text = "John Doe inc."  # str | Specify watermark text. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Document download
        api_response = api_instance.download_document(id)
        pprint(api_response)
    except pandadoc_client.ApiException as e:
        print("Exception when calling DocumentsApi->download_document: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Document download
        api_response = api_instance.download_document(
            id,
            watermark_color=watermark_color,
            watermark_font_size=watermark_font_size,
            watermark_opacity=watermark_opacity,
            watermark_text=watermark_text,
        )
        pprint(api_response)
    except pandadoc_client.ApiException as e:
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

### Return type

**file_type**

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
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **download_protected_document**
> file_type download_protected_document(id)

Download document protected

Download a signed PDF of a completed document

### Example

* Api Key Authentication (apiKey):
* OAuth Authentication (oauth2):

```python
import pandadoc_client
from pandadoc_client.api import documents_api
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
    api_instance = documents_api.DocumentsApi(api_client)
    id = "Mebvyy3NGsGBnY2rPLkH84"  # str | Specify document ID.

    # example passing only required values which don't have defaults set
    try:
        # Download document protected
        api_response = api_instance.download_protected_document(id)
        pprint(api_response)
    except pandadoc_client.ApiException as e:
        print("Exception when calling DocumentsApi->download_protected_document: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Specify document ID. |

### Return type

**file_type**

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
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **list_documents**
> DocumentListResponse list_documents()

List documents

### Example

* Api Key Authentication (apiKey):
* OAuth Authentication (oauth2):

```python
import pandadoc_client
from pandadoc_client.api import documents_api
from pandadoc_client.model.document_status_enum import DocumentStatusEnum
from pandadoc_client.model.document_ordering_fields_enum import DocumentOrderingFieldsEnum
from pandadoc_client.model.document_list_response import DocumentListResponse
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
    api_instance = documents_api.DocumentsApi(api_client)
    completed_from = "2021-10-27T15:22:23.132757Z"  # str | Return results where the `date_completed` field (ISO 8601) is greater than or equal to this value. (optional)
    completed_to = "2021-10-27T15:22:23.132757Z"  # str | Return results where the `date_completed` field (ISO 8601) is less than or equal to this value. (optional)
    contact_id = "9FeAY2NB3C9qDdtQRb4tTL"  # str | Returns results where 'contact_id' is present in document as recipient or approver (optional)
    count = 50  # int | Specify how many document results to return. Default is 50 documents, maximum is 100 documents. (optional)
    created_from = "2021-10-27T15:22:23.132757Z"  # str | Return results where the `date_created` field (ISO 8601) is greater than or equal to this value. (optional)
    created_to = "2021-10-27T15:22:23.132757Z"  # str | Return results where the `date_created` field (ISO 8601) is less than this value. (optional)
    deleted = True  # bool | Returns only the deleted documents. (optional)
    id = "BhVzRcxH9Z2LgfPPGXFUBa"  # str |  (optional)
    folder_uuid = "BhVzRcxH9Z2LgfPPGXFUBa"  # str | The UUID of the folder where the documents are stored. (optional)
    form_id = "BhVzRcxH9Z2LgfPPGXFUBa"  # str | Specify the form used for documents creation. This parameter can't be used with template_id. (optional)
    membership_id = "BhVzRcxH9Z2LgfPPGXFUBa"  # str | Returns results where 'membership_id' is present in document as owner (should be member uuid) (optional)
    metadata = "metadata_example"  # str | Specify metadata to filter by in the format of `metadata_{metadata-key}={metadata-value}` such as `metadata_opportunity_id=2181432`. The `metadata_` prefix is always required. (optional)
    modified_from = "2021-10-27T15:22:23.132757Z"  # str | Return results where the `date_modified` field (iso-8601) is greater than or equal to this value. (optional)
    modified_to = "2021-10-27T15:22:23.132757Z"  # str | Return results where the `date_modified` field (iso-8601) is less than this value. (optional)
    order_by = DocumentOrderingFieldsEnum("name")  # DocumentOrderingFieldsEnum | Specify the order of documents to return. Use `value` (for example, `date_created`) for ASC and `-value` (for example, `-date_created`) for DESC. (optional)
    page = 1  # int | Specify which page of the dataset to return. (optional)
    q = "Sample Document"  # str | Search query. Filter by document reference number (this token is stored on the template level) or name. (optional)
    status = DocumentStatusEnum(12)  # DocumentStatusEnum | Specify the status of documents to return.   * 0: document.draft   * 1: document.sent   * 2: document.completed   * 3: document.uploaded   * 4: document.error   * 5: document.viewed   * 6: document.waiting_approval   * 7: document.approved   * 8: document.rejected   * 9: document.waiting_pay   * 10: document.paid   * 11: document.voided   * 12: document.declined  (optional)
    status__ne = DocumentStatusEnum(12)  # DocumentStatusEnum | Specify the status of documents to return (exclude).   * 0: document.draft   * 1: document.sent   * 2: document.completed   * 3: document.uploaded   * 4: document.error   * 5: document.viewed   * 6: document.waiting_approval   * 7: document.approved   * 8: document.rejected   * 9: document.waiting_pay   * 10: document.paid   * 11: document.voided   * 12: document.declined  (optional)
    tag = "tag_1"  # str | Search tag. Filter by document tag. (optional)
    template_id = "BhVzRcxH9Z2LgfPPGXFUBa"  # str | Specify the template used for documents creation. Parameter can't be used with form_id. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List documents
        api_response = api_instance.list_documents(
            completed_from=completed_from,
            completed_to=completed_to,
            contact_id=contact_id,
            count=count,
            created_from=created_from,
            created_to=created_to,
            deleted=deleted,
            id=id,
            folder_uuid=folder_uuid,
            form_id=form_id,
            membership_id=membership_id,
            metadata=metadata,
            modified_from=modified_from,
            modified_to=modified_to,
            order_by=order_by,
            page=page,
            q=q,
            status=status,
            status__ne=status__ne,
            tag=tag,
            template_id=template_id,
        )
        pprint(api_response)
    except pandadoc_client.ApiException as e:
        print("Exception when calling DocumentsApi->list_documents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **completed_from** | **str**| Return results where the &#x60;date_completed&#x60; field (ISO 8601) is greater than or equal to this value. | [optional]
 **completed_to** | **str**| Return results where the &#x60;date_completed&#x60; field (ISO 8601) is less than or equal to this value. | [optional]
 **contact_id** | **str**| Returns results where &#39;contact_id&#39; is present in document as recipient or approver | [optional]
 **count** | **int**| Specify how many document results to return. Default is 50 documents, maximum is 100 documents. | [optional]
 **created_from** | **str**| Return results where the &#x60;date_created&#x60; field (ISO 8601) is greater than or equal to this value. | [optional]
 **created_to** | **str**| Return results where the &#x60;date_created&#x60; field (ISO 8601) is less than this value. | [optional]
 **deleted** | **bool**| Returns only the deleted documents. | [optional]
 **id** | **str**|  | [optional]
 **folder_uuid** | **str**| The UUID of the folder where the documents are stored. | [optional]
 **form_id** | **str**| Specify the form used for documents creation. This parameter can&#39;t be used with template_id. | [optional]
 **membership_id** | **str**| Returns results where &#39;membership_id&#39; is present in document as owner (should be member uuid) | [optional]
 **metadata** | **str**| Specify metadata to filter by in the format of &#x60;metadata_{metadata-key}&#x3D;{metadata-value}&#x60; such as &#x60;metadata_opportunity_id&#x3D;2181432&#x60;. The &#x60;metadata_&#x60; prefix is always required. | [optional]
 **modified_from** | **str**| Return results where the &#x60;date_modified&#x60; field (iso-8601) is greater than or equal to this value. | [optional]
 **modified_to** | **str**| Return results where the &#x60;date_modified&#x60; field (iso-8601) is less than this value. | [optional]
 **order_by** | **DocumentOrderingFieldsEnum**| Specify the order of documents to return. Use &#x60;value&#x60; (for example, &#x60;date_created&#x60;) for ASC and &#x60;-value&#x60; (for example, &#x60;-date_created&#x60;) for DESC. | [optional]
 **page** | **int**| Specify which page of the dataset to return. | [optional]
 **q** | **str**| Search query. Filter by document reference number (this token is stored on the template level) or name. | [optional]
 **status** | **DocumentStatusEnum**| Specify the status of documents to return.   * 0: document.draft   * 1: document.sent   * 2: document.completed   * 3: document.uploaded   * 4: document.error   * 5: document.viewed   * 6: document.waiting_approval   * 7: document.approved   * 8: document.rejected   * 9: document.waiting_pay   * 10: document.paid   * 11: document.voided   * 12: document.declined  | [optional]
 **status__ne** | **DocumentStatusEnum**| Specify the status of documents to return (exclude).   * 0: document.draft   * 1: document.sent   * 2: document.completed   * 3: document.uploaded   * 4: document.error   * 5: document.viewed   * 6: document.waiting_approval   * 7: document.approved   * 8: document.rejected   * 9: document.waiting_pay   * 10: document.paid   * 11: document.voided   * 12: document.declined  | [optional]
 **tag** | **str**| Search tag. Filter by document tag. | [optional]
 **template_id** | **str**| Specify the template used for documents creation. Parameter can&#39;t be used with form_id. | [optional]

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
**401** | Bad Request |  -  |
**403** | Authentication error |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **list_linked_objects**
> LinkedObjectListResponse list_linked_objects(id)

List Linked Objects

### Example

* Api Key Authentication (apiKey):
* OAuth Authentication (oauth2):

```python
import pandadoc_client
from pandadoc_client.api import documents_api
from pandadoc_client.model.linked_object_list_response import LinkedObjectListResponse
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
    api_instance = documents_api.DocumentsApi(api_client)
    id = "ZPeAfcpzr9aiVs5vqUf6jg"  # str | Specify document ID.

    # example passing only required values which don't have defaults set
    try:
        # List Linked Objects
        api_response = api_instance.list_linked_objects(id)
        pprint(api_response)
    except pandadoc_client.ApiException as e:
        print("Exception when calling DocumentsApi->list_linked_objects: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Specify document ID. |

### Return type

[**LinkedObjectListResponse**](LinkedObjectListResponse.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success response |  -  |
**401** | Authentication error |  -  |
**403** | Permission error |  -  |
**404** | Not found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **send_document**
> DocumentSendResponse send_document(id, document_send_request)

Send Document

### Example

* Api Key Authentication (apiKey):
* OAuth Authentication (oauth2):

```python
import pandadoc_client
from pandadoc_client.api import documents_api
from pandadoc_client.model.document_send_response import DocumentSendResponse
from pandadoc_client.model.document_send_request import DocumentSendRequest
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
    api_instance = documents_api.DocumentsApi(api_client)
    id = "ZPeAfcpzr9aiVs5vqUf6jg"  # str | Document ID
    document_send_request = DocumentSendRequest(
        message="Hello! This document was sent from the PandaDoc API",
        subject="Please check this test API document from PandaDoc",
        silent=True,
    )  # DocumentSendRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Send Document
        api_response = api_instance.send_document(id, document_send_request)
        pprint(api_response)
    except pandadoc_client.ApiException as e:
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
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **status_document**
> DocumentStatusResponse status_document(id)

Document status

### Example

* Api Key Authentication (apiKey):
* OAuth Authentication (oauth2):

```python
import pandadoc_client
from pandadoc_client.api import documents_api
from pandadoc_client.model.document_status_response import DocumentStatusResponse
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
    api_instance = documents_api.DocumentsApi(api_client)
    id = "BhVzRcxH9Z2LgfPPGXFUBa"  # str | Specify document ID.

    # example passing only required values which don't have defaults set
    try:
        # Document status
        api_response = api_instance.status_document(id)
        pprint(api_response)
    except pandadoc_client.ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **transfer_all_documents_ownership**
> transfer_all_documents_ownership(document_transfer_all_ownership_request)

Transfer all documents ownership

### Example

* Api Key Authentication (apiKey):
* OAuth Authentication (oauth2):

```python
import pandadoc_client
from pandadoc_client.api import documents_api
from pandadoc_client.model.document_transfer_all_ownership_request import DocumentTransferAllOwnershipRequest
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
    api_instance = documents_api.DocumentsApi(api_client)
    document_transfer_all_ownership_request = DocumentTransferAllOwnershipRequest(
        from_membership_id="Dqsxp4jNnFcS63tJEgLJGN",
        to_membership_id="radQBiBkU7MBk59NSgaGfd",
    )  # DocumentTransferAllOwnershipRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Transfer all documents ownership
        api_instance.transfer_all_documents_ownership(document_transfer_all_ownership_request)
    except pandadoc_client.ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **transfer_document_ownership**
> transfer_document_ownership(id, document_transfer_ownership_request)

Update document ownership

### Example

* Api Key Authentication (apiKey):
* OAuth Authentication (oauth2):

```python
import pandadoc_client
from pandadoc_client.api import documents_api
from pandadoc_client.model.document_transfer_ownership_request import DocumentTransferOwnershipRequest
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
    api_instance = documents_api.DocumentsApi(api_client)
    id = "BhVzRcxH9Z2LgfPPGXFUBa"  # str | Specify document ID.
    document_transfer_ownership_request = DocumentTransferOwnershipRequest(
        membership_id="radQBiBkU7MBk59NSgaGfd",
    )  # DocumentTransferOwnershipRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Update document ownership
        api_instance.transfer_document_ownership(id, document_transfer_ownership_request)
    except pandadoc_client.ApiException as e:
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
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

