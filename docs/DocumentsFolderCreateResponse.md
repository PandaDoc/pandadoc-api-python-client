# DocumentsFolderCreateResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**date_created** | **str** |  | [optional] 

## Example

```python
from pandadoc_client.models.documents_folder_create_response import DocumentsFolderCreateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentsFolderCreateResponse from a JSON string
documents_folder_create_response_instance = DocumentsFolderCreateResponse.from_json(json)
# print the JSON string representation of the object
print(DocumentsFolderCreateResponse.to_json())

# convert the object into a dict
documents_folder_create_response_dict = documents_folder_create_response_instance.to_dict()
# create an instance of DocumentsFolderCreateResponse from a dict
documents_folder_create_response_from_dict = DocumentsFolderCreateResponse.from_dict(documents_folder_create_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


