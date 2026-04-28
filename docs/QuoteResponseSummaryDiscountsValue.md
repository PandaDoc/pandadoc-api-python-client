# QuoteResponseSummaryDiscountsValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**value** | **str** |  | [optional] 

## Example

```python
from pandadoc_client.models.quote_response_summary_discounts_value import QuoteResponseSummaryDiscountsValue

# TODO update the JSON string below
json = "{}"
# create an instance of QuoteResponseSummaryDiscountsValue from a JSON string
quote_response_summary_discounts_value_instance = QuoteResponseSummaryDiscountsValue.from_json(json)
# print the JSON string representation of the object
print(QuoteResponseSummaryDiscountsValue.to_json())

# convert the object into a dict
quote_response_summary_discounts_value_dict = quote_response_summary_discounts_value_instance.to_dict()
# create an instance of QuoteResponseSummaryDiscountsValue from a dict
quote_response_summary_discounts_value_from_dict = QuoteResponseSummaryDiscountsValue.from_dict(quote_response_summary_discounts_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


