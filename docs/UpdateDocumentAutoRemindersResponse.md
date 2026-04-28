# UpdateDocumentAutoRemindersResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Toggles auto-reminders for the document.  If &#x60;true&#x60;, reminders are scheduled based on the configuration.  | 
**delivery_method** | [**DocumentDeliveryMethodEnum**](DocumentDeliveryMethodEnum.md) |  | [optional] 
**initial_delay_days** | **int** | Number of days to wait after sending the document before the first reminder is sent.  | [optional] 
**is_recurring** | **bool** | If &#x60;true&#x60;, reminders will be sent repeatedly at specified intervals after the initial reminder.  | [optional] 
**recurrence_frequency_days** | **int** | Number of days between recurring reminders, applicable if &#x60;is_recurring&#x60; is &#x60;true&#x60;.  | [optional] 

## Example

```python
from pandadoc_client.models.update_document_auto_reminders_response import UpdateDocumentAutoRemindersResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateDocumentAutoRemindersResponse from a JSON string
update_document_auto_reminders_response_instance = UpdateDocumentAutoRemindersResponse.from_json(json)
# print the JSON string representation of the object
print(UpdateDocumentAutoRemindersResponse.to_json())

# convert the object into a dict
update_document_auto_reminders_response_dict = update_document_auto_reminders_response_instance.to_dict()
# create an instance of UpdateDocumentAutoRemindersResponse from a dict
update_document_auto_reminders_response_from_dict = UpdateDocumentAutoRemindersResponse.from_dict(update_document_auto_reminders_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


