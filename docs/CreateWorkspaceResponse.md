# CreateWorkspaceResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from pandadoc_client.models.create_workspace_response import CreateWorkspaceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateWorkspaceResponse from a JSON string
create_workspace_response_instance = CreateWorkspaceResponse.from_json(json)
# print the JSON string representation of the object
print(CreateWorkspaceResponse.to_json())

# convert the object into a dict
create_workspace_response_dict = create_workspace_response_instance.to_dict()
# create an instance of CreateWorkspaceResponse from a dict
create_workspace_response_from_dict = CreateWorkspaceResponse.from_dict(create_workspace_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


