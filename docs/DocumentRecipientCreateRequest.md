# DocumentRecipientCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Contact uuid. | 
**kind** | [**RecipientKindEnum**](RecipientKindEnum.md) |  | [default to RecipientKindEnum.CONTACT]

## Example

```python
from pandadoc_client.models.document_recipient_create_request import DocumentRecipientCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentRecipientCreateRequest from a JSON string
document_recipient_create_request_instance = DocumentRecipientCreateRequest.from_json(json)
# print the JSON string representation of the object
print(DocumentRecipientCreateRequest.to_json())

# convert the object into a dict
document_recipient_create_request_dict = document_recipient_create_request_instance.to_dict()
# create an instance of DocumentRecipientCreateRequest from a dict
document_recipient_create_request_from_dict = DocumentRecipientCreateRequest.from_dict(document_recipient_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


