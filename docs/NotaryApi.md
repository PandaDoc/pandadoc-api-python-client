# pandadoc_client.NotaryApi

All URIs are relative to *https://api.pandadoc.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_notarization_request**](NotaryApi.md#create_notarization_request) | **POST** /public/v2/notary/notarization-requests | Create Notarization Request
[**delete_notarization_request**](NotaryApi.md#delete_notarization_request) | **DELETE** /public/v2/notary/notarization-requests/{session_request_id} | Delete Notarization Request
[**list_notaries**](NotaryApi.md#list_notaries) | **GET** /public/v2/notary/notaries | List Notaries
[**list_notarization_requests**](NotaryApi.md#list_notarization_requests) | **GET** /public/v2/notary/notarization-requests | List Notarization Requests
[**notarization_request_details**](NotaryApi.md#notarization_request_details) | **GET** /public/v2/notary/notarization-requests/{session_request_id} | Notarization Request Details


# **create_notarization_request**
> CreateNotarizationResponse create_notarization_request(create_notarization_request)

Create Notarization Request

Create a notarization request to connect with a notary and complete online notarizations for your signers within minutes.

> 🚧 **Important:** This endpoint supports only documents in draft status.

## Prerequisites

> 🚧 Before you start
> 
> Ensure the following before creating a notarization request:
> 
> - Install the Notary On-Demand or Notary add-on
> - Create a document for notarization and get its `document_id`. To create a document, use the [Create Document from Template](https://developers.pandadoc.com/reference/create-document-from-pandadoc-template) or [Create Document from File Upload](https://developers.pandadoc.com/reference/create-document-from-pdf) endpoint.

## Request Details

For the notarization request, include in the request body:

- `document_id`
- At least one `invitees`, specifying their `email`, `first_name`, and `last_name`
- Optionally, include a `message` for your signers
- Optionally, using `disable_invitees_notifications` you can disable all notifications for invitees including email with invitation for notarization. This is useful when you are using alternative delivery methods.
- If in-house notary must be assigned to this request, include the `notary` object with the notary's `id`, `scheduled_at` timestamp, and an optional `message` for the notary

After the API call is executed, your signers will receive an email invitation for notarization. Alternatively, you can directly share the `notarization_link` with your signers, which is available in the 201 response body.

Upon successful notarization, you will receive an email with a link to the notarized document.

## Usage Tips

> 📘 Best Practices
> 
> - Ensure that signers are added as both invitees in the request body and recipients in the document to avoid inconveniences during notary sessions
> - Signers will receive an email with a notary link upon a successful API call; this link is also in the 201 response
> - In case if notary is not specified in the request, signers will use the link to connect with commissioned online notaries, available Mon-Fri, 9 AM - 9 PM Central Time, typically responding within 2 minutes
> - If notary is specified, signers will use the link to connect with your in-house notary at the scheduled time

## Limits

A maximum of 100 API calls per minute is permitted. Exceeding this limit triggers a 429 Too Many Requests error.

## Troubleshooting

**Solutions for 4xx Response Codes:**

- **403 Forbidden (Inactive Add-on)**: Ensure the Notary On-Demand or Notary add-on is installed
- **403 Forbidden (Transactions Limit)**: Purchase additional transactions either through the Notary UI or by contacting the Sales team
- **429 Too Many Requests**: If you hit the limit, hold your API calls, then send them after waiting for the retry time

> 📘 To learn more about PandaDoc Notary On-Demand, visit our [website](https://notary.pandadoc.com/notary-on-demand/).


### Example

* Api Key Authentication (apiKey):
* OAuth Authentication (oauth2):

```python
import pandadoc_client
from pandadoc_client.models.create_notarization_request import CreateNotarizationRequest
from pandadoc_client.models.create_notarization_response import CreateNotarizationResponse
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
    api_instance = pandadoc_client.NotaryApi(api_client)
    create_notarization_request = {"document_id":"D3okRfgHRX7NEhavcACReB","disable_invitees_notifications":true,"invitation":{"message":"Your session is ready","invitees":[{"email":"signer@example.com","first_name":"test","last_name":"test"}]}} # CreateNotarizationRequest | 

    try:
        # Create Notarization Request
        api_response = api_instance.create_notarization_request(create_notarization_request)
        print("The response of NotaryApi->create_notarization_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotaryApi->create_notarization_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_notarization_request** | [**CreateNotarizationRequest**](CreateNotarizationRequest.md)|  | 

### Return type

[**CreateNotarizationResponse**](CreateNotarizationResponse.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Notarization request has been created successfully |  -  |
**400** | Bad Request error |  -  |
**401** | Authentication error |  -  |
**403** | Permission error |  -  |
**429** | Too many requests error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_notarization_request**
> delete_notarization_request(session_request_id)

Delete Notarization Request

Use this method to delete a notarization request.
Once notarization request is deleted it cannot be restored.

> 🚧 Notarization Request status
> 
> You can only delete a notarization request in status 'SENT', 'WAITING_FOR_NOTARY' or 'INCOMPLETE'. 
> If the notarization request is in any other status, the request will return a 400 Bad Request error.

By default all invitees will receive email notification about deletion of the notarization request. 
If you want to disable this notification, you can use the `disable_invitees_notifications` parameter when creating request (see [Create Notarization Request](https://developers.pandadoc.com/reference/create-notarization-request)).


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
    api_instance = pandadoc_client.NotaryApi(api_client)
    session_request_id = '0b2256a2-5803-4ae9-b1b8-595f48e37173' # str | Notarization Request ID.

    try:
        # Delete Notarization Request
        api_instance.delete_notarization_request(session_request_id)
    except Exception as e:
        print("Exception when calling NotaryApi->delete_notarization_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_request_id** | **str**| Notarization Request ID. | 

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
**400** | Bad Request error |  -  |
**403** | Permission error |  -  |
**404** | Not found error |  -  |
**429** | Too many requests error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_notaries**
> ListNotariesResponse list_notaries(status=status, commission_state=commission_state, offset=offset, limit=limit, order_by=order_by)

List Notaries

Retrieve a list of notaries associated with your organization.

## Important Notes

- At the moment, notaries can be added to organization only manually through the PandaDoc Notary UI. 
- Organization must have Notary addon enabled to use this endpoint


### Example

* Api Key Authentication (apiKey):
* OAuth Authentication (oauth2):

```python
import pandadoc_client
from pandadoc_client.models.list_notaries_response import ListNotariesResponse
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
    api_instance = pandadoc_client.NotaryApi(api_client)
    status = ['[\"ACTIVE\",\"UNDER_REVIEW\"]'] # List[str] | Filter by status (comma-separated values supported). Valid values are INVITED, UNDER_REVIEW, ACTIVE, REJECTED, INACTIVE (optional)
    commission_state = ['[\"California\",\"Arizona\"]'] # List[str] | Filter by commission state (comma-separated values supported) (optional)
    offset = 0 # int | Number of results to skip (optional) (default to 0)
    limit = 50 # int | Maximum number of results to return (optional) (default to 50)
    order_by = email # str | Sort by name, email, or status (default is email). Use a - prefix for descending order (e.g., -email) (optional) (default to email)

    try:
        # List Notaries
        api_response = api_instance.list_notaries(status=status, commission_state=commission_state, offset=offset, limit=limit, order_by=order_by)
        print("The response of NotaryApi->list_notaries:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotaryApi->list_notaries: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status** | [**List[str]**](str.md)| Filter by status (comma-separated values supported). Valid values are INVITED, UNDER_REVIEW, ACTIVE, REJECTED, INACTIVE | [optional] 
 **commission_state** | [**List[str]**](str.md)| Filter by commission state (comma-separated values supported) | [optional] 
 **offset** | **int**| Number of results to skip | [optional] [default to 0]
 **limit** | **int**| Maximum number of results to return | [optional] [default to 50]
 **order_by** | **str**| Sort by name, email, or status (default is email). Use a - prefix for descending order (e.g., -email) | [optional] [default to email]

### Return type

[**ListNotariesResponse**](ListNotariesResponse.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of notaries retrieved successfully |  -  |
**400** | Bad Request error |  -  |
**403** | Permission error |  -  |
**429** | Too many requests error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_notarization_requests**
> ListNotarizationRequestsResponse list_notarization_requests(status=status, created_by_user_id=created_by_user_id, document_id=document_id, offset=offset, limit=limit, order_by=order_by)

List Notarization Requests

Retrieve a paginated list of notarization requests for your organization.

Results can be filtered by status, creator, or document, and sorted by status or by the request's creation or completion dates.

## Permissions

> 🔒 **Requirements**
>
> - The **Notary On-Demand** or **Notary** add-on must be enabled for your organization. Without an active add-on, the endpoint returns `403 Forbidden`.
> - The request is executed with the permissions of the API key owner. By default, the response only includes notarization requests created by the API key owner. To list notarization requests created by any user in the organization, the API key owner must have the **Can view any notarization request** permission.

## Limits

A maximum of 100 API calls per minute is permitted. Exceeding this limit triggers a 429 Too Many Requests error.


### Example

* Api Key Authentication (apiKey):
* OAuth Authentication (oauth2):

```python
import pandadoc_client
from pandadoc_client.models.list_notarization_requests_response import ListNotarizationRequestsResponse
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
    api_instance = pandadoc_client.NotaryApi(api_client)
    status = ['[\"SENT\"]'] # List[str] | Filter by status (comma-separated values supported). (optional)
    created_by_user_id = ['[\"nyAnVpY7pZ23FBve8s9xgk\"]'] # List[str] | Filter by creator user ID (comma-separated values supported). (optional)
    document_id = ['[\"D3okRfgHRX7NEhavcACReB\"]'] # List[str] | Filter by document ID (comma-separated values supported). (optional)
    offset = 0 # int | Number of results to skip. (optional) (default to 0)
    limit = 50 # int | Maximum number of results to return. (optional) (default to 50)
    order_by = date_created # str | Sort field. Use a `-` prefix for descending order (e.g., `-date_created`). When omitted, results are sorted by `date_created` ascending (oldest first).  (optional) (default to date_created)

    try:
        # List Notarization Requests
        api_response = api_instance.list_notarization_requests(status=status, created_by_user_id=created_by_user_id, document_id=document_id, offset=offset, limit=limit, order_by=order_by)
        print("The response of NotaryApi->list_notarization_requests:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotaryApi->list_notarization_requests: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status** | [**List[str]**](str.md)| Filter by status (comma-separated values supported). | [optional] 
 **created_by_user_id** | [**List[str]**](str.md)| Filter by creator user ID (comma-separated values supported). | [optional] 
 **document_id** | [**List[str]**](str.md)| Filter by document ID (comma-separated values supported). | [optional] 
 **offset** | **int**| Number of results to skip. | [optional] [default to 0]
 **limit** | **int**| Maximum number of results to return. | [optional] [default to 50]
 **order_by** | **str**| Sort field. Use a &#x60;-&#x60; prefix for descending order (e.g., &#x60;-date_created&#x60;). When omitted, results are sorted by &#x60;date_created&#x60; ascending (oldest first).  | [optional] [default to date_created]

### Return type

[**ListNotarizationRequestsResponse**](ListNotarizationRequestsResponse.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Paginated list of notarization requests |  -  |
**400** | Bad Request error |  -  |
**401** | Authentication error |  -  |
**403** | Permission error |  -  |
**429** | Too many requests error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **notarization_request_details**
> NotarizationRequestDetailsResponse notarization_request_details(session_request_id)

Notarization Request Details

Get details about a notarization request by its `id`.

Details include:

- Basic notarization request information (status, creator, invitees).
- Signed documents information with links for downloading.
- Notarization session recording information with link for downloading.
- Timestamps associated with a notarization request.
- Termination reason and details when the notarization session was not completed successfully.

## Available Notarization Request Statuses

The following is a complete list of all possible notarization request statuses returned:

| Notarization Request Status | Status Description                                                                                                 |
| :-------------------------- | :----------------------------------------------------------------------------------------------------------------- |
| SENT                        | Notarization request has been created. Invitees are notified and can start the process of finding a notary.        |
| WAITING_FOR_NOTARY          | One of the invitees initialised the process of finding a notary.                                                   |
| ACCEPTED                    | Notarization request has been accepted by the notary. At this time nobody has joined the notarization session yet. |
| LIVE                        | Notarization session has started.                                                                                  |
| COMPLETED                   | Notarization session is finished. Documents have been successfully signed and ready for downloading.               |
| INCOMPLETE                  | Notarization session has started but was not completed successfully.                                               |

## Signed documents

Signed documents are the documents that were successfully signed during the notarization session. The signed document's info is available only if the notarization request has `COMPLETED` status, otherwise the returned list will be empty.  

In case you uploaded several documents for notarization then the `signed_documents` list will contain links for downloading for each document separately (with `SINGLE` document type) and link for the combined document (with `COMBINED` document type accordingly).

## Recording

Recording is the video of the notarization session. The recording info is available only if the notarization request has `COMPLETED` status and recording is available, otherwise the returned object will be empty.

> 📘 Links expire in 1 hour
> 
> **Note**: The signed document and recording links expire in 1 hour. After this time it will be not possible to download files using the returned urls. In this case you need to call endpoint again since each request generates a new link.

## Limits

A maximum of 100 API calls per minute is permitted. Exceeding this limit triggers a 429 Too Many Requests error.


### Example

* Api Key Authentication (apiKey):
* OAuth Authentication (oauth2):

```python
import pandadoc_client
from pandadoc_client.models.notarization_request_details_response import NotarizationRequestDetailsResponse
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
    api_instance = pandadoc_client.NotaryApi(api_client)
    session_request_id = '0b2256a2-5803-4ae9-b1b8-595f48e37173' # str | Notarization Request ID.

    try:
        # Notarization Request Details
        api_response = api_instance.notarization_request_details(session_request_id)
        print("The response of NotaryApi->notarization_request_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotaryApi->notarization_request_details: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_request_id** | **str**| Notarization Request ID. | 

### Return type

[**NotarizationRequestDetailsResponse**](NotarizationRequestDetailsResponse.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Details about notarization request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

