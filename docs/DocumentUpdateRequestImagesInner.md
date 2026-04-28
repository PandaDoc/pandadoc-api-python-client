# DocumentUpdateRequestImagesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**urls** | **List[str]** |  | 
**name** | **str** |  | 

## Example

```python
from pandadoc_client.models.document_update_request_images_inner import DocumentUpdateRequestImagesInner

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentUpdateRequestImagesInner from a JSON string
document_update_request_images_inner_instance = DocumentUpdateRequestImagesInner.from_json(json)
# print the JSON string representation of the object
print(DocumentUpdateRequestImagesInner.to_json())

# convert the object into a dict
document_update_request_images_inner_dict = document_update_request_images_inner_instance.to_dict()
# create an instance of DocumentUpdateRequestImagesInner from a dict
document_update_request_images_inner_from_dict = DocumentUpdateRequestImagesInner.from_dict(document_update_request_images_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


