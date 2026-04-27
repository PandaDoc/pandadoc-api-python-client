# ProductCatalogItemResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**date_created** | **datetime** |  | [optional] 
**date_modified** | **datetime** |  | [optional] 
**created_by** | **str** |  | [optional] 
**modified_by** | **str** |  | [optional] 
**category_id** | **str** |  | [optional] 
**category_name** | **str** |  | [optional] 
**type** | [**ProductCatalogTypeEnum**](ProductCatalogTypeEnum.md) |  | [optional] [default to ProductCatalogTypeEnum.REGULAR]
**bundle_items** | [**List[ProductCatalogItemResponseBundleItemsInner]**](ProductCatalogItemResponseBundleItemsInner.md) |  | [optional] 
**default_price_configuration** | [**ProductCatalogItemResponseDefaultPriceConfiguration**](ProductCatalogItemResponseDefaultPriceConfiguration.md) |  | [optional] 
**variants** | [**List[ProductCatalogItemResponseVariantsInner]**](ProductCatalogItemResponseVariantsInner.md) |  | [optional] 

## Example

```python
from pandadoc_client.models.product_catalog_item_response import ProductCatalogItemResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ProductCatalogItemResponse from a JSON string
product_catalog_item_response_instance = ProductCatalogItemResponse.from_json(json)
# print the JSON string representation of the object
print(ProductCatalogItemResponse.to_json())

# convert the object into a dict
product_catalog_item_response_dict = product_catalog_item_response_instance.to_dict()
# create an instance of ProductCatalogItemResponse from a dict
product_catalog_item_response_from_dict = ProductCatalogItemResponse.from_dict(product_catalog_item_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


