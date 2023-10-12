# pandadoc_client.DocumentRecipientsApi

All URIs are relative to *https://api.pandadoc.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_document_recipient**](DocumentRecipientsApi.md#add_document_recipient) | **POST** /public/v1/documents/{id}/recipients | Add Document Recipient
[**delete_document_recipient**](DocumentRecipientsApi.md#delete_document_recipient) | **DELETE** /public/v1/documents/{id}/recipients/{recipient_id} | Delete Document Recipient
[**edit_document_recipient**](DocumentRecipientsApi.md#edit_document_recipient) | **PATCH** /public/v1/documents/{id}/recipients/{recipient_id} | Edit Document Recipient
[**reassign_document_recipient**](DocumentRecipientsApi.md#reassign_document_recipient) | **POST** /public/v1/documents/{id}/recipients/{recipient_id}/reassign | Reassign Document Recipient


# **add_document_recipient**
> add_document_recipient(id, document_recipient_create_request)

Add Document Recipient

Adds recipient as CC to document

### Example

* Api Key Authentication (apiKey):
* OAuth Authentication (oauth2):

```python
import pandadoc_client
from pandadoc_client.api import document_recipients_api
from pandadoc_client.model.document_recipient_create_request import DocumentRecipientCreateRequest
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
    api_instance = document_recipients_api.DocumentRecipientsApi(api_client)
    id = "BhVzRcxH9Z2LgfPPGXFUBa"  # str | Document UUID
    document_recipient_create_request = DocumentRecipientCreateRequest(
        id="2eWSKSvVqmuVCnuUK3iWwD",
        kind="contact",
    )  # DocumentRecipientCreateRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Add Document Recipient
        api_instance.add_document_recipient(id, document_recipient_create_request)
    except pandadoc_client.ApiException as e:
        print("Exception when calling DocumentRecipientsApi->add_document_recipient: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Document UUID |
 **document_recipient_create_request** | [**DocumentRecipientCreateRequest**](DocumentRecipientCreateRequest.md)|  |

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **delete_document_recipient**
> delete_document_recipient(id, recipient_id)

Delete Document Recipient

Deleted recipient from document

### Example

* Api Key Authentication (apiKey):
* OAuth Authentication (oauth2):

```python
import pandadoc_client
from pandadoc_client.api import document_recipients_api
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
    api_instance = document_recipients_api.DocumentRecipientsApi(api_client)
    id = "BhVzRcxH9Z2LgfPPGXFUBa"  # str | Document UUID
    recipient_id = "tf5dGS3Tmu3cj228ao6fnc"  # str | Recipient UUID

    # example passing only required values which don't have defaults set
    try:
        # Delete Document Recipient
        api_instance.delete_document_recipient(id, recipient_id)
    except pandadoc_client.ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **edit_document_recipient**
> edit_document_recipient(id, recipient_id, document_recipient_edit_request)

Edit Document Recipient

Edit document recipient's details

### Example

* Api Key Authentication (apiKey):
* OAuth Authentication (oauth2):

```python
import pandadoc_client
from pandadoc_client.api import document_recipients_api
from pandadoc_client.model.document_recipient_edit_request import DocumentRecipientEditRequest
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
    api_instance = document_recipients_api.DocumentRecipientsApi(api_client)
    id = "BhVzRcxH9Z2LgfPPGXFUBa"  # str | Document UUID
    recipient_id = "tf5dGS3Tmu3cj228ao6fnc"  # str | Recipient UUID
    document_recipient_edit_request = DocumentRecipientEditRequest(
        email="user01@pandadoc.com",
        first_name="John",
        last_name="Doe",
        company="John Doe Inc.",
        job_title="CTO",
        phone="+14842634627",
        state="Texas",
        street_address="1313 Mockingbird Lane",
        city="Austin",
        postal_code="75001",
    )  # DocumentRecipientEditRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Edit Document Recipient
        api_instance.edit_document_recipient(id, recipient_id, document_recipient_edit_request)
    except pandadoc_client.ApiException as e:
        print("Exception when calling DocumentRecipientsApi->edit_document_recipient: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Document UUID |
 **recipient_id** | **str**| Recipient UUID |
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **reassign_document_recipient**
> reassign_document_recipient(id, recipient_id, document_recipient_create_request)

Reassign Document Recipient

Replace document recipient with another contact

### Example

* Api Key Authentication (apiKey):
* OAuth Authentication (oauth2):

```python
import pandadoc_client
from pandadoc_client.api import document_recipients_api
from pandadoc_client.model.document_recipient_create_request import DocumentRecipientCreateRequest
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
    api_instance = document_recipients_api.DocumentRecipientsApi(api_client)
    id = "BhVzRcxH9Z2LgfPPGXFUBa"  # str | Document UUID
    recipient_id = "tf5dGS3Tmu3cj228ao6fnc"  # str | Recipient UUID
    document_recipient_create_request = DocumentRecipientCreateRequest(
        id="2eWSKSvVqmuVCnuUK3iWwD",
        kind="contact",
    )  # DocumentRecipientCreateRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Reassign Document Recipient
        api_instance.reassign_document_recipient(id, recipient_id, document_recipient_create_request)
    except pandadoc_client.ApiException as e:
        print("Exception when calling DocumentRecipientsApi->reassign_document_recipient: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Document UUID |
 **recipient_id** | **str**| Recipient UUID |
 **document_recipient_create_request** | [**DocumentRecipientCreateRequest**](DocumentRecipientCreateRequest.md)|  |

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

