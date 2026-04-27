# ListWorkspacesResponseResultsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | A unique identifier of a workspace in a organization | [optional] 
**name** | **str** | A workspace&#39;s name | [optional] 
**date_created** | **str** | A workspace&#39;s date creation | [optional] 
**owner** | **str** | A owner&#39;s email address | [optional] 

## Example

```python
from pandadoc_client.models.list_workspaces_response_results_inner import ListWorkspacesResponseResultsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ListWorkspacesResponseResultsInner from a JSON string
list_workspaces_response_results_inner_instance = ListWorkspacesResponseResultsInner.from_json(json)
# print the JSON string representation of the object
print(ListWorkspacesResponseResultsInner.to_json())

# convert the object into a dict
list_workspaces_response_results_inner_dict = list_workspaces_response_results_inner_instance.to_dict()
# create an instance of ListWorkspacesResponseResultsInner from a dict
list_workspaces_response_results_inner_from_dict = ListWorkspacesResponseResultsInner.from_dict(list_workspaces_response_results_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


