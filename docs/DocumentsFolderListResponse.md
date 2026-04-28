# DocumentsFolderListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[DocumentsFolderListResponseResultsInner]**](DocumentsFolderListResponseResultsInner.md) |  | [optional] 

## Example

```python
from pandadoc_client.models.documents_folder_list_response import DocumentsFolderListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentsFolderListResponse from a JSON string
documents_folder_list_response_instance = DocumentsFolderListResponse.from_json(json)
# print the JSON string representation of the object
print(DocumentsFolderListResponse.to_json())

# convert the object into a dict
documents_folder_list_response_dict = documents_folder_list_response_instance.to_dict()
# create an instance of DocumentsFolderListResponse from a dict
documents_folder_list_response_from_dict = DocumentsFolderListResponse.from_dict(documents_folder_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


