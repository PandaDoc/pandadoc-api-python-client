# RemoveMember400Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**detail** | **str** |  | [optional] 

## Example

```python
from pandadoc_client.models.remove_member400_response import RemoveMember400Response

# TODO update the JSON string below
json = "{}"
# create an instance of RemoveMember400Response from a JSON string
remove_member400_response_instance = RemoveMember400Response.from_json(json)
# print the JSON string representation of the object
print(RemoveMember400Response.to_json())

# convert the object into a dict
remove_member400_response_dict = remove_member400_response_instance.to_dict()
# create an instance of RemoveMember400Response from a dict
remove_member400_response_from_dict = RemoveMember400Response.from_dict(remove_member400_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


