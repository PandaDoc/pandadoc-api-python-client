# ProductCatalogSearchCatalogItemResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**billing_cycle** | **int** |  | [optional] 
**billing_type** | **str** |  | [optional] 
**bundle_items_count** | **int** |  | [optional] 
**workspace_id** | **str** |  | [optional] 
**category_id** | **str** |  | [optional] 
**category_name** | **str** |  | [optional] 
**created_by** | **str** |  | [optional] 
**cost** | **float** |  | [optional] 
**currency** | **str** |  | [optional] 
**custom_fields** | [**List[ProductCatalogSearchCatalogItemResponseCustomFieldsInner]**](ProductCatalogSearchCatalogItemResponseCustomFieldsInner.md) |  | [optional] 
**date_created** | **datetime** |  | [optional] 
**date_modified** | **datetime** |  | [optional] 
**description** | **str** |  | [optional] 
**image_src** | **str** |  | [optional] 
**images** | [**List[ProductCatalogSearchCatalogItemResponseImagesInner]**](ProductCatalogSearchCatalogItemResponseImagesInner.md) |  | [optional] 
**max_tier_value** | **float** |  | [optional] 
**min_tier_value** | **float** |  | [optional] 
**modified_by** | **str** |  | [optional] 
**price** | **float** |  | [optional] 
**pricing_method** | **int** |  | [optional] 
**sku** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**tiers** | [**List[ProductCatalogSearchCatalogItemResponseTiersInner]**](ProductCatalogSearchCatalogItemResponseTiersInner.md) |  | [optional] 
**type** | [**ProductCatalogTypeEnum**](ProductCatalogTypeEnum.md) |  | [optional] [default to ProductCatalogTypeEnum.REGULAR]
**uuid** | **str** |  | [optional] 
**highlights** | **Dict[str, object]** |  | [optional] 

## Example

```python
from pandadoc_client.models.product_catalog_search_catalog_item_response import ProductCatalogSearchCatalogItemResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ProductCatalogSearchCatalogItemResponse from a JSON string
product_catalog_search_catalog_item_response_instance = ProductCatalogSearchCatalogItemResponse.from_json(json)
# print the JSON string representation of the object
print(ProductCatalogSearchCatalogItemResponse.to_json())

# convert the object into a dict
product_catalog_search_catalog_item_response_dict = product_catalog_search_catalog_item_response_instance.to_dict()
# create an instance of ProductCatalogSearchCatalogItemResponse from a dict
product_catalog_search_catalog_item_response_from_dict = ProductCatalogSearchCatalogItemResponse.from_dict(product_catalog_search_catalog_item_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


