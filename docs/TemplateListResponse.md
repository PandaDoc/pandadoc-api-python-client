# TemplateListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[TemplateCreateResponse]**](TemplateCreateResponse.md) |  | [optional] 

## Example

```python
from pandadoc_client.models.template_list_response import TemplateListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TemplateListResponse from a JSON string
template_list_response_instance = TemplateListResponse.from_json(json)
# print the JSON string representation of the object
print(TemplateListResponse.to_json())

# convert the object into a dict
template_list_response_dict = template_list_response_instance.to_dict()
# create an instance of TemplateListResponse from a dict
template_list_response_from_dict = TemplateListResponse.from_dict(template_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


