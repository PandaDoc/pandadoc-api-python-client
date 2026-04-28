# ProductCatalogCustomCatalogItemInBundle


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**image_url** | **str** |  | [optional] 
**images** | [**List[ProductCatalogSearchCatalogItemResponseImagesInner]**](ProductCatalogSearchCatalogItemResponseImagesInner.md) |  | [optional] 
**price** | **float** |  | [optional] 
**currency** | **str** |  | [optional] 

## Example

```python
from pandadoc_client.models.product_catalog_custom_catalog_item_in_bundle import ProductCatalogCustomCatalogItemInBundle

# TODO update the JSON string below
json = "{}"
# create an instance of ProductCatalogCustomCatalogItemInBundle from a JSON string
product_catalog_custom_catalog_item_in_bundle_instance = ProductCatalogCustomCatalogItemInBundle.from_json(json)
# print the JSON string representation of the object
print(ProductCatalogCustomCatalogItemInBundle.to_json())

# convert the object into a dict
product_catalog_custom_catalog_item_in_bundle_dict = product_catalog_custom_catalog_item_in_bundle_instance.to_dict()
# create an instance of ProductCatalogCustomCatalogItemInBundle from a dict
product_catalog_custom_catalog_item_in_bundle_from_dict = ProductCatalogCustomCatalogItemInBundle.from_dict(product_catalog_custom_catalog_item_in_bundle_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


