# QuoteUpdateRequestSettings

Quote settings. Denotes whether a quote is optional or selected, and selection type inside the section - single, multiple, or custom.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**selection_type** | [**QuoteUpdateRequestSettingsSelectionTypeTypeEnum**](QuoteUpdateRequestSettingsSelectionTypeTypeEnum.md) |  | [optional] 

## Example

```python
from pandadoc_client.models.quote_update_request_settings import QuoteUpdateRequestSettings

# TODO update the JSON string below
json = "{}"
# create an instance of QuoteUpdateRequestSettings from a JSON string
quote_update_request_settings_instance = QuoteUpdateRequestSettings.from_json(json)
# print the JSON string representation of the object
print(QuoteUpdateRequestSettings.to_json())

# convert the object into a dict
quote_update_request_settings_dict = quote_update_request_settings_instance.to_dict()
# create an instance of QuoteUpdateRequestSettings from a dict
quote_update_request_settings_from_dict = QuoteUpdateRequestSettings.from_dict(quote_update_request_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


