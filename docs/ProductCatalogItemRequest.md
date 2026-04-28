# ProductCatalogItemRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | 
**category_id** | **str** |  | [optional] 
**sku** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**type** | [**ProductCatalogTypeEnum**](ProductCatalogTypeEnum.md) |  | [optional] [default to ProductCatalogTypeEnum.REGULAR]
**bundle_items** | [**List[ProductCatalogItemRequestBundleItemsInner]**](ProductCatalogItemRequestBundleItemsInner.md) |  | [optional] 
**images** | [**List[ProductCatalogItemRequestImagesInner]**](ProductCatalogItemRequestImagesInner.md) |  | [optional] 
**custom_fields** | [**List[ProductCatalogItemRequestCustomFieldsInner]**](ProductCatalogItemRequestCustomFieldsInner.md) |  | [optional] 
**price_configuration** | [**ProductCatalogItemPriceConfiguration**](ProductCatalogItemPriceConfiguration.md) |  | 

## Example

```python
from pandadoc_client.models.product_catalog_item_request import ProductCatalogItemRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ProductCatalogItemRequest from a JSON string
product_catalog_item_request_instance = ProductCatalogItemRequest.from_json(json)
# print the JSON string representation of the object
print(ProductCatalogItemRequest.to_json())

# convert the object into a dict
product_catalog_item_request_dict = product_catalog_item_request_instance.to_dict()
# create an instance of ProductCatalogItemRequest from a dict
product_catalog_item_request_from_dict = ProductCatalogItemRequest.from_dict(product_catalog_item_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


