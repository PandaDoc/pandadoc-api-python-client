# ModelDate


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
**value** | **datetime** | Value of the Date field. | [optional] 
**merge_field** | **str** |  | [optional] 

## Example

```python
from pandadoc_client.models.model_date import ModelDate

# TODO update the JSON string below
json = "{}"
# create an instance of ModelDate from a JSON string
model_date_instance = ModelDate.from_json(json)
# print the JSON string representation of the object
print(ModelDate.to_json())

# convert the object into a dict
model_date_dict = model_date_instance.to_dict()
# create an instance of ModelDate from a dict
model_date_from_dict = ModelDate.from_dict(model_date_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


