# CreateDocumentEditingSession201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Internal id of the editing session. Don&#39;t use it, it&#39;s not a token. | [optional] 
**email** | **str** | Email associated with the editing session. | [optional] 
**expires_at** | **datetime** | Date and time when the editing session expires. | [optional] 
**key** | **str** | Same value as &#x60;token&#x60;, token for the embedded editor, aka E-Token. Deprecated — use &#x60;token&#x60; instead. | [optional] 
**token** | **str** | Token for the embedded editor, aka E-Token. Use it for your Embedding. | [optional] 
**document_id** | **str** | ID of the document | [optional] 

## Example

```python
from pandadoc_client.models.create_document_editing_session201_response import CreateDocumentEditingSession201Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateDocumentEditingSession201Response from a JSON string
create_document_editing_session201_response_instance = CreateDocumentEditingSession201Response.from_json(json)
# print the JSON string representation of the object
print(CreateDocumentEditingSession201Response.to_json())

# convert the object into a dict
create_document_editing_session201_response_dict = create_document_editing_session201_response_instance.to_dict()
# create an instance of CreateDocumentEditingSession201Response from a dict
create_document_editing_session201_response_from_dict = CreateDocumentEditingSession201Response.from_dict(create_document_editing_session201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


