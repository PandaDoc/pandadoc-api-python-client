# Text


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
**value** | **str** | Value of the Text field. | [optional] 
**merge_field** | **str** |  | [optional] 

## Example

```python
from pandadoc_client.models.text import Text

# TODO update the JSON string below
json = "{}"
# create an instance of Text from a JSON string
text_instance = Text.from_json(json)
# print the JSON string representation of the object
print(Text.to_json())

# convert the object into a dict
text_dict = text_instance.to_dict()
# create an instance of Text from a dict
text_from_dict = Text.from_dict(text_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


