# DocumentFieldsFieldCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**field_id** | **str** | Optional unique identifier. | [optional] 
**merge_field** | **str** | Use this to dynamically populate this field with data from your CRM or API. Supported field types:   * text   * checkbox   * date   * dropdown   * radio_buttons  | [optional] 
**type** | [**FieldTypeEnum**](FieldTypeEnum.md) |  | 
**placeholder** | **str** |  | [optional] 
**assigned_to** | **str** | Optional uuid of a recipient. | [optional] 
**layout** | [**DocumentFieldsLayout**](DocumentFieldsLayout.md) |  | 

## Example

```python
from pandadoc_client.models.document_fields_field_create import DocumentFieldsFieldCreate

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentFieldsFieldCreate from a JSON string
document_fields_field_create_instance = DocumentFieldsFieldCreate.from_json(json)
# print the JSON string representation of the object
print(DocumentFieldsFieldCreate.to_json())

# convert the object into a dict
document_fields_field_create_dict = document_fields_field_create_instance.to_dict()
# create an instance of DocumentFieldsFieldCreate from a dict
document_fields_field_create_from_dict = DocumentFieldsFieldCreate.from_dict(document_fields_field_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


