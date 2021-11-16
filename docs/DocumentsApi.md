# pandadoc_client.DocumentsApi

All URIs are relative to *https://api.pandadoc.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_document**](DocumentsApi.md#delete_document) | **DELETE** /public/v1/documents/{id} | Delete document by id
[**document_create**](DocumentsApi.md#document_create) | **POST** /public/v1/documents | Create document
[**document_create_link**](DocumentsApi.md#document_create_link) | **POST** /public/v1/documents/{id}/session | Create a Document Link
[**document_details**](DocumentsApi.md#document_details) | **GET** /public/v1/documents/{id}/details | Document details
[**document_list**](DocumentsApi.md#document_list) | **GET** /public/v1/documents | List documents
[**document_status**](DocumentsApi.md#document_status) | **GET** /public/v1/documents/{id} | Document status
[**download_document**](DocumentsApi.md#download_document) | **GET** /public/v1/documents/{id}/download | Document download
[**download_protected_document**](DocumentsApi.md#download_protected_document) | **GET** /public/v1/documents/{id}/download-protected | Download document protected
[**linked_object_delete**](DocumentsApi.md#linked_object_delete) | **DELETE** /public/v1/documents/{id}/linked-objects/{linked_object_id} | Delete Linked Object
[**linked_object_list**](DocumentsApi.md#linked_object_list) | **GET** /public/v1/documents/{id}/linked-objects | List Linked Objects
[**linked_objects_create**](DocumentsApi.md#linked_objects_create) | **POST** /public/v1/documents/{id}/linked-objects | Create Linked Object
[**send_document**](DocumentsApi.md#send_document) | **POST** /public/v1/documents/{id}/send | Send Document


# **delete_document**
> delete_document(id)

Delete document by id

### Example

* Api Key Authentication (apiKey):
* OAuth Authentication (oauth2):

```python
import time
import pandadoc_client
from pandadoc_client.api import documents_api
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
configuration.api_key['apiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Configure OAuth2 access token for authorization: oauth2
configuration = pandadoc_client.Configuration(
    host = "https://api.pandadoc.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pandadoc_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = documents_api.DocumentsApi(api_client)
    id = "id_example" # str | Document ID

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **document_create**
> DocumentCreateResponse document_create()

Create document

### Example

* Api Key Authentication (apiKey):
* OAuth Authentication (oauth2):

```python
import time
import pandadoc_client
from pandadoc_client.api import documents_api
from pandadoc_client.model.document_create_response import DocumentCreateResponse
from pandadoc_client.model.inline_object import InlineObject
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
configuration.api_key['apiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Configure OAuth2 access token for authorization: oauth2
configuration = pandadoc_client.Configuration(
    host = "https://api.pandadoc.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pandadoc_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = documents_api.DocumentsApi(api_client)
    editor_ver = "ev1" # str | Set this parameter as `ev1` if you want to create a document from PDF with Classic Editor when both editors are enabled for the workspace. (optional)
    inline_object = InlineObject(
        name="API Sample Document from PandaDoc Template",
        template_uuid="hryJY9mqYZHjQCYQuSjRQg",
        folder_uuid="QMDSzwabfFzTgjW4kUijqQ",
        recipients=[
            PublicV1DocumentsRecipients(
                email="josh@example.com",
                first_name="Josh",
                last_name="Ron",
                role="user",
                signing_order=1,
            ),
        ],
        tokens=[
            PublicV1DocumentsTokens(
                name="Favorite.Pet",
                value="Panda",
            ),
        ],
        fields={},
        metadata={},
        tags=["created_via_api","test_document"],
        images=[
            PublicV1DocumentsImages(
                urls=["https://s3.amazonaws.com/pd-static-content/public-docs/pandadoc-panda-bear.png"],
                name="Image 1",
            ),
        ],
        pricing_tables=[
            PricingTableRequest(
                name="Pricing Table",
                options=PricingTableRequestOptions(
                    currency="USD",
                    discount=PricingTableRequestOptionsDiscount(
                        is_global=True,
                        type="absolute",
                        name="Global Discount",
                        value=2.26,
                    ),
                    tax_first=PricingTableRequestOptionsTaxFirst(
                        is_global=True,
                        type="percent",
                        name="Tax First",
                        value=2.26,
                    ),
                    tax_second=PricingTableRequestOptionsTaxSecond(
                        is_global=True,
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
            PublicV1DocumentsContentPlaceholders(
                block_id="hryJY9mqYZHjQCYQuSjRQg",
                content_library_items=[
                    PublicV1DocumentsContentLibraryItems(
                        id="hryJY9mqYZHjQCYQuSjRQg",
                        pricing_tables=[
                            PricingTableRequest(
                                name="Pricing Table",
                                options=PricingTableRequestOptions(
                                    currency="USD",
                                    discount=PricingTableRequestOptionsDiscount(
                                        is_global=True,
                                        type="absolute",
                                        name="Global Discount",
                                        value=2.26,
                                    ),
                                    tax_first=PricingTableRequestOptionsTaxFirst(
                                        is_global=True,
                                        type="percent",
                                        name="Tax First",
                                        value=2.26,
                                    ),
                                    tax_second=PricingTableRequestOptionsTaxSecond(
                                        is_global=True,
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
                            {},
                        ],
                    ),
                ],
            ),
        ],
        url="https://s3.amazonaws.com/pd-static-content/public-docs/pandadoc-panda-bear.png",
        parse_form_fields=True,
    ) # InlineObject |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create document
        api_response = api_instance.document_create(editor_ver=editor_ver, inline_object=inline_object)
        pprint(api_response)
    except pandadoc_client.ApiException as e:
        print("Exception when calling DocumentsApi->document_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **editor_ver** | **str**| Set this parameter as &#x60;ev1&#x60; if you want to create a document from PDF with Classic Editor when both editors are enabled for the workspace. | [optional]
 **inline_object** | [**InlineObject**](InlineObject.md)|  | [optional]

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **document_create_link**
> DocumentCreateLinkResponse document_create_link(id, document_create_link_request)

Create a Document Link

### Example

* Api Key Authentication (apiKey):
* OAuth Authentication (oauth2):

```python
import time
import pandadoc_client
from pandadoc_client.api import documents_api
from pandadoc_client.model.document_create_link_response import DocumentCreateLinkResponse
from pandadoc_client.model.document_create_link_request import DocumentCreateLinkRequest
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
configuration.api_key['apiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Configure OAuth2 access token for authorization: oauth2
configuration = pandadoc_client.Configuration(
    host = "https://api.pandadoc.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pandadoc_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = documents_api.DocumentsApi(api_client)
    id = "id_example" # str | Document ID
    document_create_link_request = DocumentCreateLinkRequest(None) # DocumentCreateLinkRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Create a Document Link
        api_response = api_instance.document_create_link(id, document_create_link_request)
        pprint(api_response)
    except pandadoc_client.ApiException as e:
        print("Exception when calling DocumentsApi->document_create_link: %s\n" % e)
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

# **document_details**
> DocumentDetailsResponse document_details(id)

Document details

### Example

* Api Key Authentication (apiKey):
* OAuth Authentication (oauth2):

```python
import time
import pandadoc_client
from pandadoc_client.api import documents_api
from pandadoc_client.model.document_details_response import DocumentDetailsResponse
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
configuration.api_key['apiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Configure OAuth2 access token for authorization: oauth2
configuration = pandadoc_client.Configuration(
    host = "https://api.pandadoc.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pandadoc_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = documents_api.DocumentsApi(api_client)
    id = "id_example" # str | Document ID

    # example passing only required values which don't have defaults set
    try:
        # Document details
        api_response = api_instance.document_details(id)
        pprint(api_response)
    except pandadoc_client.ApiException as e:
        print("Exception when calling DocumentsApi->document_details: %s\n" % e)
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **document_list**
> DocumentListResponse document_list()

List documents

### Example

* Api Key Authentication (apiKey):
* OAuth Authentication (oauth2):

```python
import time
import pandadoc_client
from pandadoc_client.api import documents_api
from pandadoc_client.model.document_status_enum import DocumentStatusEnum
from pandadoc_client.model.document_ordering_fields_enum import DocumentOrderingFieldsEnum
from pandadoc_client.model.document_list_response import DocumentListResponse
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
configuration.api_key['apiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Configure OAuth2 access token for authorization: oauth2
configuration = pandadoc_client.Configuration(
    host = "https://api.pandadoc.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pandadoc_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = documents_api.DocumentsApi(api_client)
    completed_from = "2021-10-27T15:22:23.132757Z" # str | Return results where the `date_completed` field (ISO 8601) is greater than or equal to this value. (optional)
    completed_to = "2021-10-27T15:22:23.132757Z" # str | Return results where the `date_completed` field (ISO 8601) is less than or equal to this value. (optional)
    count = 50 # int | Specify how many document results to return. Default is 50 documents, maximum is 100 documents. (optional)
    created_from = "2021-10-27T15:22:23.132757Z" # str | Return results where the `date_created` field (ISO 8601) is greater than or equal to this value. (optional)
    created_to = "2021-10-27T15:22:23.132757Z" # str | Return results where the `date_created` field (ISO 8601) is less than this value. (optional)
    deleted = True # bool | Returns only the deleted documents. (optional)
    id = "BhVzRcxH9Z2LgfPPGXFUBa" # str |  (optional)
    folder_uuid = "BhVzRcxH9Z2LgfPPGXFUBa" # str | The UUID of the folder where the documents are stored. (optional)
    form_id = "BhVzRcxH9Z2LgfPPGXFUBa" # str | Specify the form used for documents creation. This parameter can't be used with template_id. (optional)
    metadata = "metadata_example" # str | Specify metadata to filter by in the format of `metadata_{metadata-key}={metadata-value}` such as `metadata_opportunity_id=2181432`. The `metadata_` prefix is always required. (optional)
    modified_from = "2021-10-27T15:22:23.132757Z" # str | Return results where the `date_modified` field (iso-8601) is greater than or equal to this value. (optional)
    modified_to = "2021-10-27T15:22:23.132757Z" # str | Return results where the `date_modified` field (iso-8601) is less than this value. (optional)
    order_by = DocumentOrderingFieldsEnum("name") # DocumentOrderingFieldsEnum | Specify the order of documents to return. Use `value` (for example, `date_created`) for ASC and `-value` (for example, `-date_created`) for DESC. (optional)
    page = 1 # int | Specify which page of the dataset to return. (optional)
    q = "Sample Document" # str | Search query. Filter by document reference number (this token is stored on the template level) or name. (optional)
    status = DocumentStatusEnum(0) # DocumentStatusEnum | Specify the status of documents to return.   * 0: document.draft   * 1: document.sent   * 2: document.completed   * 3: document.uploaded   * 4: document.error   * 5: document.viewed   * 6: document.waiting_approval   * 7: document.approved   * 8: document.rejected   * 9: document.waiting_pay   * 10: document.paid   * 11: document.voided   * 12: document.declined  (optional)
    status__ne = DocumentStatusEnum(0) # DocumentStatusEnum | Specify the status of documents to return (exclude).   * 0: document.draft   * 1: document.sent   * 2: document.completed   * 3: document.uploaded   * 4: document.error   * 5: document.viewed   * 6: document.waiting_approval   * 7: document.approved   * 8: document.rejected   * 9: document.waiting_pay   * 10: document.paid   * 11: document.voided   * 12: document.declined  (optional)
    tag = "tag_1" # str | Search tag. Filter by document tag. (optional)
    template_id = "BhVzRcxH9Z2LgfPPGXFUBa" # str | Specify the template used for documents creation. Parameter can't be used with form_id. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List documents
        api_response = api_instance.document_list(completed_from=completed_from, completed_to=completed_to, count=count, created_from=created_from, created_to=created_to, deleted=deleted, id=id, folder_uuid=folder_uuid, form_id=form_id, metadata=metadata, modified_from=modified_from, modified_to=modified_to, order_by=order_by, page=page, q=q, status=status, status__ne=status__ne, tag=tag, template_id=template_id)
        pprint(api_response)
    except pandadoc_client.ApiException as e:
        print("Exception when calling DocumentsApi->document_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **completed_from** | **str**| Return results where the &#x60;date_completed&#x60; field (ISO 8601) is greater than or equal to this value. | [optional]
 **completed_to** | **str**| Return results where the &#x60;date_completed&#x60; field (ISO 8601) is less than or equal to this value. | [optional]
 **count** | **int**| Specify how many document results to return. Default is 50 documents, maximum is 100 documents. | [optional]
 **created_from** | **str**| Return results where the &#x60;date_created&#x60; field (ISO 8601) is greater than or equal to this value. | [optional]
 **created_to** | **str**| Return results where the &#x60;date_created&#x60; field (ISO 8601) is less than this value. | [optional]
 **deleted** | **bool**| Returns only the deleted documents. | [optional]
 **id** | **str**|  | [optional]
 **folder_uuid** | **str**| The UUID of the folder where the documents are stored. | [optional]
 **form_id** | **str**| Specify the form used for documents creation. This parameter can&#39;t be used with template_id. | [optional]
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **document_status**
> DocumentStatusResponse document_status(id)

Document status

### Example

* Api Key Authentication (apiKey):
* OAuth Authentication (oauth2):

```python
import time
import pandadoc_client
from pandadoc_client.api import documents_api
from pandadoc_client.model.document_status_response import DocumentStatusResponse
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
configuration.api_key['apiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Configure OAuth2 access token for authorization: oauth2
configuration = pandadoc_client.Configuration(
    host = "https://api.pandadoc.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pandadoc_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = documents_api.DocumentsApi(api_client)
    id = "id_example" # str | Specify document ID.

    # example passing only required values which don't have defaults set
    try:
        # Document status
        api_response = api_instance.document_status(id)
        pprint(api_response)
    except pandadoc_client.ApiException as e:
        print("Exception when calling DocumentsApi->document_status: %s\n" % e)
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

# **download_document**
> file_type download_document(id)

Document download

### Example

* Api Key Authentication (apiKey):
* OAuth Authentication (oauth2):

```python
import time
import pandadoc_client
from pandadoc_client.api import documents_api
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
configuration.api_key['apiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Configure OAuth2 access token for authorization: oauth2
configuration = pandadoc_client.Configuration(
    host = "https://api.pandadoc.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pandadoc_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = documents_api.DocumentsApi(api_client)
    id = "id_example" # str | Specify document ID.
    watermark_color = "watermark_color_example" # str | HEX code (for example `#RRGGBB`). (optional)
    watermark_font_size = 1 # int | Font size of the watermark. (optional)
    watermark_opacity = 3.14 # float | In range 0.0-1.0 (optional)
    watermark_text = "watermark_text_example" # str | Specify watermark text. (optional)

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
        api_response = api_instance.download_document(id, watermark_color=watermark_color, watermark_font_size=watermark_font_size, watermark_opacity=watermark_opacity, watermark_text=watermark_text)
        pprint(api_response)
    except pandadoc_client.ApiException as e:
        print("Exception when calling DocumentsApi->download_document: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Specify document ID. |
 **watermark_color** | **str**| HEX code (for example &#x60;#RRGGBB&#x60;). | [optional]
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_protected_document**
> file_type download_protected_document(id)

Download document protected

Download a signed PDF of a completed document

### Example

* Api Key Authentication (apiKey):
* OAuth Authentication (oauth2):

```python
import time
import pandadoc_client
from pandadoc_client.api import documents_api
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
configuration.api_key['apiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Configure OAuth2 access token for authorization: oauth2
configuration = pandadoc_client.Configuration(
    host = "https://api.pandadoc.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pandadoc_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = documents_api.DocumentsApi(api_client)
    id = "Mebvyy3NGsGBnY2rPLkH84" # str | Specify document ID.

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **linked_object_delete**
> linked_object_delete(id, linked_object_id)

Delete Linked Object

### Example

* Api Key Authentication (apiKey):
* OAuth Authentication (oauth2):

```python
import time
import pandadoc_client
from pandadoc_client.api import documents_api
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
configuration.api_key['apiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Configure OAuth2 access token for authorization: oauth2
configuration = pandadoc_client.Configuration(
    host = "https://api.pandadoc.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pandadoc_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = documents_api.DocumentsApi(api_client)
    id = "id_example" # str | Specify document ID.
    linked_object_id = "linked_object_id_example" # str | Specify linked object ID.

    # example passing only required values which don't have defaults set
    try:
        # Delete Linked Object
        api_instance.linked_object_delete(id, linked_object_id)
    except pandadoc_client.ApiException as e:
        print("Exception when calling DocumentsApi->linked_object_delete: %s\n" % e)
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **linked_object_list**
> LinkedObjectListResponse linked_object_list(id)

List Linked Objects

### Example

* Api Key Authentication (apiKey):
* OAuth Authentication (oauth2):

```python
import time
import pandadoc_client
from pandadoc_client.api import documents_api
from pandadoc_client.model.linked_object_list_response import LinkedObjectListResponse
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
configuration.api_key['apiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Configure OAuth2 access token for authorization: oauth2
configuration = pandadoc_client.Configuration(
    host = "https://api.pandadoc.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pandadoc_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = documents_api.DocumentsApi(api_client)
    id = "id_example" # str | Specify document ID.

    # example passing only required values which don't have defaults set
    try:
        # List Linked Objects
        api_response = api_instance.linked_object_list(id)
        pprint(api_response)
    except pandadoc_client.ApiException as e:
        print("Exception when calling DocumentsApi->linked_object_list: %s\n" % e)
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **linked_objects_create**
> LinkedObjectCreateResponse linked_objects_create(id, linked_object_create_request)

Create Linked Object

### Example

* Api Key Authentication (apiKey):
* OAuth Authentication (oauth2):

```python
import time
import pandadoc_client
from pandadoc_client.api import documents_api
from pandadoc_client.model.linked_object_create_response import LinkedObjectCreateResponse
from pandadoc_client.model.linked_object_create_request import LinkedObjectCreateRequest
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
configuration.api_key['apiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Configure OAuth2 access token for authorization: oauth2
configuration = pandadoc_client.Configuration(
    host = "https://api.pandadoc.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pandadoc_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = documents_api.DocumentsApi(api_client)
    id = "id_example" # str | Specify document ID.
    linked_object_create_request = LinkedObjectCreateRequest(None) # LinkedObjectCreateRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Create Linked Object
        api_response = api_instance.linked_objects_create(id, linked_object_create_request)
        pprint(api_response)
    except pandadoc_client.ApiException as e:
        print("Exception when calling DocumentsApi->linked_objects_create: %s\n" % e)
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_document**
> DocumentSendResponse send_document(id)

Send Document

### Example

* Api Key Authentication (apiKey):
* OAuth Authentication (oauth2):

```python
import time
import pandadoc_client
from pandadoc_client.api import documents_api
from pandadoc_client.model.document_send_response import DocumentSendResponse
from pandadoc_client.model.document_send_request import DocumentSendRequest
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
configuration.api_key['apiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Configure OAuth2 access token for authorization: oauth2
configuration = pandadoc_client.Configuration(
    host = "https://api.pandadoc.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pandadoc_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = documents_api.DocumentsApi(api_client)
    id = "id_example" # str | Document ID
    document_send_request = DocumentSendRequest(None) # DocumentSendRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Send Document
        api_response = api_instance.send_document(id)
        pprint(api_response)
    except pandadoc_client.ApiException as e:
        print("Exception when calling DocumentsApi->send_document: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Send Document
        api_response = api_instance.send_document(id, document_send_request=document_send_request)
        pprint(api_response)
    except pandadoc_client.ApiException as e:
        print("Exception when calling DocumentsApi->send_document: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Document ID |
 **document_send_request** | [**DocumentSendRequest**](DocumentSendRequest.md)|  | [optional]

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

