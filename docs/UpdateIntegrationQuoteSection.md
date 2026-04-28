# UpdateIntegrationQuoteSection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Section ID to update. Invalid (or missing) ID causes creating a new section. | [optional] 
**name** | **str** | Name of the quotes section. If you create a section without providing a value, it will have the default value. | [optional] [default to 'Section name']
**summary** | [**QuoteUpdateRequestSummary**](QuoteUpdateRequestSummary.md) |  | [optional] 
**items** | [**List[UpdateIntegrationQuoteSectionItem]**](UpdateIntegrationQuoteSectionItem.md) | Section items - this property overrides the existing items in the order specified. If you want to change only one item, you must still pass other items IDs. Otherwise these items will be removed. | [optional] 
**settings** | [**UpdateIntegrationQuoteSectionSettings**](UpdateIntegrationQuoteSectionSettings.md) |  | [optional] 

## Example

```python
from pandadoc_client.models.update_integration_quote_section import UpdateIntegrationQuoteSection

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateIntegrationQuoteSection from a JSON string
update_integration_quote_section_instance = UpdateIntegrationQuoteSection.from_json(json)
# print the JSON string representation of the object
print(UpdateIntegrationQuoteSection.to_json())

# convert the object into a dict
update_integration_quote_section_dict = update_integration_quote_section_instance.to_dict()
# create an instance of UpdateIntegrationQuoteSection from a dict
update_integration_quote_section_from_dict = UpdateIntegrationQuoteSection.from_dict(update_integration_quote_section_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


