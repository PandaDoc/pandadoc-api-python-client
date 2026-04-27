# DocumentAutoRemindersResponseResultInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recipient_id** | **str** | Unique identifier of the recipient. | [optional] 
**status** | **str** | Status of the reminder attempt (sent, error, scheduled). | [optional] 

## Example

```python
from pandadoc_client.models.document_auto_reminders_response_result_inner import DocumentAutoRemindersResponseResultInner

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentAutoRemindersResponseResultInner from a JSON string
document_auto_reminders_response_result_inner_instance = DocumentAutoRemindersResponseResultInner.from_json(json)
# print the JSON string representation of the object
print(DocumentAutoRemindersResponseResultInner.to_json())

# convert the object into a dict
document_auto_reminders_response_result_inner_dict = document_auto_reminders_response_result_inner_instance.to_dict()
# create an instance of DocumentAutoRemindersResponseResultInner from a dict
document_auto_reminders_response_result_inner_from_dict = DocumentAutoRemindersResponseResultInner.from_dict(document_auto_reminders_response_result_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


