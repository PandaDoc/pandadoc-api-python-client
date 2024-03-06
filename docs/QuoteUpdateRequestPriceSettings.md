# QuoteUpdateRequestPriceSettings

Price settings if the price is not flat rate. If it is null, the price is flat rate.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_value** | **float, none_type** | Base value for volume discount pricing. If set, tiers are treated like percentage of discount on this value. If not set, tiers are treated like a flat value discount of chosen currency. | 
**tiers** | [**[QuoteUpdateRequestPriceSettingsTiers]**](QuoteUpdateRequestPriceSettingsTiers.md) |  | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


