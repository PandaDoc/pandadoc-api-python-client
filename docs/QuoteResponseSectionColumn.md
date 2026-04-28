# QuoteResponseSectionColumn


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**header** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**merge_name** | **str** |  | [optional] 
**hidden** | **str** |  | [optional] 

## Example

```python
from pandadoc_client.models.quote_response_section_column import QuoteResponseSectionColumn

# TODO update the JSON string below
json = "{}"
# create an instance of QuoteResponseSectionColumn from a JSON string
quote_response_section_column_instance = QuoteResponseSectionColumn.from_json(json)
# print the JSON string representation of the object
print(QuoteResponseSectionColumn.to_json())

# convert the object into a dict
quote_response_section_column_dict = quote_response_section_column_instance.to_dict()
# create an instance of QuoteResponseSectionColumn from a dict
quote_response_section_column_from_dict = QuoteResponseSectionColumn.from_dict(quote_response_section_column_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


