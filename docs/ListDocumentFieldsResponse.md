# ListDocumentFieldsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fields** | [**List[DocumentFieldsField]**](DocumentFieldsField.md) |  | [optional] 

## Example

```python
from pandadoc_client.models.list_document_fields_response import ListDocumentFieldsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListDocumentFieldsResponse from a JSON string
list_document_fields_response_instance = ListDocumentFieldsResponse.from_json(json)
# print the JSON string representation of the object
print(ListDocumentFieldsResponse.to_json())

# convert the object into a dict
list_document_fields_response_dict = list_document_fields_response_instance.to_dict()
# create an instance of ListDocumentFieldsResponse from a dict
list_document_fields_response_from_dict = ListDocumentFieldsResponse.from_dict(list_document_fields_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


