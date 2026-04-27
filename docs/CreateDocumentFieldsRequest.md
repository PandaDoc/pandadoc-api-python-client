# CreateDocumentFieldsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fields** | [**List[DocumentFieldsFieldCreate]**](DocumentFieldsFieldCreate.md) | An array of fields to place on a document. | [optional] 

## Example

```python
from pandadoc_client.models.create_document_fields_request import CreateDocumentFieldsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateDocumentFieldsRequest from a JSON string
create_document_fields_request_instance = CreateDocumentFieldsRequest.from_json(json)
# print the JSON string representation of the object
print(CreateDocumentFieldsRequest.to_json())

# convert the object into a dict
create_document_fields_request_dict = create_document_fields_request_instance.to_dict()
# create an instance of CreateDocumentFieldsRequest from a dict
create_document_fields_request_from_dict = CreateDocumentFieldsRequest.from_dict(create_document_fields_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


