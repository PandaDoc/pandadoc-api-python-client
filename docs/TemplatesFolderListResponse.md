# TemplatesFolderListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[TemplatesFolderListResponseResultsInner]**](TemplatesFolderListResponseResultsInner.md) |  | [optional] 

## Example

```python
from pandadoc_client.models.templates_folder_list_response import TemplatesFolderListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TemplatesFolderListResponse from a JSON string
templates_folder_list_response_instance = TemplatesFolderListResponse.from_json(json)
# print the JSON string representation of the object
print(TemplatesFolderListResponse.to_json())

# convert the object into a dict
templates_folder_list_response_dict = templates_folder_list_response_instance.to_dict()
# create an instance of TemplatesFolderListResponse from a dict
templates_folder_list_response_from_dict = TemplatesFolderListResponse.from_dict(templates_folder_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


