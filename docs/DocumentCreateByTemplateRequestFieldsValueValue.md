# DocumentCreateByTemplateRequestFieldsValueValue

The value to pre-fill the field with. The type of the value depends on the field type in the template. For example, for a checkbox field, you can pass a boolean value, and for a date field, you can pass a date string in RFC 3339 format (e.g., 2019-12-31T00:00:00.000Z). 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from pandadoc_client.models.document_create_by_template_request_fields_value_value import DocumentCreateByTemplateRequestFieldsValueValue

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentCreateByTemplateRequestFieldsValueValue from a JSON string
document_create_by_template_request_fields_value_value_instance = DocumentCreateByTemplateRequestFieldsValueValue.from_json(json)
# print the JSON string representation of the object
print(DocumentCreateByTemplateRequestFieldsValueValue.to_json())

# convert the object into a dict
document_create_by_template_request_fields_value_value_dict = document_create_by_template_request_fields_value_value_instance.to_dict()
# create an instance of DocumentCreateByTemplateRequestFieldsValueValue from a dict
document_create_by_template_request_fields_value_value_from_dict = DocumentCreateByTemplateRequestFieldsValueValue.from_dict(document_create_by_template_request_fields_value_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


