# Dropdown


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
**value** | **str** | Value of the Dropdown field. | [optional] 
**merge_field** | **str** |  | [optional] 

## Example

```python
from pandadoc_client.models.dropdown import Dropdown

# TODO update the JSON string below
json = "{}"
# create an instance of Dropdown from a JSON string
dropdown_instance = Dropdown.from_json(json)
# print the JSON string representation of the object
print(Dropdown.to_json())

# convert the object into a dict
dropdown_dict = dropdown_instance.to_dict()
# create an instance of Dropdown from a dict
dropdown_from_dict = Dropdown.from_dict(dropdown_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


