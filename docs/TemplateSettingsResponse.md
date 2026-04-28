# TemplateSettingsResponse

Template settings response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**language** | [**DocumentLanguageEnum**](DocumentLanguageEnum.md) |  | 

## Example

```python
from pandadoc_client.models.template_settings_response import TemplateSettingsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TemplateSettingsResponse from a JSON string
template_settings_response_instance = TemplateSettingsResponse.from_json(json)
# print the JSON string representation of the object
print(TemplateSettingsResponse.to_json())

# convert the object into a dict
template_settings_response_dict = template_settings_response_instance.to_dict()
# create an instance of TemplateSettingsResponse from a dict
template_settings_response_from_dict = TemplateSettingsResponse.from_dict(template_settings_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


