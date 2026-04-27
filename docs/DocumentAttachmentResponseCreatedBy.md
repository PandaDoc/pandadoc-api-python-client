# DocumentAttachmentResponseCreatedBy


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**avatar** | **str** |  | [optional] 

## Example

```python
from pandadoc_client.models.document_attachment_response_created_by import DocumentAttachmentResponseCreatedBy

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentAttachmentResponseCreatedBy from a JSON string
document_attachment_response_created_by_instance = DocumentAttachmentResponseCreatedBy.from_json(json)
# print the JSON string representation of the object
print(DocumentAttachmentResponseCreatedBy.to_json())

# convert the object into a dict
document_attachment_response_created_by_dict = document_attachment_response_created_by_instance.to_dict()
# create an instance of DocumentAttachmentResponseCreatedBy from a dict
document_attachment_response_created_by_from_dict = DocumentAttachmentResponseCreatedBy.from_dict(document_attachment_response_created_by_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


