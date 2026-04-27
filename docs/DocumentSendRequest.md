# DocumentSendRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | A message that will be sent by email with a link to a document to sign. | [optional] 
**subject** | **str** | Value that will be used as the email subject. | [optional] 
**silent** | **bool** | If set to &#x60;true&#x60;, disables email notifications for document recipients and the document sender. Also disables scheduled reminders (manual reminders still possible). Doesn&#39;t affect \&quot;Approve document\&quot; email notification sent to the Approver. | [optional] 
**sender** | [**DocumentSendRequestSender**](DocumentSendRequestSender.md) |  | [optional] 
**forwarding_settings** | [**DocumentSendRequestForwardingSettings**](DocumentSendRequestForwardingSettings.md) |  | [optional] 
**reply_to** | **str** | Email address that will be used as a reply-to address for the document. To use this parameter, please contact the support team to have it enabled for your account.  | [optional] 
**selected_approvers** | [**DocumentSendRequestSelectedApprovers**](DocumentSendRequestSelectedApprovers.md) |  | [optional] 

## Example

```python
from pandadoc_client.models.document_send_request import DocumentSendRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentSendRequest from a JSON string
document_send_request_instance = DocumentSendRequest.from_json(json)
# print the JSON string representation of the object
print(DocumentSendRequest.to_json())

# convert the object into a dict
document_send_request_dict = document_send_request_instance.to_dict()
# create an instance of DocumentSendRequest from a dict
document_send_request_from_dict = DocumentSendRequest.from_dict(document_send_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


