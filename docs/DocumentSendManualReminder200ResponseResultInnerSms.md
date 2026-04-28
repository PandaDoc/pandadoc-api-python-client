# DocumentSendManualReminder200ResponseResultInnerSms


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | Status of the SMS reminder attempt (sent or error). | [optional] 
**sent_at** | **datetime** | Timestamp of when the reminder was sent, in ISO 8601 format. | [optional] 
**detail** | **str** | Detailed explanation of why the reminder could not be sent, if applicable. | [optional] 

## Example

```python
from pandadoc_client.models.document_send_manual_reminder200_response_result_inner_sms import DocumentSendManualReminder200ResponseResultInnerSms

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentSendManualReminder200ResponseResultInnerSms from a JSON string
document_send_manual_reminder200_response_result_inner_sms_instance = DocumentSendManualReminder200ResponseResultInnerSms.from_json(json)
# print the JSON string representation of the object
print(DocumentSendManualReminder200ResponseResultInnerSms.to_json())

# convert the object into a dict
document_send_manual_reminder200_response_result_inner_sms_dict = document_send_manual_reminder200_response_result_inner_sms_instance.to_dict()
# create an instance of DocumentSendManualReminder200ResponseResultInnerSms from a dict
document_send_manual_reminder200_response_result_inner_sms_from_dict = DocumentSendManualReminder200ResponseResultInnerSms.from_dict(document_send_manual_reminder200_response_result_inner_sms_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


