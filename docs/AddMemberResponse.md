# AddMemberResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**member_id** | **str** |  | [optional] 
**workspace_id** | **str** |  | [optional] 
**role** | [**WorkspaceMemberRoleEnum**](WorkspaceMemberRoleEnum.md) |  | [optional] 
**email** | **str** |  | [optional] 
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 

## Example

```python
from pandadoc_client.models.add_member_response import AddMemberResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AddMemberResponse from a JSON string
add_member_response_instance = AddMemberResponse.from_json(json)
# print the JSON string representation of the object
print(AddMemberResponse.to_json())

# convert the object into a dict
add_member_response_dict = add_member_response_instance.to_dict()
# create an instance of AddMemberResponse from a dict
add_member_response_from_dict = AddMemberResponse.from_dict(add_member_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


