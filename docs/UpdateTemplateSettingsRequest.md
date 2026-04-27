# UpdateTemplateSettingsRequest

Template settings update request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**language** | [**DocumentLanguageEnum**](DocumentLanguageEnum.md) |  | [optional] 

## Example

```python
from pandadoc_client.models.update_template_settings_request import UpdateTemplateSettingsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateTemplateSettingsRequest from a JSON string
update_template_settings_request_instance = UpdateTemplateSettingsRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateTemplateSettingsRequest.to_json())

# convert the object into a dict
update_template_settings_request_dict = update_template_settings_request_instance.to_dict()
# create an instance of UpdateTemplateSettingsRequest from a dict
update_template_settings_request_from_dict = UpdateTemplateSettingsRequest.from_dict(update_template_settings_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


