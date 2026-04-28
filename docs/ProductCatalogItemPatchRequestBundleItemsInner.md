# ProductCatalogItemPatchRequestBundleItemsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quantity** | **int** |  | [optional] 
**item_or_uuid** | [**ProductCatalogItemPatchRequestBundleItemsInnerItemOrUuid**](ProductCatalogItemPatchRequestBundleItemsInnerItemOrUuid.md) |  | [optional] 

## Example

```python
from pandadoc_client.models.product_catalog_item_patch_request_bundle_items_inner import ProductCatalogItemPatchRequestBundleItemsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ProductCatalogItemPatchRequestBundleItemsInner from a JSON string
product_catalog_item_patch_request_bundle_items_inner_instance = ProductCatalogItemPatchRequestBundleItemsInner.from_json(json)
# print the JSON string representation of the object
print(ProductCatalogItemPatchRequestBundleItemsInner.to_json())

# convert the object into a dict
product_catalog_item_patch_request_bundle_items_inner_dict = product_catalog_item_patch_request_bundle_items_inner_instance.to_dict()
# create an instance of ProductCatalogItemPatchRequestBundleItemsInner from a dict
product_catalog_item_patch_request_bundle_items_inner_from_dict = ProductCatalogItemPatchRequestBundleItemsInner.from_dict(product_catalog_item_patch_request_bundle_items_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


