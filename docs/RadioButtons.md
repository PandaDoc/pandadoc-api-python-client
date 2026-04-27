# RadioButtons


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** |  | [optional] 
**name** | **str** | Name of a field | [optional] 
**title** | **str** |  | [optional] 
**placeholder** | **str** | Placeholder of a field | [optional] 
**assigned_to** | [**BaseFieldAssignedTo**](BaseFieldAssignedTo.md) |  | [optional] 
**field_id** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**value** | **str** | Value of the Radio Buttons field. | [optional] 
**merge_field** | **str** |  | [optional] 

## Example

```python
from pandadoc_client.models.radio_buttons import RadioButtons

# TODO update the JSON string below
json = "{}"
# create an instance of RadioButtons from a JSON string
radio_buttons_instance = RadioButtons.from_json(json)
# print the JSON string representation of the object
print(RadioButtons.to_json())

# convert the object into a dict
radio_buttons_dict = radio_buttons_instance.to_dict()
# create an instance of RadioButtons from a dict
radio_buttons_from_dict = RadioButtons.from_dict(radio_buttons_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


