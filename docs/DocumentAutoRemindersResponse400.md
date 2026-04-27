# DocumentAutoRemindersResponse400


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**detail** | **str** | Reason why auto reminder settings could not be retrieved. | [optional] 

## Example

```python
from pandadoc_client.models.document_auto_reminders_response400 import DocumentAutoRemindersResponse400

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentAutoRemindersResponse400 from a JSON string
document_auto_reminders_response400_instance = DocumentAutoRemindersResponse400.from_json(json)
# print the JSON string representation of the object
print(DocumentAutoRemindersResponse400.to_json())

# convert the object into a dict
document_auto_reminders_response400_dict = document_auto_reminders_response400_instance.to_dict()
# create an instance of DocumentAutoRemindersResponse400 from a dict
document_auto_reminders_response400_from_dict = DocumentAutoRemindersResponse400.from_dict(document_auto_reminders_response400_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


