# UpdateIntegrationQuoteSectionItem


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Item ID to update. Invalid (or missing) ID causes creating a new item. | [optional] 
**sku** | **str** | Product SKU. If you create an item without providing a value, it will have the default value. | [optional]  if omitted the server will use the default value of "#"
**name** | **str** | Item name. If you create an item without providing a value, it will have the default value. | [optional]  if omitted the server will use the default value of ""
**description** | **str** | Item description. If you create an item without providing a value, it will have the default value. | [optional]  if omitted the server will use the default value of ""
**qty** | **int** | Item QTY. If you create an item without providing a value, it will have the default value. | [optional]  if omitted the server will use the default value of 1
**price** | **float** | Item price. If you create an item without providing a value, it will have the default value. If &#x60;price_settings&#x60; is passed, this value may change after the quote is updated. | [optional]  if omitted the server will use the default value of 0
**price_settings** | [**QuoteUpdateRequestPriceSettings**](QuoteUpdateRequestPriceSettings.md) |  | [optional] 
**cost** | **float** | Item cost. If you create an item without providing a value, it will have the default value. | [optional] 
**billing_frequency** | **str, none_type** |  | [optional] 
**contract_term** | **int, none_type** | Contract term. Measured in units set in the &#x60;billing_frequency&#x60; parameter. | [optional] 
**reference_id** | **str, none_type** | Use this field to pass an id that references this item in external systems. | [optional] 
**options** | [**QuoteUpdateRequestOptions**](QuoteUpdateRequestOptions.md) |  | [optional] 
**custom_columns** | **{str: (str,)}** |  | [optional] 
**discounts** | [**{str: (QuoteUpdateRequestDiscounts,)}**](QuoteUpdateRequestDiscounts.md) | Item discounts. | [optional] 
**taxes** | [**{str: (QuoteUpdateRequestDiscounts,)}**](QuoteUpdateRequestDiscounts.md) | Item taxes. | [optional] 
**fees** | [**{str: (QuoteUpdateRequestDiscounts,)}**](QuoteUpdateRequestDiscounts.md) | Item fees. | [optional] 
**multipliers** | **{str: (float,)}** | Item multipliers. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


