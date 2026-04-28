# DocumentsFolderCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name the folder for the Documents you are creating. | 
**parent_uuid** | **str** | ID of the parent folder. To create a new folder in the root folder, remove this parameter in the request. | [optional] 

## Example

```python
from pandadoc_client.models.documents_folder_create_request import DocumentsFolderCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentsFolderCreateRequest from a JSON string
documents_folder_create_request_instance = DocumentsFolderCreateRequest.from_json(json)
# print the JSON string representation of the object
print(DocumentsFolderCreateRequest.to_json())

# convert the object into a dict
documents_folder_create_request_dict = documents_folder_create_request_instance.to_dict()
# create an instance of DocumentsFolderCreateRequest from a dict
documents_folder_create_request_from_dict = DocumentsFolderCreateRequest.from_dict(documents_folder_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


