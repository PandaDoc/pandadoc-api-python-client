# DocumentCreateByTemplateRequestFieldsValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**DocumentCreateByTemplateRequestFieldsValueValue**](DocumentCreateByTemplateRequestFieldsValueValue.md) |  | 
**role** | **str** | Assign this field to a recipient role. The role must be present in the &#x60;recipients&#x60; list.  | [optional] 

## Example

```python
from pandadoc_client.models.document_create_by_template_request_fields_value import DocumentCreateByTemplateRequestFieldsValue

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentCreateByTemplateRequestFieldsValue from a JSON string
document_create_by_template_request_fields_value_instance = DocumentCreateByTemplateRequestFieldsValue.from_json(json)
# print the JSON string representation of the object
print(DocumentCreateByTemplateRequestFieldsValue.to_json())

# convert the object into a dict
document_create_by_template_request_fields_value_dict = document_create_by_template_request_fields_value_instance.to_dict()
# create an instance of DocumentCreateByTemplateRequestFieldsValue from a dict
document_create_by_template_request_fields_value_from_dict = DocumentCreateByTemplateRequestFieldsValue.from_dict(document_create_by_template_request_fields_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


