# UpdateIntegrationQuoteSectionItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Item ID to update. Invalid (or missing) ID causes creating a new item. | [optional] 
**sku** | **str** | Product SKU. If you create an item without providing a value, it will have the default value. | [optional] [default to '#']
**name** | **str** | Item name. If you create an item without providing a value, it will have the default value. | [optional] [default to '']
**description** | **str** | Item description. If you create an item without providing a value, it will have the default value. | [optional] [default to '']
**qty** | **int** | Item QTY. If you create an item without providing a value, it will have the default value. | [optional] [default to 1]
**price** | **float** | Item price. If you create an item without providing a value, it will have the default value. If &#x60;price_settings&#x60; is passed, this value may change after the quote is updated. | [optional] [default to 0]
**price_settings** | [**UpdateIntegrationQuoteSectionItemPriceSettings**](UpdateIntegrationQuoteSectionItemPriceSettings.md) |  | [optional] 
**cost** | **float** | Item cost. If you create an item without providing a value, it will have the default value. | [optional] 
**billing_frequency** | [**QuoteUpdateRequestBillingFrequencyEnum**](QuoteUpdateRequestBillingFrequencyEnum.md) |  | [optional] 
**contract_term** | **int** | Contract term. Measured in units set in the &#x60;billing_frequency&#x60; parameter. | [optional] 
**reference_id** | **str** | Use this field to pass an id that references this item in external systems. | [optional] 
**options** | [**UpdateIntegrationQuoteSectionItemOptions**](UpdateIntegrationQuoteSectionItemOptions.md) |  | [optional] 
**custom_columns** | **Dict[str, str]** |  | [optional] 
**external_columns** | **Dict[str, str]** |  | [optional] 
**text_columns** | **Dict[str, str]** |  | [optional] 
**discounts** | [**Dict[str, QuoteUpdateRequestSummaryDiscountsValue]**](QuoteUpdateRequestSummaryDiscountsValue.md) | Item discounts. | [optional] 
**taxes** | [**Dict[str, QuoteUpdateRequestSummaryDiscountsValue]**](QuoteUpdateRequestSummaryDiscountsValue.md) | Item taxes. | [optional] 
**fees** | [**Dict[str, QuoteUpdateRequestSummaryDiscountsValue]**](QuoteUpdateRequestSummaryDiscountsValue.md) | Item fees. | [optional] 
**multipliers** | **Dict[str, float]** | Item multipliers. | [optional] 

## Example

```python
from pandadoc_client.models.update_integration_quote_section_item import UpdateIntegrationQuoteSectionItem

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateIntegrationQuoteSectionItem from a JSON string
update_integration_quote_section_item_instance = UpdateIntegrationQuoteSectionItem.from_json(json)
# print the JSON string representation of the object
print(UpdateIntegrationQuoteSectionItem.to_json())

# convert the object into a dict
update_integration_quote_section_item_dict = update_integration_quote_section_item_instance.to_dict()
# create an instance of UpdateIntegrationQuoteSectionItem from a dict
update_integration_quote_section_item_from_dict = UpdateIntegrationQuoteSectionItem.from_dict(update_integration_quote_section_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


