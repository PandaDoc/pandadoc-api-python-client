# DocumentSendManualReminderRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reminders** | [**List[DocumentSendManualReminderRequestRemindersInner]**](DocumentSendManualReminderRequestRemindersInner.md) | A list of reminders to be sent to specified recipients. Use this field to specify which recipients should receive a reminder and through which delivery methods.  Each email reminder contains document sender in the From field,  ensuring the recipient always sees consistent sender details and branding.  | [optional] 

## Example

```python
from pandadoc_client.models.document_send_manual_reminder_request import DocumentSendManualReminderRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentSendManualReminderRequest from a JSON string
document_send_manual_reminder_request_instance = DocumentSendManualReminderRequest.from_json(json)
# print the JSON string representation of the object
print(DocumentSendManualReminderRequest.to_json())

# convert the object into a dict
document_send_manual_reminder_request_dict = document_send_manual_reminder_request_instance.to_dict()
# create an instance of DocumentSendManualReminderRequest from a dict
document_send_manual_reminder_request_from_dict = DocumentSendManualReminderRequest.from_dict(document_send_manual_reminder_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


