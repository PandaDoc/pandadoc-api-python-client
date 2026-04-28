# DocumentFieldsLayoutPosition


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**offset_x** | **float** |  | 
**offset_y** | **float** |  | 
**anchor_point** | [**DocumentFieldAnchorPointEnum**](DocumentFieldAnchorPointEnum.md) |  | 

## Example

```python
from pandadoc_client.models.document_fields_layout_position import DocumentFieldsLayoutPosition

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentFieldsLayoutPosition from a JSON string
document_fields_layout_position_instance = DocumentFieldsLayoutPosition.from_json(json)
# print the JSON string representation of the object
print(DocumentFieldsLayoutPosition.to_json())

# convert the object into a dict
document_fields_layout_position_dict = document_fields_layout_position_instance.to_dict()
# create an instance of DocumentFieldsLayoutPosition from a dict
document_fields_layout_position_from_dict = DocumentFieldsLayoutPosition.from_dict(document_fields_layout_position_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


