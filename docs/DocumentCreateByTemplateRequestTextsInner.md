# DocumentCreateByTemplateRequestTextsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the Text Block to update. This name is defined in the template. | 
**data** | **str** | The text content to be inserted into the block. Supports markdown. | 

## Example

```python
from pandadoc_client.models.document_create_by_template_request_texts_inner import DocumentCreateByTemplateRequestTextsInner

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentCreateByTemplateRequestTextsInner from a JSON string
document_create_by_template_request_texts_inner_instance = DocumentCreateByTemplateRequestTextsInner.from_json(json)
# print the JSON string representation of the object
print(DocumentCreateByTemplateRequestTextsInner.to_json())

# convert the object into a dict
document_create_by_template_request_texts_inner_dict = document_create_by_template_request_texts_inner_instance.to_dict()
# create an instance of DocumentCreateByTemplateRequestTextsInner from a dict
document_create_by_template_request_texts_inner_from_dict = DocumentCreateByTemplateRequestTextsInner.from_dict(document_create_by_template_request_texts_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


