# DocumentRevertToDraftResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**date_created** | **str** |  | [optional] 
**date_modified** | **str** |  | [optional] 
**expiration_date** | **str** |  | [optional] 
**version** | **str** |  | [optional] 

## Example

```python
from pandadoc_client.models.document_revert_to_draft_response import DocumentRevertToDraftResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentRevertToDraftResponse from a JSON string
document_revert_to_draft_response_instance = DocumentRevertToDraftResponse.from_json(json)
# print the JSON string representation of the object
print(DocumentRevertToDraftResponse.to_json())

# convert the object into a dict
document_revert_to_draft_response_dict = document_revert_to_draft_response_instance.to_dict()
# create an instance of DocumentRevertToDraftResponse from a dict
document_revert_to_draft_response_from_dict = DocumentRevertToDraftResponse.from_dict(document_revert_to_draft_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


