# DocumentsFolderRenameRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Provide a new name for the folder. | 

## Example

```python
from pandadoc_client.models.documents_folder_rename_request import DocumentsFolderRenameRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentsFolderRenameRequest from a JSON string
documents_folder_rename_request_instance = DocumentsFolderRenameRequest.from_json(json)
# print the JSON string representation of the object
print(DocumentsFolderRenameRequest.to_json())

# convert the object into a dict
documents_folder_rename_request_dict = documents_folder_rename_request_instance.to_dict()
# create an instance of DocumentsFolderRenameRequest from a dict
documents_folder_rename_request_from_dict = DocumentsFolderRenameRequest.from_dict(documents_folder_rename_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


