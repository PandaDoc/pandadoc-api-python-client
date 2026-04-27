# pandadoc_client.DocumentRemindersApi

All URIs are relative to *https://api.pandadoc.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_manual_reminder**](DocumentRemindersApi.md#create_manual_reminder) | **POST** /public/v1/documents/{document_id}/send-reminder | Send Manual Reminder
[**get_document_auto_reminder_settings**](DocumentRemindersApi.md#get_document_auto_reminder_settings) | **GET** /public/v1/documents/{document_id}/auto-reminders | Document Auto Reminder Settings
[**status_document_auto_reminder**](DocumentRemindersApi.md#status_document_auto_reminder) | **GET** /public/v1/documents/{document_id}/auto-reminders/status | Document Auto Reminder Status
[**update_document_auto_reminder_settings**](DocumentRemindersApi.md#update_document_auto_reminder_settings) | **PATCH** /public/v1/documents/{document_id}/auto-reminders | Update Document Auto Reminder Settings


# **create_manual_reminder**
> DocumentSendManualReminder200Response create_manual_reminder(document_id, document_send_manual_reminder_request)

Send Manual Reminder

Sends manual reminders to one or more recipients of a specified document.


### Example

* Api Key Authentication (apiKey):
* OAuth Authentication (oauth2):

```python
import pandadoc_client
from pandadoc_client.models.document_send_manual_reminder200_response import DocumentSendManualReminder200Response
from pandadoc_client.models.document_send_manual_reminder_request import DocumentSendManualReminderRequest
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
    api_instance = pandadoc_client.DocumentRemindersApi(api_client)
    document_id = 'BhVzRcxH9Z2LgfPPGXFUBa' # str | The UUID of the document.
    document_send_manual_reminder_request = {"reminders":[{"recipient_id":"2eWSKSvVqmuVCnuUK3iWwD","delivery_methods":{"email":true,"sms":false}},{"recipient_id":"7JhSDcvLQa9uR7kBX8mYeK","delivery_methods":{"email":true,"sms":true}}]} # DocumentSendManualReminderRequest | 

    try:
        # Send Manual Reminder
        api_response = api_instance.create_manual_reminder(document_id, document_send_manual_reminder_request)
        print("The response of DocumentRemindersApi->create_manual_reminder:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentRemindersApi->create_manual_reminder: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_id** | **str**| The UUID of the document. | 
 **document_send_manual_reminder_request** | [**DocumentSendManualReminderRequest**](DocumentSendManualReminderRequest.md)|  | 

### Return type

[**DocumentSendManualReminder200Response**](DocumentSendManualReminder200Response.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully processed reminder requests. Returns an array of objects, where each object details the outcome of the reminder delivery attempt for a specific recipient.  |  -  |
**401** | Authentication error |  -  |
**403** | Permission error |  -  |
**404** | Not found |  -  |
**409** | Returned when a manual reminder cannot be sent due to the document&#39;s current status. This occurs when:   - The document has not been sent yet.   - The document is in a final state (e.g., completed, paid, declined, or expired).   - The document is in \&quot;suggesting mode,\&quot; during which reminders are disabled.  |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_document_auto_reminder_settings**
> AutoReminders get_document_auto_reminder_settings(document_id)

Document Auto Reminder Settings

Retrieves the current auto reminder configuration for a specified document.


### Example

* Api Key Authentication (apiKey):
* OAuth Authentication (oauth2):

```python
import pandadoc_client
from pandadoc_client.models.auto_reminders import AutoReminders
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
    api_instance = pandadoc_client.DocumentRemindersApi(api_client)
    document_id = 'BhVzRcxH9Z2LgfPPGXFUBa' # str | The UUID of the document.

    try:
        # Document Auto Reminder Settings
        api_response = api_instance.get_document_auto_reminder_settings(document_id)
        print("The response of DocumentRemindersApi->get_document_auto_reminder_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentRemindersApi->get_document_auto_reminder_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_id** | **str**| The UUID of the document. | 

### Return type

[**AutoReminders**](AutoReminders.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Auto reminder settings retrieved successfully. |  -  |
**400** | Returned when auto reminder settings could not be retrieved from the document. This occurs when document is in a final state (e.g., completed, paid, declined, or expired).  |  -  |
**401** | Authentication error |  -  |
**403** | Permission error |  -  |
**404** | Not found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **status_document_auto_reminder**
> DocumentAutoRemindersResponse status_document_auto_reminder(document_id)

Document Auto Reminder Status

Retrieves the current auto reminder status per recipient for a specified document. Recipients who could not receive
reminders due to validations (recipient groups, non-signers, etc.) will be skipped and not included in the response.


### Example

* Api Key Authentication (apiKey):
* OAuth Authentication (oauth2):

```python
import pandadoc_client
from pandadoc_client.models.document_auto_reminders_response import DocumentAutoRemindersResponse
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
    api_instance = pandadoc_client.DocumentRemindersApi(api_client)
    document_id = 'BhVzRcxH9Z2LgfPPGXFUBa' # str | The UUID of the document.

    try:
        # Document Auto Reminder Status
        api_response = api_instance.status_document_auto_reminder(document_id)
        print("The response of DocumentRemindersApi->status_document_auto_reminder:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentRemindersApi->status_document_auto_reminder: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_id** | **str**| The UUID of the document. | 

### Return type

[**DocumentAutoRemindersResponse**](DocumentAutoRemindersResponse.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Auto reminder status retrieved successfully. |  -  |
**400** | Returned when auto reminder status could not be retrieved due to the document&#39;s current status or  reminders configuration. This occurs when:   - The document has not been sent yet.   - The document is in a final state (e.g., completed, paid, declined, or expired).   - The auto reminders are disabled in the document settings.  |  -  |
**401** | Authentication error |  -  |
**403** | Permission error |  -  |
**404** | Not found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_document_auto_reminder_settings**
> UpdateDocumentAutoRemindersResponse update_document_auto_reminder_settings(document_id, update_document_auto_reminders_request)

Update Document Auto Reminder Settings

Configures automatic reminders for document recipients. 
These reminders are sent after the document's initial dispatch. 
Settings include enabling reminders, delivery method (email/SMS), initial delay, 
and recurrence frequency.


### Example

* Api Key Authentication (apiKey):
* OAuth Authentication (oauth2):

```python
import pandadoc_client
from pandadoc_client.models.update_document_auto_reminders_request import UpdateDocumentAutoRemindersRequest
from pandadoc_client.models.update_document_auto_reminders_response import UpdateDocumentAutoRemindersResponse
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
    api_instance = pandadoc_client.DocumentRemindersApi(api_client)
    document_id = 'BhVzRcxH9Z2LgfPPGXFUBa' # str | The UUID of the document.
    update_document_auto_reminders_request = {"enabled":true,"delivery_method":"email","initial_delay_days":3,"is_recurring":true,"recurrence_frequency_days":5} # UpdateDocumentAutoRemindersRequest | 

    try:
        # Update Document Auto Reminder Settings
        api_response = api_instance.update_document_auto_reminder_settings(document_id, update_document_auto_reminders_request)
        print("The response of DocumentRemindersApi->update_document_auto_reminder_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentRemindersApi->update_document_auto_reminder_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_id** | **str**| The UUID of the document. | 
 **update_document_auto_reminders_request** | [**UpdateDocumentAutoRemindersRequest**](UpdateDocumentAutoRemindersRequest.md)|  | 

### Return type

[**UpdateDocumentAutoRemindersResponse**](UpdateDocumentAutoRemindersResponse.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Auto reminder settings updated successfully. |  -  |
**400** | Returned when auto reminder settings could not be retrieved from the document. This occurs when document is in a final state (e.g., completed, paid, declined, or expired).  |  -  |
**401** | Authentication error |  -  |
**403** | Permission error |  -  |
**404** | Not found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

