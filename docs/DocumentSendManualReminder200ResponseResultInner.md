# DocumentSendManualReminder200ResponseResultInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recipient_id** | **str** | Unique identifier of the recipient. | [optional] 
**sms** | [**DocumentSendManualReminder200ResponseResultInnerSms**](DocumentSendManualReminder200ResponseResultInnerSms.md) |  | [optional] 
**email** | [**DocumentSendManualReminder200ResponseResultInnerEmail**](DocumentSendManualReminder200ResponseResultInnerEmail.md) |  | [optional] 
**email_customization** | [**DocumentSendManualReminder200ResponseResultInnerEmailCustomization**](DocumentSendManualReminder200ResponseResultInnerEmailCustomization.md) |  | [optional] 

## Example

```python
from pandadoc_client.models.document_send_manual_reminder200_response_result_inner import DocumentSendManualReminder200ResponseResultInner

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentSendManualReminder200ResponseResultInner from a JSON string
document_send_manual_reminder200_response_result_inner_instance = DocumentSendManualReminder200ResponseResultInner.from_json(json)
# print the JSON string representation of the object
print(DocumentSendManualReminder200ResponseResultInner.to_json())

# convert the object into a dict
document_send_manual_reminder200_response_result_inner_dict = document_send_manual_reminder200_response_result_inner_instance.to_dict()
# create an instance of DocumentSendManualReminder200ResponseResultInner from a dict
document_send_manual_reminder200_response_result_inner_from_dict = DocumentSendManualReminder200ResponseResultInner.from_dict(document_send_manual_reminder200_response_result_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


