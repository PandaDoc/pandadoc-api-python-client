# ProductCatalogItemPatchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | [optional] 
**category_id** | **str** |  | [optional] 
**type** | [**ProductCatalogTypeEnum**](ProductCatalogTypeEnum.md) |  | [optional] [default to ProductCatalogTypeEnum.REGULAR]
**bundle_items** | [**List[ProductCatalogItemPatchRequestBundleItemsInner]**](ProductCatalogItemPatchRequestBundleItemsInner.md) |  | [optional] 
**product_variant** | [**ProductCatalogItemPatchRequestProductVariant**](ProductCatalogItemPatchRequestProductVariant.md) |  | [optional] 

## Example

```python
from pandadoc_client.models.product_catalog_item_patch_request import ProductCatalogItemPatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ProductCatalogItemPatchRequest from a JSON string
product_catalog_item_patch_request_instance = ProductCatalogItemPatchRequest.from_json(json)
# print the JSON string representation of the object
print(ProductCatalogItemPatchRequest.to_json())

# convert the object into a dict
product_catalog_item_patch_request_dict = product_catalog_item_patch_request_instance.to_dict()
# create an instance of ProductCatalogItemPatchRequest from a dict
product_catalog_item_patch_request_from_dict = ProductCatalogItemPatchRequest.from_dict(product_catalog_item_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


