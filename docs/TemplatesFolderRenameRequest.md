# TemplatesFolderRenameRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Provide a new name for the folder. | 

## Example

```python
from pandadoc_client.models.templates_folder_rename_request import TemplatesFolderRenameRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TemplatesFolderRenameRequest from a JSON string
templates_folder_rename_request_instance = TemplatesFolderRenameRequest.from_json(json)
# print the JSON string representation of the object
print(TemplatesFolderRenameRequest.to_json())

# convert the object into a dict
templates_folder_rename_request_dict = templates_folder_rename_request_instance.to_dict()
# create an instance of TemplatesFolderRenameRequest from a dict
templates_folder_rename_request_from_dict = TemplatesFolderRenameRequest.from_dict(templates_folder_rename_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


