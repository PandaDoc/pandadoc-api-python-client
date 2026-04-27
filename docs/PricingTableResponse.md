# PricingTableResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**total** | **str** |  | [optional] 
**is_included_in_total** | **bool** |  | [optional] 
**summary** | [**PricingTableResponseSummary**](PricingTableResponseSummary.md) |  | [optional] 
**items** | [**List[PricingTableResponseItemsInner]**](PricingTableResponseItemsInner.md) |  | [optional] 
**currency** | **str** |  | [optional] 

## Example

```python
from pandadoc_client.models.pricing_table_response import PricingTableResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PricingTableResponse from a JSON string
pricing_table_response_instance = PricingTableResponse.from_json(json)
# print the JSON string representation of the object
print(PricingTableResponse.to_json())

# convert the object into a dict
pricing_table_response_dict = pricing_table_response_instance.to_dict()
# create an instance of PricingTableResponse from a dict
pricing_table_response_from_dict = PricingTableResponse.from_dict(pricing_table_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


