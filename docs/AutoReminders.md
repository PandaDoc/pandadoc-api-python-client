# AutoReminders


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
from pandadoc_client.models.auto_reminders import AutoReminders

# TODO update the JSON string below
json = "{}"
# create an instance of AutoReminders from a JSON string
auto_reminders_instance = AutoReminders.from_json(json)
# print the JSON string representation of the object
print(AutoReminders.to_json())

# convert the object into a dict
auto_reminders_dict = auto_reminders_instance.to_dict()
# create an instance of AutoReminders from a dict
auto_reminders_from_dict = AutoReminders.from_dict(auto_reminders_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


