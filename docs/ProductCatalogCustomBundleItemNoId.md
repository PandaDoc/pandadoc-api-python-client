# ProductCatalogCustomBundleItemNoId


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | [optional] 
**sku** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**image_url** | **str** |  | [optional] 
**images** | [**List[ProductCatalogSearchCatalogItemResponseImagesInner]**](ProductCatalogSearchCatalogItemResponseImagesInner.md) |  | [optional] 
**price** | **float** |  | [optional] 
**currency** | **str** |  | [optional] 

## Example

```python
from pandadoc_client.models.product_catalog_custom_bundle_item_no_id import ProductCatalogCustomBundleItemNoId

# TODO update the JSON string below
json = "{}"
# create an instance of ProductCatalogCustomBundleItemNoId from a JSON string
product_catalog_custom_bundle_item_no_id_instance = ProductCatalogCustomBundleItemNoId.from_json(json)
# print the JSON string representation of the object
print(ProductCatalogCustomBundleItemNoId.to_json())

# convert the object into a dict
product_catalog_custom_bundle_item_no_id_dict = product_catalog_custom_bundle_item_no_id_instance.to_dict()
# create an instance of ProductCatalogCustomBundleItemNoId from a dict
product_catalog_custom_bundle_item_no_id_from_dict = ProductCatalogCustomBundleItemNoId.from_dict(product_catalog_custom_bundle_item_no_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


