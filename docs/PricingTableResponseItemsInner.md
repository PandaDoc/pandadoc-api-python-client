# PricingTableResponseItemsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**sku** | **str** |  | [optional] 
**qty** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**cost** | **str** |  | [optional] 
**price** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**custom_fields** | **object** |  | [optional] 
**custom_columns** | **object** |  | [optional] 
**discount** | [**PricingTableResponseItemsInnerDiscount**](PricingTableResponseItemsInnerDiscount.md) |  | [optional] 
**tax_first** | [**PricingTableResponseItemsInnerDiscount**](PricingTableResponseItemsInnerDiscount.md) |  | [optional] 
**tax_second** | [**PricingTableResponseItemsInnerDiscount**](PricingTableResponseItemsInnerDiscount.md) |  | [optional] 
**subtotal** | **str** |  | [optional] 
**options** | [**PricingTableResponseItemsInnerOptions**](PricingTableResponseItemsInnerOptions.md) |  | [optional] 
**sale_price** | **str** |  | [optional] 
**taxes** | **object** |  | [optional] 
**discounts** | **object** |  | [optional] 
**fees** | **object** |  | [optional] 
**merged_data** | **object** | Contains all fields in a flat structure with external field names defined in the template. | [optional] 

## Example

```python
from pandadoc_client.models.pricing_table_response_items_inner import PricingTableResponseItemsInner

# TODO update the JSON string below
json = "{}"
# create an instance of PricingTableResponseItemsInner from a JSON string
pricing_table_response_items_inner_instance = PricingTableResponseItemsInner.from_json(json)
# print the JSON string representation of the object
print(PricingTableResponseItemsInner.to_json())

# convert the object into a dict
pricing_table_response_items_inner_dict = pricing_table_response_items_inner_instance.to_dict()
# create an instance of PricingTableResponseItemsInner from a dict
pricing_table_response_items_inner_from_dict = PricingTableResponseItemsInner.from_dict(pricing_table_response_items_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


