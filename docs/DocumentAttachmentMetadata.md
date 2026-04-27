# DocumentAttachmentMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Optional name to set for uploaded file | [optional] 

## Example

```python
from pandadoc_client.models.document_attachment_metadata import DocumentAttachmentMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentAttachmentMetadata from a JSON string
document_attachment_metadata_instance = DocumentAttachmentMetadata.from_json(json)
# print the JSON string representation of the object
print(DocumentAttachmentMetadata.to_json())

# convert the object into a dict
document_attachment_metadata_dict = document_attachment_metadata_instance.to_dict()
# create an instance of DocumentAttachmentMetadata from a dict
document_attachment_metadata_from_dict = DocumentAttachmentMetadata.from_dict(document_attachment_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


