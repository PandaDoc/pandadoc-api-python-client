# DocxExportTaskResponseAllOfDocxItems

List of download links and section item titles of the document.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**section_title** | **str** | Document Section Item title. | [optional] 
**url** | **str** | The url for downloading the DOCX file. | [optional] 

## Example

```python
from pandadoc_client.models.docx_export_task_response_all_of_docx_items import DocxExportTaskResponseAllOfDocxItems

# TODO update the JSON string below
json = "{}"
# create an instance of DocxExportTaskResponseAllOfDocxItems from a JSON string
docx_export_task_response_all_of_docx_items_instance = DocxExportTaskResponseAllOfDocxItems.from_json(json)
# print the JSON string representation of the object
print(DocxExportTaskResponseAllOfDocxItems.to_json())

# convert the object into a dict
docx_export_task_response_all_of_docx_items_dict = docx_export_task_response_all_of_docx_items_instance.to_dict()
# create an instance of DocxExportTaskResponseAllOfDocxItems from a dict
docx_export_task_response_all_of_docx_items_from_dict = DocxExportTaskResponseAllOfDocxItems.from_dict(docx_export_task_response_all_of_docx_items_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


