# DocumentCreateByTemplateRequestContentPlaceholdersInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content_library_items** | [**List[DocumentCreateByTemplateRequestContentPlaceholdersInnerContentLibraryItemsInner]**](DocumentCreateByTemplateRequestContentPlaceholdersInnerContentLibraryItemsInner.md) |  | [optional] 
**block_id** | **str** | Content placeholder block id | 

## Example

```python
from pandadoc_client.models.document_create_by_template_request_content_placeholders_inner import DocumentCreateByTemplateRequestContentPlaceholdersInner

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentCreateByTemplateRequestContentPlaceholdersInner from a JSON string
document_create_by_template_request_content_placeholders_inner_instance = DocumentCreateByTemplateRequestContentPlaceholdersInner.from_json(json)
# print the JSON string representation of the object
print(DocumentCreateByTemplateRequestContentPlaceholdersInner.to_json())

# convert the object into a dict
document_create_by_template_request_content_placeholders_inner_dict = document_create_by_template_request_content_placeholders_inner_instance.to_dict()
# create an instance of DocumentCreateByTemplateRequestContentPlaceholdersInner from a dict
document_create_by_template_request_content_placeholders_inner_from_dict = DocumentCreateByTemplateRequestContentPlaceholdersInner.from_dict(document_create_by_template_request_content_placeholders_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


