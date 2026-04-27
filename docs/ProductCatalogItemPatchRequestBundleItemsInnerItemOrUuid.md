# ProductCatalogItemPatchRequestBundleItemsInnerItemOrUuid


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
from pandadoc_client.models.product_catalog_item_patch_request_bundle_items_inner_item_or_uuid import ProductCatalogItemPatchRequestBundleItemsInnerItemOrUuid

# TODO update the JSON string below
json = "{}"
# create an instance of ProductCatalogItemPatchRequestBundleItemsInnerItemOrUuid from a JSON string
product_catalog_item_patch_request_bundle_items_inner_item_or_uuid_instance = ProductCatalogItemPatchRequestBundleItemsInnerItemOrUuid.from_json(json)
# print the JSON string representation of the object
print(ProductCatalogItemPatchRequestBundleItemsInnerItemOrUuid.to_json())

# convert the object into a dict
product_catalog_item_patch_request_bundle_items_inner_item_or_uuid_dict = product_catalog_item_patch_request_bundle_items_inner_item_or_uuid_instance.to_dict()
# create an instance of ProductCatalogItemPatchRequestBundleItemsInnerItemOrUuid from a dict
product_catalog_item_patch_request_bundle_items_inner_item_or_uuid_from_dict = ProductCatalogItemPatchRequestBundleItemsInnerItemOrUuid.from_dict(product_catalog_item_patch_request_bundle_items_inner_item_or_uuid_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


