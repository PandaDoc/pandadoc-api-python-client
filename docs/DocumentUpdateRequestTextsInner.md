# DocumentUpdateRequestTextsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the text block to update. | 
**data** | **str** | The rich text content to be inserted into the block. Supports markdown. | 

## Example

```python
from pandadoc_client.models.document_update_request_texts_inner import DocumentUpdateRequestTextsInner

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentUpdateRequestTextsInner from a JSON string
document_update_request_texts_inner_instance = DocumentUpdateRequestTextsInner.from_json(json)
# print the JSON string representation of the object
print(DocumentUpdateRequestTextsInner.to_json())

# convert the object into a dict
document_update_request_texts_inner_dict = document_update_request_texts_inner_instance.to_dict()
# create an instance of DocumentUpdateRequestTextsInner from a dict
document_update_request_texts_inner_from_dict = DocumentUpdateRequestTextsInner.from_dict(document_update_request_texts_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


