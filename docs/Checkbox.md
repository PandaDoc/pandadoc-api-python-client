# Checkbox


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
**value** | **bool** | Value of the Checkbox field. | [optional] 
**merge_field** | **str** |  | [optional] 

## Example

```python
from pandadoc_client.models.checkbox import Checkbox

# TODO update the JSON string below
json = "{}"
# create an instance of Checkbox from a JSON string
checkbox_instance = Checkbox.from_json(json)
# print the JSON string representation of the object
print(Checkbox.to_json())

# convert the object into a dict
checkbox_dict = checkbox_instance.to_dict()
# create an instance of Checkbox from a dict
checkbox_from_dict = Checkbox.from_dict(checkbox_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


