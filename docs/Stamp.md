# Stamp


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
**value** | **object** | Value of the Stamp field. Always empty object. | [optional] 

## Example

```python
from pandadoc_client.models.stamp import Stamp

# TODO update the JSON string below
json = "{}"
# create an instance of Stamp from a JSON string
stamp_instance = Stamp.from_json(json)
# print the JSON string representation of the object
print(Stamp.to_json())

# convert the object into a dict
stamp_dict = stamp_instance.to_dict()
# create an instance of Stamp from a dict
stamp_from_dict = Stamp.from_dict(stamp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


