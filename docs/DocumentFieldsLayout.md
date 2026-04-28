# DocumentFieldsLayout


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **int** |  | 
**position** | [**DocumentFieldsLayoutPosition**](DocumentFieldsLayoutPosition.md) |  | 
**style** | [**DocumentFieldsLayoutStyle**](DocumentFieldsLayoutStyle.md) |  | 

## Example

```python
from pandadoc_client.models.document_fields_layout import DocumentFieldsLayout

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentFieldsLayout from a JSON string
document_fields_layout_instance = DocumentFieldsLayout.from_json(json)
# print the JSON string representation of the object
print(DocumentFieldsLayout.to_json())

# convert the object into a dict
document_fields_layout_dict = document_fields_layout_instance.to_dict()
# create an instance of DocumentFieldsLayout from a dict
document_fields_layout_from_dict = DocumentFieldsLayout.from_dict(document_fields_layout_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


