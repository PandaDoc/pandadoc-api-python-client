# CollectFile


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
**value** | [**CollectFileAllOfValue**](CollectFileAllOfValue.md) |  | [optional] 

## Example

```python
from pandadoc_client.models.collect_file import CollectFile

# TODO update the JSON string below
json = "{}"
# create an instance of CollectFile from a JSON string
collect_file_instance = CollectFile.from_json(json)
# print the JSON string representation of the object
print(CollectFile.to_json())

# convert the object into a dict
collect_file_dict = collect_file_instance.to_dict()
# create an instance of CollectFile from a dict
collect_file_from_dict = CollectFile.from_dict(collect_file_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


