# QuoteResponseMergeRulesInnerCondition


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**field_name** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**comparison** | [**List[QuoteResponseMergeRulesInnerConditionComparisonInner]**](QuoteResponseMergeRulesInnerConditionComparisonInner.md) |  | [optional] 

## Example

```python
from pandadoc_client.models.quote_response_merge_rules_inner_condition import QuoteResponseMergeRulesInnerCondition

# TODO update the JSON string below
json = "{}"
# create an instance of QuoteResponseMergeRulesInnerCondition from a JSON string
quote_response_merge_rules_inner_condition_instance = QuoteResponseMergeRulesInnerCondition.from_json(json)
# print the JSON string representation of the object
print(QuoteResponseMergeRulesInnerCondition.to_json())

# convert the object into a dict
quote_response_merge_rules_inner_condition_dict = quote_response_merge_rules_inner_condition_instance.to_dict()
# create an instance of QuoteResponseMergeRulesInnerCondition from a dict
quote_response_merge_rules_inner_condition_from_dict = QuoteResponseMergeRulesInnerCondition.from_dict(quote_response_merge_rules_inner_condition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


