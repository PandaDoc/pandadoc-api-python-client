# ProductCatalogItemPatchRequestProductVariant


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sku** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**images** | [**List[ProductCatalogItemRequestImagesInner]**](ProductCatalogItemRequestImagesInner.md) |  | [optional] 
**custom_fields** | [**List[ProductCatalogSearchCatalogItemResponseCustomFieldsInner]**](ProductCatalogSearchCatalogItemResponseCustomFieldsInner.md) |  | [optional] 
**price_configuration** | [**ProductCatalogItemPriceConfiguration**](ProductCatalogItemPriceConfiguration.md) |  | [optional] 

## Example

```python
from pandadoc_client.models.product_catalog_item_patch_request_product_variant import ProductCatalogItemPatchRequestProductVariant

# TODO update the JSON string below
json = "{}"
# create an instance of ProductCatalogItemPatchRequestProductVariant from a JSON string
product_catalog_item_patch_request_product_variant_instance = ProductCatalogItemPatchRequestProductVariant.from_json(json)
# print the JSON string representation of the object
print(ProductCatalogItemPatchRequestProductVariant.to_json())

# convert the object into a dict
product_catalog_item_patch_request_product_variant_dict = product_catalog_item_patch_request_product_variant_instance.to_dict()
# create an instance of ProductCatalogItemPatchRequestProductVariant from a dict
product_catalog_item_patch_request_product_variant_from_dict = ProductCatalogItemPatchRequestProductVariant.from_dict(product_catalog_item_patch_request_product_variant_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


