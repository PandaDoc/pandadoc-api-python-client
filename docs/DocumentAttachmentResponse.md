# DocumentAttachmentResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** |  | [optional] 
**date_created** | **str** |  | [optional] 
**created_by** | [**DocumentAttachmentResponseCreatedBy**](DocumentAttachmentResponseCreatedBy.md) |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from pandadoc_client.models.document_attachment_response import DocumentAttachmentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentAttachmentResponse from a JSON string
document_attachment_response_instance = DocumentAttachmentResponse.from_json(json)
# print the JSON string representation of the object
print(DocumentAttachmentResponse.to_json())

# convert the object into a dict
document_attachment_response_dict = document_attachment_response_instance.to_dict()
# create an instance of DocumentAttachmentResponse from a dict
document_attachment_response_from_dict = DocumentAttachmentResponse.from_dict(document_attachment_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


