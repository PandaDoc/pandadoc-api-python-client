# PricingTableRequestSectionsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | 
**default** | **bool** |  | [optional] 
**multichoice_enabled** | **bool** |  | [optional] [default to False]
**rows** | [**List[PricingTableRequestSectionsInnerRowsInner]**](PricingTableRequestSectionsInnerRowsInner.md) |  | [optional] 

## Example

```python
from pandadoc_client.models.pricing_table_request_sections_inner import PricingTableRequestSectionsInner

# TODO update the JSON string below
json = "{}"
# create an instance of PricingTableRequestSectionsInner from a JSON string
pricing_table_request_sections_inner_instance = PricingTableRequestSectionsInner.from_json(json)
# print the JSON string representation of the object
print(PricingTableRequestSectionsInner.to_json())

# convert the object into a dict
pricing_table_request_sections_inner_dict = pricing_table_request_sections_inner_instance.to_dict()
# create an instance of PricingTableRequestSectionsInner from a dict
pricing_table_request_sections_inner_from_dict = PricingTableRequestSectionsInner.from_dict(pricing_table_request_sections_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


