# ProductCatalogCatalogCustomBundleItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**image_url** | **str** |  | [optional] 
**images** | [**List[ProductCatalogSearchCatalogItemResponseImagesInner]**](ProductCatalogSearchCatalogItemResponseImagesInner.md) |  | [optional] 
**price_configuration** | [**ProductCatalogItemPriceConfiguration**](ProductCatalogItemPriceConfiguration.md) |  | [optional] 

## Example

```python
from pandadoc_client.models.product_catalog_catalog_custom_bundle_item import ProductCatalogCatalogCustomBundleItem

# TODO update the JSON string below
json = "{}"
# create an instance of ProductCatalogCatalogCustomBundleItem from a JSON string
product_catalog_catalog_custom_bundle_item_instance = ProductCatalogCatalogCustomBundleItem.from_json(json)
# print the JSON string representation of the object
print(ProductCatalogCatalogCustomBundleItem.to_json())

# convert the object into a dict
product_catalog_catalog_custom_bundle_item_dict = product_catalog_catalog_custom_bundle_item_instance.to_dict()
# create an instance of ProductCatalogCatalogCustomBundleItem from a dict
product_catalog_catalog_custom_bundle_item_from_dict = ProductCatalogCatalogCustomBundleItem.from_dict(product_catalog_catalog_custom_bundle_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


