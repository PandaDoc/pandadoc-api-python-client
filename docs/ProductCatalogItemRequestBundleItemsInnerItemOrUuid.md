# ProductCatalogItemRequestBundleItemsInnerItemOrUuid


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
from pandadoc_client.models.product_catalog_item_request_bundle_items_inner_item_or_uuid import ProductCatalogItemRequestBundleItemsInnerItemOrUuid

# TODO update the JSON string below
json = "{}"
# create an instance of ProductCatalogItemRequestBundleItemsInnerItemOrUuid from a JSON string
product_catalog_item_request_bundle_items_inner_item_or_uuid_instance = ProductCatalogItemRequestBundleItemsInnerItemOrUuid.from_json(json)
# print the JSON string representation of the object
print(ProductCatalogItemRequestBundleItemsInnerItemOrUuid.to_json())

# convert the object into a dict
product_catalog_item_request_bundle_items_inner_item_or_uuid_dict = product_catalog_item_request_bundle_items_inner_item_or_uuid_instance.to_dict()
# create an instance of ProductCatalogItemRequestBundleItemsInnerItemOrUuid from a dict
product_catalog_item_request_bundle_items_inner_item_or_uuid_from_dict = ProductCatalogItemRequestBundleItemsInnerItemOrUuid.from_dict(product_catalog_item_request_bundle_items_inner_item_or_uuid_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


