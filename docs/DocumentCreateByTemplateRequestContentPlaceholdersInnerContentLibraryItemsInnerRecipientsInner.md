# DocumentCreateByTemplateRequestContentPlaceholdersInnerContentLibraryItemsInnerRecipientsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | [optional] 
**phone** | **str** |  | [optional] 
**delivery_methods** | [**RecipientDeliveryMethods**](RecipientDeliveryMethods.md) |  | [optional] 
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**role** | **str** |  | [optional] 
**signing_order** | **int** |  | [optional] 
**redirect** | [**RecipientRedirect**](RecipientRedirect.md) |  | [optional] 

## Example

```python
from pandadoc_client.models.document_create_by_template_request_content_placeholders_inner_content_library_items_inner_recipients_inner import DocumentCreateByTemplateRequestContentPlaceholdersInnerContentLibraryItemsInnerRecipientsInner

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentCreateByTemplateRequestContentPlaceholdersInnerContentLibraryItemsInnerRecipientsInner from a JSON string
document_create_by_template_request_content_placeholders_inner_content_library_items_inner_recipients_inner_instance = DocumentCreateByTemplateRequestContentPlaceholdersInnerContentLibraryItemsInnerRecipientsInner.from_json(json)
# print the JSON string representation of the object
print(DocumentCreateByTemplateRequestContentPlaceholdersInnerContentLibraryItemsInnerRecipientsInner.to_json())

# convert the object into a dict
document_create_by_template_request_content_placeholders_inner_content_library_items_inner_recipients_inner_dict = document_create_by_template_request_content_placeholders_inner_content_library_items_inner_recipients_inner_instance.to_dict()
# create an instance of DocumentCreateByTemplateRequestContentPlaceholdersInnerContentLibraryItemsInnerRecipientsInner from a dict
document_create_by_template_request_content_placeholders_inner_content_library_items_inner_recipients_inner_from_dict = DocumentCreateByTemplateRequestContentPlaceholdersInnerContentLibraryItemsInnerRecipientsInner.from_dict(document_create_by_template_request_content_placeholders_inner_content_library_items_inner_recipients_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


