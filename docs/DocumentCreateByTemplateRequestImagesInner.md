# DocumentCreateByTemplateRequestImagesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**urls** | **List[str]** |  | 
**name** | **str** |  | 

## Example

```python
from pandadoc_client.models.document_create_by_template_request_images_inner import DocumentCreateByTemplateRequestImagesInner

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentCreateByTemplateRequestImagesInner from a JSON string
document_create_by_template_request_images_inner_instance = DocumentCreateByTemplateRequestImagesInner.from_json(json)
# print the JSON string representation of the object
print(DocumentCreateByTemplateRequestImagesInner.to_json())

# convert the object into a dict
document_create_by_template_request_images_inner_dict = document_create_by_template_request_images_inner_instance.to_dict()
# create an instance of DocumentCreateByTemplateRequestImagesInner from a dict
document_create_by_template_request_images_inner_from_dict = DocumentCreateByTemplateRequestImagesInner.from_dict(document_create_by_template_request_images_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


