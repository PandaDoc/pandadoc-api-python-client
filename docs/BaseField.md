# BaseField


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** |  | [optional] 
**name** | **str** | Name of a field | [optional] 
**title** | **str** |  | [optional] 
**placeholder** | **str** | Placeholder of a field | [optional] 
**assigned_to** | [**BaseFieldAssignedTo**](BaseFieldAssignedTo.md) |  | [optional] 
**field_id** | **str** |  | [optional] 
**type** | [**FieldTypeEnum**](FieldTypeEnum.md) |  | [optional] 

## Example

```python
from pandadoc_client.models.base_field import BaseField

# TODO update the JSON string below
json = "{}"
# create an instance of BaseField from a JSON string
base_field_instance = BaseField.from_json(json)
# print the JSON string representation of the object
print(BaseField.to_json())

# convert the object into a dict
base_field_dict = base_field_instance.to_dict()
# create an instance of BaseField from a dict
base_field_from_dict = BaseField.from_dict(base_field_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


