# CreateUserRequestWorkspacesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workspace_id** | **str** |  | [optional] 
**role** | [**WorkspaceMemberRoleEnum**](WorkspaceMemberRoleEnum.md) |  | [optional] 

## Example

```python
from pandadoc_client.models.create_user_request_workspaces_inner import CreateUserRequestWorkspacesInner

# TODO update the JSON string below
json = "{}"
# create an instance of CreateUserRequestWorkspacesInner from a JSON string
create_user_request_workspaces_inner_instance = CreateUserRequestWorkspacesInner.from_json(json)
# print the JSON string representation of the object
print(CreateUserRequestWorkspacesInner.to_json())

# convert the object into a dict
create_user_request_workspaces_inner_dict = create_user_request_workspaces_inner_instance.to_dict()
# create an instance of CreateUserRequestWorkspacesInner from a dict
create_user_request_workspaces_inner_from_dict = CreateUserRequestWorkspacesInner.from_dict(create_user_request_workspaces_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


