# DocumentUpdateRequestFieldValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**DocumentCreateByTemplateRequestFieldsValueValue**](DocumentCreateByTemplateRequestFieldsValueValue.md) |  | 

## Example

```python
from pandadoc_client.models.document_update_request_field_value import DocumentUpdateRequestFieldValue

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentUpdateRequestFieldValue from a JSON string
document_update_request_field_value_instance = DocumentUpdateRequestFieldValue.from_json(json)
# print the JSON string representation of the object
print(DocumentUpdateRequestFieldValue.to_json())

# convert the object into a dict
document_update_request_field_value_dict = document_update_request_field_value_instance.to_dict()
# create an instance of DocumentUpdateRequestFieldValue from a dict
document_update_request_field_value_from_dict = DocumentUpdateRequestFieldValue.from_dict(document_update_request_field_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


