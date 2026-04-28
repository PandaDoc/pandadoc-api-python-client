# DocumentAttachmentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Optional name to set for uploaded file | [optional] 
**source** | **str** | URL link to the file to be attached to a document | [optional] 

## Example

```python
from pandadoc_client.models.document_attachment_request import DocumentAttachmentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentAttachmentRequest from a JSON string
document_attachment_request_instance = DocumentAttachmentRequest.from_json(json)
# print the JSON string representation of the object
print(DocumentAttachmentRequest.to_json())

# convert the object into a dict
document_attachment_request_dict = document_attachment_request_instance.to_dict()
# create an instance of DocumentAttachmentRequest from a dict
document_attachment_request_from_dict = DocumentAttachmentRequest.from_dict(document_attachment_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


