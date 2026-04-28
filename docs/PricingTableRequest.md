# PricingTableRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**data_merge** | **bool** | When set to true all field names in data rows must be passed as external names defined in the template. | [optional] 
**options** | **object** |  | [optional] 
**sections** | [**List[PricingTableRequestSectionsInner]**](PricingTableRequestSectionsInner.md) |  | [optional] 

## Example

```python
from pandadoc_client.models.pricing_table_request import PricingTableRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PricingTableRequest from a JSON string
pricing_table_request_instance = PricingTableRequest.from_json(json)
# print the JSON string representation of the object
print(PricingTableRequest.to_json())

# convert the object into a dict
pricing_table_request_dict = pricing_table_request_instance.to_dict()
# create an instance of PricingTableRequest from a dict
pricing_table_request_from_dict = PricingTableRequest.from_dict(pricing_table_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


