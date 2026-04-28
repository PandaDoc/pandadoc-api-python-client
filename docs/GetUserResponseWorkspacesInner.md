# GetUserResponseWorkspacesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role** | [**WorkspaceMemberRoleEnum**](WorkspaceMemberRoleEnum.md) |  | [optional] 
**workspace_id** | **str** | A user&#39;s workspace. | [optional] 
**membership_id** | **str** | A user&#39;s membership id in workspace. | [optional] 

## Example

```python
from pandadoc_client.models.get_user_response_workspaces_inner import GetUserResponseWorkspacesInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetUserResponseWorkspacesInner from a JSON string
get_user_response_workspaces_inner_instance = GetUserResponseWorkspacesInner.from_json(json)
# print the JSON string representation of the object
print(GetUserResponseWorkspacesInner.to_json())

# convert the object into a dict
get_user_response_workspaces_inner_dict = get_user_response_workspaces_inner_instance.to_dict()
# create an instance of GetUserResponseWorkspacesInner from a dict
get_user_response_workspaces_inner_from_dict = GetUserResponseWorkspacesInner.from_dict(get_user_response_workspaces_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


