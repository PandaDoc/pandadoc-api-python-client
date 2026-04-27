# DocumentFieldsFieldAssignedTo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**phone** | **str** |  | [optional] 
**recipient_type** | **str** |  | [optional] 
**has_completed** | **bool** |  | [optional] 
**signing_order** | **object** |  | [optional] 
**delivery_methods** | **object** |  | [optional] 
**redirect** | **object** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from pandadoc_client.models.document_fields_field_assigned_to import DocumentFieldsFieldAssignedTo

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentFieldsFieldAssignedTo from a JSON string
document_fields_field_assigned_to_instance = DocumentFieldsFieldAssignedTo.from_json(json)
# print the JSON string representation of the object
print(DocumentFieldsFieldAssignedTo.to_json())

# convert the object into a dict
document_fields_field_assigned_to_dict = document_fields_field_assigned_to_instance.to_dict()
# create an instance of DocumentFieldsFieldAssignedTo from a dict
document_fields_field_assigned_to_from_dict = DocumentFieldsFieldAssignedTo.from_dict(document_fields_field_assigned_to_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


