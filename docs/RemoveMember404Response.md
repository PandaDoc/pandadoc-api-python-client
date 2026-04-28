# RemoveMember404Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**detail** | **str** |  | [optional] 

## Example

```python
from pandadoc_client.models.remove_member404_response import RemoveMember404Response

# TODO update the JSON string below
json = "{}"
# create an instance of RemoveMember404Response from a JSON string
remove_member404_response_instance = RemoveMember404Response.from_json(json)
# print the JSON string representation of the object
print(RemoveMember404Response.to_json())

# convert the object into a dict
remove_member404_response_dict = remove_member404_response_instance.to_dict()
# create an instance of RemoveMember404Response from a dict
remove_member404_response_from_dict = RemoveMember404Response.from_dict(remove_member404_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


