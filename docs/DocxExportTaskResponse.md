# DocxExportTaskResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Export task id. | 
**document_id** | **str** | Document id. | 
**status** | [**DocumentDocxExportStatusEnum**](DocumentDocxExportStatusEnum.md) |  | 
**docx_items** | [**List[DocxExportTaskResponseAllOfDocxItems]**](DocxExportTaskResponseAllOfDocxItems.md) | DOCX files result URLs with their names. | [optional] 

## Example

```python
from pandadoc_client.models.docx_export_task_response import DocxExportTaskResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DocxExportTaskResponse from a JSON string
docx_export_task_response_instance = DocxExportTaskResponse.from_json(json)
# print the JSON string representation of the object
print(DocxExportTaskResponse.to_json())

# convert the object into a dict
docx_export_task_response_dict = docx_export_task_response_instance.to_dict()
# create an instance of DocxExportTaskResponse from a dict
docx_export_task_response_from_dict = DocxExportTaskResponse.from_dict(docx_export_task_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


