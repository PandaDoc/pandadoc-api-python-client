# QuoteSectionSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**optional** | **bool** |  | [optional] 
**selected** | **bool** |  | [optional] 
**selection_type** | **str** |  | [optional] 

## Example

```python
from pandadoc_client.models.quote_section_settings import QuoteSectionSettings

# TODO update the JSON string below
json = "{}"
# create an instance of QuoteSectionSettings from a JSON string
quote_section_settings_instance = QuoteSectionSettings.from_json(json)
# print the JSON string representation of the object
print(QuoteSectionSettings.to_json())

# convert the object into a dict
quote_section_settings_dict = quote_section_settings_instance.to_dict()
# create an instance of QuoteSectionSettings from a dict
quote_section_settings_from_dict = QuoteSectionSettings.from_dict(quote_section_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


