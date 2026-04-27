# QuoteResponseSectionItemOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**selected** | **bool** |  | [optional] 
**qty_editable** | **bool** |  | [optional] 

## Example

```python
from pandadoc_client.models.quote_response_section_item_options import QuoteResponseSectionItemOptions

# TODO update the JSON string below
json = "{}"
# create an instance of QuoteResponseSectionItemOptions from a JSON string
quote_response_section_item_options_instance = QuoteResponseSectionItemOptions.from_json(json)
# print the JSON string representation of the object
print(QuoteResponseSectionItemOptions.to_json())

# convert the object into a dict
quote_response_section_item_options_dict = quote_response_section_item_options_instance.to_dict()
# create an instance of QuoteResponseSectionItemOptions from a dict
quote_response_section_item_options_from_dict = QuoteResponseSectionItemOptions.from_dict(quote_response_section_item_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


