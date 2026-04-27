# UploadSectionByTemplateRequestAllOfContentPlaceholders


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content_library_items** | [**List[UploadSectionByTemplateRequestAllOfContentLibraryItems]**](UploadSectionByTemplateRequestAllOfContentLibraryItems.md) |  | [optional] 
**block_id** | **str** |  | 

## Example

```python
from pandadoc_client.models.upload_section_by_template_request_all_of_content_placeholders import UploadSectionByTemplateRequestAllOfContentPlaceholders

# TODO update the JSON string below
json = "{}"
# create an instance of UploadSectionByTemplateRequestAllOfContentPlaceholders from a JSON string
upload_section_by_template_request_all_of_content_placeholders_instance = UploadSectionByTemplateRequestAllOfContentPlaceholders.from_json(json)
# print the JSON string representation of the object
print(UploadSectionByTemplateRequestAllOfContentPlaceholders.to_json())

# convert the object into a dict
upload_section_by_template_request_all_of_content_placeholders_dict = upload_section_by_template_request_all_of_content_placeholders_instance.to_dict()
# create an instance of UploadSectionByTemplateRequestAllOfContentPlaceholders from a dict
upload_section_by_template_request_all_of_content_placeholders_from_dict = UploadSectionByTemplateRequestAllOfContentPlaceholders.from_dict(upload_section_by_template_request_all_of_content_placeholders_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


