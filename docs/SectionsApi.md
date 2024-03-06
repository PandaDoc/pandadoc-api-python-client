# pandadoc_client.SectionsApi

All URIs are relative to *https://api.pandadoc.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_sections**](SectionsApi.md#list_sections) | **GET** /public/v1/documents/{document_id}/sections | List sections
[**section_details**](SectionsApi.md#section_details) | **GET** /public/v1/documents/{document_id}/sections/uploads/{upload_id} | Section details
[**section_info**](SectionsApi.md#section_info) | **GET** /public/v1/documents/{document_id}/sections/{section_id} | Section Info
[**upload_section**](SectionsApi.md#upload_section) | **POST** /public/v1/documents/{document_id}/sections/uploads | Upload section


# **list_sections**
> UploadSectionListResponse list_sections(document_id)

List sections

### Example

* Api Key Authentication (apiKey):
* OAuth Authentication (oauth2):

```python
import pandadoc_client
from pandadoc_client.api import sections_api
from pandadoc_client.model.upload_section_list_response import UploadSectionListResponse
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
    api_instance = sections_api.SectionsApi(api_client)
    document_id = "BhVzRcxH9Z2LgfPPGXFUBa"  # str | Document ID

    # example passing only required values which don't have defaults set
    try:
        # List sections
        api_response = api_instance.list_sections(document_id)
        pprint(api_response)
    except pandadoc_client.ApiException as e:
        print("Exception when calling SectionsApi->list_sections: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_id** | **str**| Document ID |

### Return type

[**UploadSectionListResponse**](UploadSectionListResponse.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **section_details**
> UploadSectionStatusResponse section_details(document_id, upload_id)

Section details

### Example

* Api Key Authentication (apiKey):
* OAuth Authentication (oauth2):

```python
import pandadoc_client
from pandadoc_client.api import sections_api
from pandadoc_client.model.upload_section_status_response import UploadSectionStatusResponse
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
    api_instance = sections_api.SectionsApi(api_client)
    document_id = "BhVzRcxH9Z2LgfPPGXFUBa"  # str | Document ID
    upload_id = "LQ6cUT7xevPLUEgJeF8Zrm"  # str | Upload ID

    # example passing only required values which don't have defaults set
    try:
        # Section details
        api_response = api_instance.section_details(document_id, upload_id)
        pprint(api_response)
    except pandadoc_client.ApiException as e:
        print("Exception when calling SectionsApi->section_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_id** | **str**| Document ID |
 **upload_id** | **str**| Upload ID |

### Return type

[**UploadSectionStatusResponse**](UploadSectionStatusResponse.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **section_info**
> SectionInfoResponse section_info(document_id, section_id)

Section Info

### Example

* Api Key Authentication (apiKey):
* OAuth Authentication (oauth2):

```python
import pandadoc_client
from pandadoc_client.api import sections_api
from pandadoc_client.model.section_info_response import SectionInfoResponse
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
    api_instance = sections_api.SectionsApi(api_client)
    document_id = "BhVzRcxH9Z2LgfPPGXFUBa"  # str | Document ID
    section_id = "LQ6cUT7xevPLUEgJeF8Zrm"  # str | Section ID

    # example passing only required values which don't have defaults set
    try:
        # Section Info
        api_response = api_instance.section_info(document_id, section_id)
        pprint(api_response)
    except pandadoc_client.ApiException as e:
        print("Exception when calling SectionsApi->section_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_id** | **str**| Document ID |
 **section_id** | **str**| Section ID |

### Return type

[**SectionInfoResponse**](SectionInfoResponse.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **upload_section**
> UploadSectionResponse upload_section(document_id, upload_section_request)

Upload section

### Example

* Api Key Authentication (apiKey):
* OAuth Authentication (oauth2):

```python
import pandadoc_client
from pandadoc_client.api import sections_api
from pandadoc_client.model.upload_section_request import UploadSectionRequest
from pandadoc_client.model.upload_section_response import UploadSectionResponse
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
    api_instance = sections_api.SectionsApi(api_client)
    document_id = "BhVzRcxH9Z2LgfPPGXFUBa"  # str | Document ID
    upload_section_request = UploadSectionRequest(
        name="API Sample Section from PandaDoc Template",
        template_uuid="hryJY9mqYZHjQCYQuSjRQg",
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
        tags=["created_via_api","test_document"],
        pricing_tables=[
            PricingTableRequest(
                name="Pricing Table 1",
                data_merge=True,
                options={},
                sections=[
                    PricingTableRequestSections(
                        title="Sample Section",
                        default=True,
                        multichoice_enabled=False,
                        rows=[
                            PricingTableRequestRows(
                                options=PricingTableRequestRowOptions(
                                    qty_editable=True,
                                    optional_selected=True,
                                    optional=True,
                                ),
                                data={},
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
                                options={},
                                sections=[
                                    PricingTableRequestSections(
                                        title="Sample Section",
                                        default=True,
                                        multichoice_enabled=False,
                                        rows=[
                                            PricingTableRequestRows(
                                                options=PricingTableRequestRowOptions(
                                                    qty_editable=True,
                                                    optional_selected=True,
                                                    optional=True,
                                                ),
                                                data={},
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
    )  # UploadSectionRequest | Use a PandaDoc template or an existing PDF to upload a section. See the creation request examples [by template](/schemas/UploadSectionByTemplateRequest) and [by pdf](/schemas/UploadSectionByPdfRequest) 

    # example passing only required values which don't have defaults set
    try:
        # Upload section
        api_response = api_instance.upload_section(document_id, upload_section_request)
        pprint(api_response)
    except pandadoc_client.ApiException as e:
        print("Exception when calling SectionsApi->upload_section: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_id** | **str**| Document ID |
 **upload_section_request** | [**UploadSectionRequest**](UploadSectionRequest.md)| Use a PandaDoc template or an existing PDF to upload a section. See the creation request examples [by template](/schemas/UploadSectionByTemplateRequest) and [by pdf](/schemas/UploadSectionByPdfRequest)  |

### Return type

[**UploadSectionResponse**](UploadSectionResponse.md)

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

