# DocumentUpdateRequestTokensInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**value** | **str** |  | 

## Example

```python
from pandadoc_client.models.document_update_request_tokens_inner import DocumentUpdateRequestTokensInner

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentUpdateRequestTokensInner from a JSON string
document_update_request_tokens_inner_instance = DocumentUpdateRequestTokensInner.from_json(json)
# print the JSON string representation of the object
print(DocumentUpdateRequestTokensInner.to_json())

# convert the object into a dict
document_update_request_tokens_inner_dict = document_update_request_tokens_inner_instance.to_dict()
# create an instance of DocumentUpdateRequestTokensInner from a dict
document_update_request_tokens_inner_from_dict = DocumentUpdateRequestTokensInner.from_dict(document_update_request_tokens_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


