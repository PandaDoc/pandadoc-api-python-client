# ProductCatalogItemResponseBundleItemsInnerItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**sku** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**image_url** | **str** |  | [optional] 
**images** | [**List[ProductCatalogSearchCatalogItemResponseImagesInner]**](ProductCatalogSearchCatalogItemResponseImagesInner.md) |  | [optional] 
**price** | **float** |  | [optional] 
**currency** | **str** |  | [optional] 

## Example

```python
from pandadoc_client.models.product_catalog_item_response_bundle_items_inner_item import ProductCatalogItemResponseBundleItemsInnerItem

# TODO update the JSON string below
json = "{}"
# create an instance of ProductCatalogItemResponseBundleItemsInnerItem from a JSON string
product_catalog_item_response_bundle_items_inner_item_instance = ProductCatalogItemResponseBundleItemsInnerItem.from_json(json)
# print the JSON string representation of the object
print(ProductCatalogItemResponseBundleItemsInnerItem.to_json())

# convert the object into a dict
product_catalog_item_response_bundle_items_inner_item_dict = product_catalog_item_response_bundle_items_inner_item_instance.to_dict()
# create an instance of ProductCatalogItemResponseBundleItemsInnerItem from a dict
product_catalog_item_response_bundle_items_inner_item_from_dict = ProductCatalogItemResponseBundleItemsInnerItem.from_dict(product_catalog_item_response_bundle_items_inner_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


