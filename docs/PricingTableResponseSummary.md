# PricingTableResponseSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subtotal** | **str** |  | [optional] 
**total** | **str** |  | [optional] 
**discount** | **str** |  | [optional] 
**tax** | **str** |  | [optional] 
**fee** | **str** |  | [optional] 

## Example

```python
from pandadoc_client.models.pricing_table_response_summary import PricingTableResponseSummary

# TODO update the JSON string below
json = "{}"
# create an instance of PricingTableResponseSummary from a JSON string
pricing_table_response_summary_instance = PricingTableResponseSummary.from_json(json)
# print the JSON string representation of the object
print(PricingTableResponseSummary.to_json())

# convert the object into a dict
pricing_table_response_summary_dict = pricing_table_response_summary_instance.to_dict()
# create an instance of PricingTableResponseSummary from a dict
pricing_table_response_summary_from_dict = PricingTableResponseSummary.from_dict(pricing_table_response_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


