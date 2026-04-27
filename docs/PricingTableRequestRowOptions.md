# PricingTableRequestRowOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**qty_editable** | **bool** |  | [optional] 
**optional_selected** | **bool** |  | [optional] 
**optional** | **bool** |  | [optional] 

## Example

```python
from pandadoc_client.models.pricing_table_request_row_options import PricingTableRequestRowOptions

# TODO update the JSON string below
json = "{}"
# create an instance of PricingTableRequestRowOptions from a JSON string
pricing_table_request_row_options_instance = PricingTableRequestRowOptions.from_json(json)
# print the JSON string representation of the object
print(PricingTableRequestRowOptions.to_json())

# convert the object into a dict
pricing_table_request_row_options_dict = pricing_table_request_row_options_instance.to_dict()
# create an instance of PricingTableRequestRowOptions from a dict
pricing_table_request_row_options_from_dict = PricingTableRequestRowOptions.from_dict(pricing_table_request_row_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


