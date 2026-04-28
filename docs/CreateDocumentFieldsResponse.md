# CreateDocumentFieldsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fields** | [**List[DocumentFieldsField]**](DocumentFieldsField.md) |  | [optional] 

## Example

```python
from pandadoc_client.models.create_document_fields_response import CreateDocumentFieldsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateDocumentFieldsResponse from a JSON string
create_document_fields_response_instance = CreateDocumentFieldsResponse.from_json(json)
# print the JSON string representation of the object
print(CreateDocumentFieldsResponse.to_json())

# convert the object into a dict
create_document_fields_response_dict = create_document_fields_response_instance.to_dict()
# create an instance of CreateDocumentFieldsResponse from a dict
create_document_fields_response_from_dict = CreateDocumentFieldsResponse.from_dict(create_document_fields_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


