# ProductCatalogItemResponseBundleItemsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quantity** | **int** |  | [optional] 
**item** | [**ProductCatalogItemResponseBundleItemsInnerItem**](ProductCatalogItemResponseBundleItemsInnerItem.md) |  | [optional] 

## Example

```python
from pandadoc_client.models.product_catalog_item_response_bundle_items_inner import ProductCatalogItemResponseBundleItemsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ProductCatalogItemResponseBundleItemsInner from a JSON string
product_catalog_item_response_bundle_items_inner_instance = ProductCatalogItemResponseBundleItemsInner.from_json(json)
# print the JSON string representation of the object
print(ProductCatalogItemResponseBundleItemsInner.to_json())

# convert the object into a dict
product_catalog_item_response_bundle_items_inner_dict = product_catalog_item_response_bundle_items_inner_instance.to_dict()
# create an instance of ProductCatalogItemResponseBundleItemsInner from a dict
product_catalog_item_response_bundle_items_inner_from_dict = ProductCatalogItemResponseBundleItemsInner.from_dict(product_catalog_item_response_bundle_items_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


