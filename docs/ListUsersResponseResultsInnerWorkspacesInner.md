# ListUsersResponseResultsInnerWorkspacesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role** | **str** | A user&#39;s role in workspace. | [optional] 
**workspace_id** | **str** | A user&#39;s workspace. | [optional] 
**membership_id** | **str** | A user&#39;s membership id in workspace. | [optional] 

## Example

```python
from pandadoc_client.models.list_users_response_results_inner_workspaces_inner import ListUsersResponseResultsInnerWorkspacesInner

# TODO update the JSON string below
json = "{}"
# create an instance of ListUsersResponseResultsInnerWorkspacesInner from a JSON string
list_users_response_results_inner_workspaces_inner_instance = ListUsersResponseResultsInnerWorkspacesInner.from_json(json)
# print the JSON string representation of the object
print(ListUsersResponseResultsInnerWorkspacesInner.to_json())

# convert the object into a dict
list_users_response_results_inner_workspaces_inner_dict = list_users_response_results_inner_workspaces_inner_instance.to_dict()
# create an instance of ListUsersResponseResultsInnerWorkspacesInner from a dict
list_users_response_results_inner_workspaces_inner_from_dict = ListUsersResponseResultsInnerWorkspacesInner.from_dict(list_users_response_results_inner_workspaces_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


