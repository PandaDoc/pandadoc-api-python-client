# DocumentSendManualReminderRequestRemindersInnerEmailCustomization

Optional customization settings for the reminder email. Defines the subject and body text used when sending the reminder via email. **This object is processed only if** `delivery_methods.email` is set to `true`. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subject** | **str** | Subject line of the reminder email sent to the recipient.  | [optional] 
**message** | **str** | Custom message body of the reminder email. Can include friendly or contextual text encouraging the recipient to complete the signing process.  Supports **Markdown** syntax for rich text formatting (e.g., bold, italics, links, and line breaks).  | [optional] 

## Example

```python
from pandadoc_client.models.document_send_manual_reminder_request_reminders_inner_email_customization import DocumentSendManualReminderRequestRemindersInnerEmailCustomization

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentSendManualReminderRequestRemindersInnerEmailCustomization from a JSON string
document_send_manual_reminder_request_reminders_inner_email_customization_instance = DocumentSendManualReminderRequestRemindersInnerEmailCustomization.from_json(json)
# print the JSON string representation of the object
print(DocumentSendManualReminderRequestRemindersInnerEmailCustomization.to_json())

# convert the object into a dict
document_send_manual_reminder_request_reminders_inner_email_customization_dict = document_send_manual_reminder_request_reminders_inner_email_customization_instance.to_dict()
# create an instance of DocumentSendManualReminderRequestRemindersInnerEmailCustomization from a dict
document_send_manual_reminder_request_reminders_inner_email_customization_from_dict = DocumentSendManualReminderRequestRemindersInnerEmailCustomization.from_dict(document_send_manual_reminder_request_reminders_inner_email_customization_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


