# QuoteUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency** | **str** | Currency code (ISO 4217) | [optional] 
**summary** | [**QuoteUpdateRequestSummary**](QuoteUpdateRequestSummary.md) |  | [optional] 
**sections** | [**List[UpdateIntegrationQuoteSection]**](UpdateIntegrationQuoteSection.md) | Quote sections - this property overrides existing sections in the specified order. If you want to change only one section, you must still pass other sections IDs. Otherwise these sections will be removed. | [optional] 
**settings** | [**QuoteUpdateRequestSettings**](QuoteUpdateRequestSettings.md) |  | [optional] 

## Example

```python
from pandadoc_client.models.quote_update_request import QuoteUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of QuoteUpdateRequest from a JSON string
quote_update_request_instance = QuoteUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(QuoteUpdateRequest.to_json())

# convert the object into a dict
quote_update_request_dict = quote_update_request_instance.to_dict()
# create an instance of QuoteUpdateRequest from a dict
quote_update_request_from_dict = QuoteUpdateRequest.from_dict(quote_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


