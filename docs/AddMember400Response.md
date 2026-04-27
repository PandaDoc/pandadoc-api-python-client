# AddMember400Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**detail** | **object** |  | [optional] 

## Example

```python
from pandadoc_client.models.add_member400_response import AddMember400Response

# TODO update the JSON string below
json = "{}"
# create an instance of AddMember400Response from a JSON string
add_member400_response_instance = AddMember400Response.from_json(json)
# print the JSON string representation of the object
print(AddMember400Response.to_json())

# convert the object into a dict
add_member400_response_dict = add_member400_response_instance.to_dict()
# create an instance of AddMember400Response from a dict
add_member400_response_from_dict = AddMember400Response.from_dict(add_member400_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


