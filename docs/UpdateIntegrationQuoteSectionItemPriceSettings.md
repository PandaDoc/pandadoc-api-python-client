# UpdateIntegrationQuoteSectionItemPriceSettings

Price settings if the price is not flat rate. If it is null, the price is flat rate.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_value** | **float** | Base value for volume discount pricing. If set, tiers are treated like percentage of discount on this value. If not set, tiers are treated like a flat value discount of chosen currency. | 
**tiers** | [**List[UpdateIntegrationQuoteSectionItemPriceSettingsTiersInner]**](UpdateIntegrationQuoteSectionItemPriceSettingsTiersInner.md) |  | 

## Example

```python
from pandadoc_client.models.update_integration_quote_section_item_price_settings import UpdateIntegrationQuoteSectionItemPriceSettings

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateIntegrationQuoteSectionItemPriceSettings from a JSON string
update_integration_quote_section_item_price_settings_instance = UpdateIntegrationQuoteSectionItemPriceSettings.from_json(json)
# print the JSON string representation of the object
print(UpdateIntegrationQuoteSectionItemPriceSettings.to_json())

# convert the object into a dict
update_integration_quote_section_item_price_settings_dict = update_integration_quote_section_item_price_settings_instance.to_dict()
# create an instance of UpdateIntegrationQuoteSectionItemPriceSettings from a dict
update_integration_quote_section_item_price_settings_from_dict = UpdateIntegrationQuoteSectionItemPriceSettings.from_dict(update_integration_quote_section_item_price_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


