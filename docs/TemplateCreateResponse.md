# TemplateCreateResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**date_created** | **datetime** |  | [optional] 
**date_modified** | **datetime** |  | [optional] 
**version** | **str** |  | [optional] 
**content_date_modified** | **datetime** |  | [optional] 

## Example

```python
from pandadoc_client.models.template_create_response import TemplateCreateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TemplateCreateResponse from a JSON string
template_create_response_instance = TemplateCreateResponse.from_json(json)
# print the JSON string representation of the object
print(TemplateCreateResponse.to_json())

# convert the object into a dict
template_create_response_dict = template_create_response_instance.to_dict()
# create an instance of TemplateCreateResponse from a dict
template_create_response_from_dict = TemplateCreateResponse.from_dict(template_create_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


