# QuoteResponseSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **str** |  | [optional] 
**subtotal** | **str** |  | [optional] 
**one_time_subtotal** | **str** |  | [optional] 
**recurring_subtotal** | [**List[QuoteResponseSummaryRecurringSubtotalInner]**](QuoteResponseSummaryRecurringSubtotalInner.md) |  | [optional] 
**total_qty** | **str** |  | [optional] 
**discounts** | [**Dict[str, QuoteResponseSummaryDiscountsValue]**](QuoteResponseSummaryDiscountsValue.md) |  | [optional] 
**taxes** | **object** |  | [optional] 
**fees** | **object** |  | [optional] 
**custom_fields** | **Dict[str, str]** |  | [optional] 
**total_discount** | **str** |  | [optional] 
**total_tax** | **str** |  | [optional] 
**total_fee** | **str** |  | [optional] 
**total_savings** | **str** |  | [optional] 
**total_contract_value** | **str** |  | [optional] 

## Example

```python
from pandadoc_client.models.quote_response_summary import QuoteResponseSummary

# TODO update the JSON string below
json = "{}"
# create an instance of QuoteResponseSummary from a JSON string
quote_response_summary_instance = QuoteResponseSummary.from_json(json)
# print the JSON string representation of the object
print(QuoteResponseSummary.to_json())

# convert the object into a dict
quote_response_summary_dict = quote_response_summary_instance.to_dict()
# create an instance of QuoteResponseSummary from a dict
quote_response_summary_from_dict = QuoteResponseSummary.from_dict(quote_response_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


