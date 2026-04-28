# DocumentDocxExport


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Export task id. | 
**document_id** | **str** | Document id. | 
**status** | [**DocumentDocxExportStatusEnum**](DocumentDocxExportStatusEnum.md) |  | 

## Example

```python
from pandadoc_client.models.document_docx_export import DocumentDocxExport

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentDocxExport from a JSON string
document_docx_export_instance = DocumentDocxExport.from_json(json)
# print the JSON string representation of the object
print(DocumentDocxExport.to_json())

# convert the object into a dict
document_docx_export_dict = document_docx_export_instance.to_dict()
# create an instance of DocumentDocxExport from a dict
document_docx_export_from_dict = DocumentDocxExport.from_dict(document_docx_export_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


