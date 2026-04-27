# DocumentRecipientResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recipient_id** | **str** |  | [optional] 

## Example

```python
from pandadoc_client.models.document_recipient_response import DocumentRecipientResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentRecipientResponse from a JSON string
document_recipient_response_instance = DocumentRecipientResponse.from_json(json)
# print the JSON string representation of the object
print(DocumentRecipientResponse.to_json())

# convert the object into a dict
document_recipient_response_dict = document_recipient_response_instance.to_dict()
# create an instance of DocumentRecipientResponse from a dict
document_recipient_response_from_dict = DocumentRecipientResponse.from_dict(document_recipient_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


