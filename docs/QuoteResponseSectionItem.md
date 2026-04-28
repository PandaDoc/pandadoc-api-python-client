# QuoteResponseSectionItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**sku** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**qty** | **str** |  | [optional] 
**price** | **str** |  | [optional] 
**cost** | **str** |  | [optional] 
**billing_frequency** | **str** |  | [optional] 
**contract_term** | **str** |  | [optional] 
**pricing_method** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**reference_type** | **str** |  | [optional] 
**options** | [**QuoteResponseSectionItemOptions**](QuoteResponseSectionItemOptions.md) |  | [optional] 
**custom_columns** | **Dict[str, str]** |  | [optional] 
**external_columns** | **Dict[str, str]** |  | [optional] 
**discounts** | [**Dict[str, QuoteResponseSummaryDiscountsValue]**](QuoteResponseSummaryDiscountsValue.md) |  | [optional] 
**taxes** | [**Dict[str, QuoteResponseSummaryDiscountsValue]**](QuoteResponseSummaryDiscountsValue.md) |  | [optional] 
**fees** | [**Dict[str, QuoteResponseSummaryDiscountsValue]**](QuoteResponseSummaryDiscountsValue.md) |  | [optional] 
**multipliers** | **Dict[str, str]** |  | [optional] 
**total** | **str** |  | [optional] 
**overall_total** | **str** |  | [optional] 

## Example

```python
from pandadoc_client.models.quote_response_section_item import QuoteResponseSectionItem

# TODO update the JSON string below
json = "{}"
# create an instance of QuoteResponseSectionItem from a JSON string
quote_response_section_item_instance = QuoteResponseSectionItem.from_json(json)
# print the JSON string representation of the object
print(QuoteResponseSectionItem.to_json())

# convert the object into a dict
quote_response_section_item_dict = quote_response_section_item_instance.to_dict()
# create an instance of QuoteResponseSectionItem from a dict
quote_response_section_item_from_dict = QuoteResponseSectionItem.from_dict(quote_response_section_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


