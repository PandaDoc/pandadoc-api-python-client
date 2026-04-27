# UpdateDocumentFieldsAssignmentRequest

Request body for updating field assignments on a document.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fields** | [**List[DocumentFieldAssignmentItem]**](DocumentFieldAssignmentItem.md) | An array of field assignment operations. Each item specifies a field and the recipient it should be assigned to. | 

## Example

```python
from pandadoc_client.models.update_document_fields_assignment_request import UpdateDocumentFieldsAssignmentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateDocumentFieldsAssignmentRequest from a JSON string
update_document_fields_assignment_request_instance = UpdateDocumentFieldsAssignmentRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateDocumentFieldsAssignmentRequest.to_json())

# convert the object into a dict
update_document_fields_assignment_request_dict = update_document_fields_assignment_request_instance.to_dict()
# create an instance of UpdateDocumentFieldsAssignmentRequest from a dict
update_document_fields_assignment_request_from_dict = UpdateDocumentFieldsAssignmentRequest.from_dict(update_document_fields_assignment_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


