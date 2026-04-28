# TemplatesFolderCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name the folder for Templates you are creating. | 
**parent_uuid** | **str** | ID of the parent folder. To create a new folder in the root folder, remove this parameter in the request. | [optional] 

## Example

```python
from pandadoc_client.models.templates_folder_create_request import TemplatesFolderCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TemplatesFolderCreateRequest from a JSON string
templates_folder_create_request_instance = TemplatesFolderCreateRequest.from_json(json)
# print the JSON string representation of the object
print(TemplatesFolderCreateRequest.to_json())

# convert the object into a dict
templates_folder_create_request_dict = templates_folder_create_request_instance.to_dict()
# create an instance of TemplatesFolderCreateRequest from a dict
templates_folder_create_request_from_dict = TemplatesFolderCreateRequest.from_dict(templates_folder_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


