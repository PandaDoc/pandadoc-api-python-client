# QuoteUpdateRequestSummaryDiscountsValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**QuoteUpdateRequestDiscountTypeEnum**](QuoteUpdateRequestDiscountTypeEnum.md) |  | [optional] 
**value** | **float** |  | [optional] 

## Example

```python
from pandadoc_client.models.quote_update_request_summary_discounts_value import QuoteUpdateRequestSummaryDiscountsValue

# TODO update the JSON string below
json = "{}"
# create an instance of QuoteUpdateRequestSummaryDiscountsValue from a JSON string
quote_update_request_summary_discounts_value_instance = QuoteUpdateRequestSummaryDiscountsValue.from_json(json)
# print the JSON string representation of the object
print(QuoteUpdateRequestSummaryDiscountsValue.to_json())

# convert the object into a dict
quote_update_request_summary_discounts_value_dict = quote_update_request_summary_discounts_value_instance.to_dict()
# create an instance of QuoteUpdateRequestSummaryDiscountsValue from a dict
quote_update_request_summary_discounts_value_from_dict = QuoteUpdateRequestSummaryDiscountsValue.from_dict(quote_update_request_summary_discounts_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


