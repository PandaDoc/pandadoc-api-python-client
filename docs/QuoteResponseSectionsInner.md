# QuoteResponseSectionsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**summary** | [**QuoteResponseSectionSummary**](QuoteResponseSectionSummary.md) |  | [optional] 
**columns** | [**List[QuoteResponseSectionColumn]**](QuoteResponseSectionColumn.md) |  | [optional] 
**items** | [**List[QuoteResponseSectionItem]**](QuoteResponseSectionItem.md) |  | [optional] 
**total** | **str** |  | [optional] 
**settings** | [**QuoteSectionSettings**](QuoteSectionSettings.md) |  | [optional] 

## Example

```python
from pandadoc_client.models.quote_response_sections_inner import QuoteResponseSectionsInner

# TODO update the JSON string below
json = "{}"
# create an instance of QuoteResponseSectionsInner from a JSON string
quote_response_sections_inner_instance = QuoteResponseSectionsInner.from_json(json)
# print the JSON string representation of the object
print(QuoteResponseSectionsInner.to_json())

# convert the object into a dict
quote_response_sections_inner_dict = quote_response_sections_inner_instance.to_dict()
# create an instance of QuoteResponseSectionsInner from a dict
quote_response_sections_inner_from_dict = QuoteResponseSectionsInner.from_dict(quote_response_sections_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


