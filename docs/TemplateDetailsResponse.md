# TemplateDetailsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**folder_uuid** | **str** |  | [optional] 
**date_created** | **str** |  | [optional] 
**date_modified** | **str** |  | [optional] 
**content_date_modified** | **str** |  | [optional] 
**created_by** | [**ContentLibraryItemResponseCreatedBy**](ContentLibraryItemResponseCreatedBy.md) |  | [optional] 
**metadata** | **object** |  | [optional] 
**tokens** | [**List[TemplateDetailsResponseTokensInner]**](TemplateDetailsResponseTokensInner.md) |  | [optional] 
**fields** | **List[object]** |  | [optional] 
**pricing** | [**PricingResponse**](PricingResponse.md) |  | [optional] 
**tags** | **List[str]** |  | [optional] 
**roles** | [**List[TemplateDetailsResponseRolesInner]**](TemplateDetailsResponseRolesInner.md) |  | [optional] 
**version** | **str** |  | [optional] 
**content_placeholders** | [**List[TemplateDetailsResponseContentPlaceholdersInner]**](TemplateDetailsResponseContentPlaceholdersInner.md) |  | [optional] 
**tables** | [**List[DocumentDetailsResponseTablesInner]**](DocumentDetailsResponseTablesInner.md) | Document tables. | [optional] 
**images** | [**List[TemplateDetailsResponseImagesInner]**](TemplateDetailsResponseImagesInner.md) |  | [optional] 

## Example

```python
from pandadoc_client.models.template_details_response import TemplateDetailsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TemplateDetailsResponse from a JSON string
template_details_response_instance = TemplateDetailsResponse.from_json(json)
# print the JSON string representation of the object
print(TemplateDetailsResponse.to_json())

# convert the object into a dict
template_details_response_dict = template_details_response_instance.to_dict()
# create an instance of TemplateDetailsResponse from a dict
template_details_response_from_dict = TemplateDetailsResponse.from_dict(template_details_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


