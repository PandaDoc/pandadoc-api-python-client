# ListCatalogItemsSearchResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[ProductCatalogSearchCatalogItemResponse]**](ProductCatalogSearchCatalogItemResponse.md) |  | [optional] 
**has_more_items** | **bool** |  | [optional] 
**total** | **float** |  | [optional] 

## Example

```python
from pandadoc_client.models.list_catalog_items_search_response import ListCatalogItemsSearchResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListCatalogItemsSearchResponse from a JSON string
list_catalog_items_search_response_instance = ListCatalogItemsSearchResponse.from_json(json)
# print the JSON string representation of the object
print(ListCatalogItemsSearchResponse.to_json())

# convert the object into a dict
list_catalog_items_search_response_dict = list_catalog_items_search_response_instance.to_dict()
# create an instance of ListCatalogItemsSearchResponse from a dict
list_catalog_items_search_response_from_dict = ListCatalogItemsSearchResponse.from_dict(list_catalog_items_search_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


