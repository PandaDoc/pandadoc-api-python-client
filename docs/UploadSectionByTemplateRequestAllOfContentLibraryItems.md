# UploadSectionByTemplateRequestAllOfContentLibraryItems


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**fields** | **object** |  | [optional] 
**pricing_tables** | [**List[PricingTableRequest]**](PricingTableRequest.md) |  | [optional] 
**recipients** | [**List[DocumentCreateByTemplateRequestContentPlaceholdersInnerContentLibraryItemsInnerRecipientsInner]**](DocumentCreateByTemplateRequestContentPlaceholdersInnerContentLibraryItemsInnerRecipientsInner.md) |  | [optional] 

## Example

```python
from pandadoc_client.models.upload_section_by_template_request_all_of_content_library_items import UploadSectionByTemplateRequestAllOfContentLibraryItems

# TODO update the JSON string below
json = "{}"
# create an instance of UploadSectionByTemplateRequestAllOfContentLibraryItems from a JSON string
upload_section_by_template_request_all_of_content_library_items_instance = UploadSectionByTemplateRequestAllOfContentLibraryItems.from_json(json)
# print the JSON string representation of the object
print(UploadSectionByTemplateRequestAllOfContentLibraryItems.to_json())

# convert the object into a dict
upload_section_by_template_request_all_of_content_library_items_dict = upload_section_by_template_request_all_of_content_library_items_instance.to_dict()
# create an instance of UploadSectionByTemplateRequestAllOfContentLibraryItems from a dict
upload_section_by_template_request_all_of_content_library_items_from_dict = UploadSectionByTemplateRequestAllOfContentLibraryItems.from_dict(upload_section_by_template_request_all_of_content_library_items_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


