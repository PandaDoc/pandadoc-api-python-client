# QuoteResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**currency** | **str** |  | [optional] 
**total** | **str** |  | [optional] 
**summary** | [**QuoteResponseSummary**](QuoteResponseSummary.md) |  | [optional] 
**sections** | [**List[QuoteResponseSectionsInner]**](QuoteResponseSectionsInner.md) |  | [optional] 
**merge_rules** | [**List[QuoteResponseMergeRulesInner]**](QuoteResponseMergeRulesInner.md) |  | [optional] 
**settings** | [**QuoteResponseSettings**](QuoteResponseSettings.md) |  | [optional] 

## Example

```python
from pandadoc_client.models.quote_response import QuoteResponse

# TODO update the JSON string below
json = "{}"
# create an instance of QuoteResponse from a JSON string
quote_response_instance = QuoteResponse.from_json(json)
# print the JSON string representation of the object
print(QuoteResponse.to_json())

# convert the object into a dict
quote_response_dict = quote_response_instance.to_dict()
# create an instance of QuoteResponse from a dict
quote_response_from_dict = QuoteResponse.from_dict(quote_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


