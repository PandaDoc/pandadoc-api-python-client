# QuoteUpdateRequestSummary

Summary settings containing adjustments (discounts, fees, taxes) and custom columns that apply to the entire quote / section total.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**custom_columns** | **Dict[str, str]** |  | [optional] 
**discounts** | [**Dict[str, QuoteUpdateRequestSummaryDiscountsValue]**](QuoteUpdateRequestSummaryDiscountsValue.md) | Summary level discounts. | [optional] 
**fees** | [**Dict[str, QuoteUpdateRequestSummaryDiscountsValue]**](QuoteUpdateRequestSummaryDiscountsValue.md) | Summary level fees. | [optional] 
**taxes** | [**Dict[str, QuoteUpdateRequestSummaryDiscountsValue]**](QuoteUpdateRequestSummaryDiscountsValue.md) | Summary level taxes. | [optional] 

## Example

```python
from pandadoc_client.models.quote_update_request_summary import QuoteUpdateRequestSummary

# TODO update the JSON string below
json = "{}"
# create an instance of QuoteUpdateRequestSummary from a JSON string
quote_update_request_summary_instance = QuoteUpdateRequestSummary.from_json(json)
# print the JSON string representation of the object
print(QuoteUpdateRequestSummary.to_json())

# convert the object into a dict
quote_update_request_summary_dict = quote_update_request_summary_instance.to_dict()
# create an instance of QuoteUpdateRequestSummary from a dict
quote_update_request_summary_from_dict = QuoteUpdateRequestSummary.from_dict(quote_update_request_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


