# UpdateIntegrationQuoteSection


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Section ID to update. Invalid (or missing) ID causes creating a new section. | [optional] 
**name** | **str, none_type** | Name of the quotes section. If you create a section without providing a value, it will have the default value. | [optional]  if omitted the server will use the default value of "Section name"
**items** | [**[UpdateIntegrationQuoteSectionItem]**](UpdateIntegrationQuoteSectionItem.md) | Section items - this property overrides the existing items in the order specified. If you want to change only one item, you must still pass other items IDs. Otherwise these items will be removed. | [optional] 
**settings** | [**QuoteUpdateRequestSettings**](QuoteUpdateRequestSettings.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


