# PricingTableResponseItemsInnerOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**optional** | **bool** |  | [optional] 
**optional_selected** | **bool** |  | [optional] 
**multichoice_enabled** | **bool** |  | [optional] 
**multichoice_selected** | **bool** |  | [optional] 

## Example

```python
from pandadoc_client.models.pricing_table_response_items_inner_options import PricingTableResponseItemsInnerOptions

# TODO update the JSON string below
json = "{}"
# create an instance of PricingTableResponseItemsInnerOptions from a JSON string
pricing_table_response_items_inner_options_instance = PricingTableResponseItemsInnerOptions.from_json(json)
# print the JSON string representation of the object
print(PricingTableResponseItemsInnerOptions.to_json())

# convert the object into a dict
pricing_table_response_items_inner_options_dict = pricing_table_response_items_inner_options_instance.to_dict()
# create an instance of PricingTableResponseItemsInnerOptions from a dict
pricing_table_response_items_inner_options_from_dict = PricingTableResponseItemsInnerOptions.from_dict(pricing_table_response_items_inner_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


