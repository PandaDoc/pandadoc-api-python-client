# DocumentCreateByTemplateRequestContentPlaceholdersInnerContentLibraryItemsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Content library item id | 
**fields** | **object** |  | [optional] 
**pricing_tables** | [**List[PricingTableRequest]**](PricingTableRequest.md) |  | [optional] 
**recipients** | [**List[DocumentCreateByTemplateRequestContentPlaceholdersInnerContentLibraryItemsInnerRecipientsInner]**](DocumentCreateByTemplateRequestContentPlaceholdersInnerContentLibraryItemsInnerRecipientsInner.md) |  | [optional] 

## Example

```python
from pandadoc_client.models.document_create_by_template_request_content_placeholders_inner_content_library_items_inner import DocumentCreateByTemplateRequestContentPlaceholdersInnerContentLibraryItemsInner

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentCreateByTemplateRequestContentPlaceholdersInnerContentLibraryItemsInner from a JSON string
document_create_by_template_request_content_placeholders_inner_content_library_items_inner_instance = DocumentCreateByTemplateRequestContentPlaceholdersInnerContentLibraryItemsInner.from_json(json)
# print the JSON string representation of the object
print(DocumentCreateByTemplateRequestContentPlaceholdersInnerContentLibraryItemsInner.to_json())

# convert the object into a dict
document_create_by_template_request_content_placeholders_inner_content_library_items_inner_dict = document_create_by_template_request_content_placeholders_inner_content_library_items_inner_instance.to_dict()
# create an instance of DocumentCreateByTemplateRequestContentPlaceholdersInnerContentLibraryItemsInner from a dict
document_create_by_template_request_content_placeholders_inner_content_library_items_inner_from_dict = DocumentCreateByTemplateRequestContentPlaceholdersInnerContentLibraryItemsInner.from_dict(document_create_by_template_request_content_placeholders_inner_content_library_items_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


