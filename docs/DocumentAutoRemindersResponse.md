# DocumentAutoRemindersResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**List[DocumentAutoRemindersResponseResultInner]**](DocumentAutoRemindersResponseResultInner.md) |  | [optional] 

## Example

```python
from pandadoc_client.models.document_auto_reminders_response import DocumentAutoRemindersResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentAutoRemindersResponse from a JSON string
document_auto_reminders_response_instance = DocumentAutoRemindersResponse.from_json(json)
# print the JSON string representation of the object
print(DocumentAutoRemindersResponse.to_json())

# convert the object into a dict
document_auto_reminders_response_dict = document_auto_reminders_response_instance.to_dict()
# create an instance of DocumentAutoRemindersResponse from a dict
document_auto_reminders_response_from_dict = DocumentAutoRemindersResponse.from_dict(document_auto_reminders_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


