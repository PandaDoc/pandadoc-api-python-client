# DocumentsFolderListResponseResultsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**date_created** | **str** |  | [optional] 
**has_folders** | **bool** |  | [optional] 
**has_items** | **bool** |  | [optional] 

## Example

```python
from pandadoc_client.models.documents_folder_list_response_results_inner import DocumentsFolderListResponseResultsInner

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentsFolderListResponseResultsInner from a JSON string
documents_folder_list_response_results_inner_instance = DocumentsFolderListResponseResultsInner.from_json(json)
# print the JSON string representation of the object
print(DocumentsFolderListResponseResultsInner.to_json())

# convert the object into a dict
documents_folder_list_response_results_inner_dict = documents_folder_list_response_results_inner_instance.to_dict()
# create an instance of DocumentsFolderListResponseResultsInner from a dict
documents_folder_list_response_results_inner_from_dict = DocumentsFolderListResponseResultsInner.from_dict(documents_folder_list_response_results_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


