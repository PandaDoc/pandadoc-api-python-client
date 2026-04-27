# UpdateIntegrationQuoteSectionItemOptions

Denotes whether an item is selected, optional, and has editable quantity.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**selected** | **bool** |  | [optional] [default to True]
**qty_editable** | **bool** |  | [default to True]
**optional** | **bool** |  | [optional] [default to False]

## Example

```python
from pandadoc_client.models.update_integration_quote_section_item_options import UpdateIntegrationQuoteSectionItemOptions

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateIntegrationQuoteSectionItemOptions from a JSON string
update_integration_quote_section_item_options_instance = UpdateIntegrationQuoteSectionItemOptions.from_json(json)
# print the JSON string representation of the object
print(UpdateIntegrationQuoteSectionItemOptions.to_json())

# convert the object into a dict
update_integration_quote_section_item_options_dict = update_integration_quote_section_item_options_instance.to_dict()
# create an instance of UpdateIntegrationQuoteSectionItemOptions from a dict
update_integration_quote_section_item_options_from_dict = UpdateIntegrationQuoteSectionItemOptions.from_dict(update_integration_quote_section_item_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


