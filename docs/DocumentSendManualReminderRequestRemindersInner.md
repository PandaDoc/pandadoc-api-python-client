# DocumentSendManualReminderRequestRemindersInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recipient_id** | **str** | Unique identifier of the recipient to receive the reminder. | [optional] 
**delivery_methods** | [**RecipientDeliveryMethods**](RecipientDeliveryMethods.md) |  | [optional] 
**email_customization** | [**DocumentSendManualReminderRequestRemindersInnerEmailCustomization**](DocumentSendManualReminderRequestRemindersInnerEmailCustomization.md) |  | [optional] 

## Example

```python
from pandadoc_client.models.document_send_manual_reminder_request_reminders_inner import DocumentSendManualReminderRequestRemindersInner

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentSendManualReminderRequestRemindersInner from a JSON string
document_send_manual_reminder_request_reminders_inner_instance = DocumentSendManualReminderRequestRemindersInner.from_json(json)
# print the JSON string representation of the object
print(DocumentSendManualReminderRequestRemindersInner.to_json())

# convert the object into a dict
document_send_manual_reminder_request_reminders_inner_dict = document_send_manual_reminder_request_reminders_inner_instance.to_dict()
# create an instance of DocumentSendManualReminderRequestRemindersInner from a dict
document_send_manual_reminder_request_reminders_inner_from_dict = DocumentSendManualReminderRequestRemindersInner.from_dict(document_send_manual_reminder_request_reminders_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


