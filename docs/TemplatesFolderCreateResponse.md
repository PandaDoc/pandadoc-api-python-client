# TemplatesFolderCreateResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**date_created** | **str** |  | [optional] 

## Example

```python
from pandadoc_client.models.templates_folder_create_response import TemplatesFolderCreateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TemplatesFolderCreateResponse from a JSON string
templates_folder_create_response_instance = TemplatesFolderCreateResponse.from_json(json)
# print the JSON string representation of the object
print(TemplatesFolderCreateResponse.to_json())

# convert the object into a dict
templates_folder_create_response_dict = templates_folder_create_response_instance.to_dict()
# create an instance of TemplatesFolderCreateResponse from a dict
templates_folder_create_response_from_dict = TemplatesFolderCreateResponse.from_dict(templates_folder_create_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


