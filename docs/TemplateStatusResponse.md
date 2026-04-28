# TemplateStatusResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**date_created** | **str** |  | [optional] 
**date_modified** | **str** |  | [optional] 
**version** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from pandadoc_client.models.template_status_response import TemplateStatusResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TemplateStatusResponse from a JSON string
template_status_response_instance = TemplateStatusResponse.from_json(json)
# print the JSON string representation of the object
print(TemplateStatusResponse.to_json())

# convert the object into a dict
template_status_response_dict = template_status_response_instance.to_dict()
# create an instance of TemplateStatusResponse from a dict
template_status_response_from_dict = TemplateStatusResponse.from_dict(template_status_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


