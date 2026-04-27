# TemplatesFolderRenameResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**date_created** | **str** |  | [optional] 

## Example

```python
from pandadoc_client.models.templates_folder_rename_response import TemplatesFolderRenameResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TemplatesFolderRenameResponse from a JSON string
templates_folder_rename_response_instance = TemplatesFolderRenameResponse.from_json(json)
# print the JSON string representation of the object
print(TemplatesFolderRenameResponse.to_json())

# convert the object into a dict
templates_folder_rename_response_dict = templates_folder_rename_response_instance.to_dict()
# create an instance of TemplatesFolderRenameResponse from a dict
templates_folder_rename_response_from_dict = TemplatesFolderRenameResponse.from_dict(templates_folder_rename_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


