# Initials


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
**value** | **object** | Value of the Initials field. Always empty object. | [optional] 

## Example

```python
from pandadoc_client.models.initials import Initials

# TODO update the JSON string below
json = "{}"
# create an instance of Initials from a JSON string
initials_instance = Initials.from_json(json)
# print the JSON string representation of the object
print(Initials.to_json())

# convert the object into a dict
initials_dict = initials_instance.to_dict()
# create an instance of Initials from a dict
initials_from_dict = Initials.from_dict(initials_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


