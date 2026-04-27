# DocumentFieldsField


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**value** | **object** |  | [optional] 
**field_id** | **str** |  | [optional] 
**type** | [**FieldTypeEnum**](FieldTypeEnum.md) |  | [optional] 
**placeholder** | **str** |  | [optional] 
**assigned_to** | [**DocumentFieldsFieldAssignedTo**](DocumentFieldsFieldAssignedTo.md) |  | [optional] 
**layout** | [**DocumentFieldsLayout**](DocumentFieldsLayout.md) |  | [optional] 
**section_uuid** | **str** |  | [optional] 

## Example

```python
from pandadoc_client.models.document_fields_field import DocumentFieldsField

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentFieldsField from a JSON string
document_fields_field_instance = DocumentFieldsField.from_json(json)
# print the JSON string representation of the object
print(DocumentFieldsField.to_json())

# convert the object into a dict
document_fields_field_dict = document_fields_field_instance.to_dict()
# create an instance of DocumentFieldsField from a dict
document_fields_field_from_dict = DocumentFieldsField.from_dict(document_fields_field_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


