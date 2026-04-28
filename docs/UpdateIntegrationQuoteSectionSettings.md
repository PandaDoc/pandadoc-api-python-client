# UpdateIntegrationQuoteSectionSettings

Section settings. Denotes whether a section is optional or selected, and selection type inside the section - single, multiple, or custom.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**optional** | **bool** |  | [optional] 
**selected** | **bool** |  | [optional] 
**selection_type** | [**QuoteUpdateRequestSettingsSelectionTypeTypeEnum**](QuoteUpdateRequestSettingsSelectionTypeTypeEnum.md) |  | [optional] 

## Example

```python
from pandadoc_client.models.update_integration_quote_section_settings import UpdateIntegrationQuoteSectionSettings

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateIntegrationQuoteSectionSettings from a JSON string
update_integration_quote_section_settings_instance = UpdateIntegrationQuoteSectionSettings.from_json(json)
# print the JSON string representation of the object
print(UpdateIntegrationQuoteSectionSettings.to_json())

# convert the object into a dict
update_integration_quote_section_settings_dict = update_integration_quote_section_settings_instance.to_dict()
# create an instance of UpdateIntegrationQuoteSectionSettings from a dict
update_integration_quote_section_settings_from_dict = UpdateIntegrationQuoteSectionSettings.from_dict(update_integration_quote_section_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


