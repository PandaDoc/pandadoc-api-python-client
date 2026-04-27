# DocumentListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[DocumentListResponseResultsInner]**](DocumentListResponseResultsInner.md) |  | [optional] 

## Example

```python
from pandadoc_client.models.document_list_response import DocumentListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentListResponse from a JSON string
document_list_response_instance = DocumentListResponse.from_json(json)
# print the JSON string representation of the object
print(DocumentListResponse.to_json())

# convert the object into a dict
document_list_response_dict = document_list_response_instance.to_dict()
# create an instance of DocumentListResponse from a dict
document_list_response_from_dict = DocumentListResponse.from_dict(document_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


