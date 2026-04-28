# PricingResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tables** | [**List[PricingTableResponse]**](PricingTableResponse.md) |  | [optional] 
**quotes** | [**List[QuoteResponse]**](QuoteResponse.md) |  | [optional] 
**total** | **str** |  | [optional] 

## Example

```python
from pandadoc_client.models.pricing_response import PricingResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PricingResponse from a JSON string
pricing_response_instance = PricingResponse.from_json(json)
# print the JSON string representation of the object
print(PricingResponse.to_json())

# convert the object into a dict
pricing_response_dict = pricing_response_instance.to_dict()
# create an instance of PricingResponse from a dict
pricing_response_from_dict = PricingResponse.from_dict(pricing_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


