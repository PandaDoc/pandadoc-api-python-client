# ContentLibraryItemResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**date_created** | **str** |  | [optional] 
**date_modified** | **str** |  | [optional] 
**content_date_modified** | **str** |  | [optional] 
**created_by** | [**ContentLibraryItemResponseCreatedBy**](ContentLibraryItemResponseCreatedBy.md) |  | [optional] 
**metadata** | **object** |  | [optional] 
**tokens** | **List[object]** |  | [optional] 
**fields** | **List[object]** |  | [optional] 
**pricing** | [**PricingResponse**](PricingResponse.md) |  | [optional] 
**tags** | **List[str]** |  | [optional] 
**roles** | **List[object]** |  | [optional] 
**version** | **str** |  | [optional] 
**content_placeholders** | **List[object]** |  | [optional] 
**tables** | [**List[DocumentDetailsResponseTablesInner]**](DocumentDetailsResponseTablesInner.md) | Document tables. | [optional] 
**images** | **List[object]** |  | [optional] 

## Example

```python
from pandadoc_client.models.content_library_item_response import ContentLibraryItemResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ContentLibraryItemResponse from a JSON string
content_library_item_response_instance = ContentLibraryItemResponse.from_json(json)
# print the JSON string representation of the object
print(ContentLibraryItemResponse.to_json())

# convert the object into a dict
content_library_item_response_dict = content_library_item_response_instance.to_dict()
# create an instance of ContentLibraryItemResponse from a dict
content_library_item_response_from_dict = ContentLibraryItemResponse.from_dict(content_library_item_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


