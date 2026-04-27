# TemplatesFolderListResponseResultsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**date_created** | **str** |  | [optional] 
**has_folders** | **bool** |  | [optional] 
**has_items** | **bool** |  | [optional] 

## Example

```python
from pandadoc_client.models.templates_folder_list_response_results_inner import TemplatesFolderListResponseResultsInner

# TODO update the JSON string below
json = "{}"
# create an instance of TemplatesFolderListResponseResultsInner from a JSON string
templates_folder_list_response_results_inner_instance = TemplatesFolderListResponseResultsInner.from_json(json)
# print the JSON string representation of the object
print(TemplatesFolderListResponseResultsInner.to_json())

# convert the object into a dict
templates_folder_list_response_results_inner_dict = templates_folder_list_response_results_inner_instance.to_dict()
# create an instance of TemplatesFolderListResponseResultsInner from a dict
templates_folder_list_response_results_inner_from_dict = TemplatesFolderListResponseResultsInner.from_dict(templates_folder_list_response_results_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


