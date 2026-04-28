# QuoteResponseSectionSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **str** |  | [optional] 
**subtotal** | **str** |  | [optional] 
**one_time_subtotal** | **str** |  | [optional] 
**recurring_subtotal** | [**List[QuoteResponseSummaryRecurringSubtotalInner]**](QuoteResponseSummaryRecurringSubtotalInner.md) |  | [optional] 
**total_qty** | **str** |  | [optional] 
**discounts** | **object** |  | [optional] 
**taxes** | **object** |  | [optional] 
**fees** | **object** |  | [optional] 
**custom_fields** | **Dict[str, str]** |  | [optional] 
**total_section_value** | **str** |  | [optional] 

## Example

```python
from pandadoc_client.models.quote_response_section_summary import QuoteResponseSectionSummary

# TODO update the JSON string below
json = "{}"
# create an instance of QuoteResponseSectionSummary from a JSON string
quote_response_section_summary_instance = QuoteResponseSectionSummary.from_json(json)
# print the JSON string representation of the object
print(QuoteResponseSectionSummary.to_json())

# convert the object into a dict
quote_response_section_summary_dict = quote_response_section_summary_instance.to_dict()
# create an instance of QuoteResponseSectionSummary from a dict
quote_response_section_summary_from_dict = QuoteResponseSectionSummary.from_dict(quote_response_section_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


