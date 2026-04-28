# CreateUserResponseWorkspacesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workspace_id** | **str** |  | [optional] 
**role** | **str** |  | [optional] 
**member_id** | **str** |  | [optional] 

## Example

```python
from pandadoc_client.models.create_user_response_workspaces_inner import CreateUserResponseWorkspacesInner

# TODO update the JSON string below
json = "{}"
# create an instance of CreateUserResponseWorkspacesInner from a JSON string
create_user_response_workspaces_inner_instance = CreateUserResponseWorkspacesInner.from_json(json)
# print the JSON string representation of the object
print(CreateUserResponseWorkspacesInner.to_json())

# convert the object into a dict
create_user_response_workspaces_inner_dict = create_user_response_workspaces_inner_instance.to_dict()
# create an instance of CreateUserResponseWorkspacesInner from a dict
create_user_response_workspaces_inner_from_dict = CreateUserResponseWorkspacesInner.from_dict(create_user_response_workspaces_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


