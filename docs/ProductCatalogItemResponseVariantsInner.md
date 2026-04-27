# ProductCatalogItemResponseVariantsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** |  | [optional] 
**sku** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**custom_fields** | [**List[ProductCatalogSearchCatalogItemResponseCustomFieldsInner]**](ProductCatalogSearchCatalogItemResponseCustomFieldsInner.md) |  | [optional] 
**images** | [**List[ProductCatalogSearchCatalogItemResponseImagesInner]**](ProductCatalogSearchCatalogItemResponseImagesInner.md) |  | [optional] 
**date_created** | **datetime** |  | [optional] 
**date_modified** | **datetime** |  | [optional] 
**status** | **float** |  | [optional] 
**price_configurations** | [**List[ProductCatalogItemResponseDefaultPriceConfiguration]**](ProductCatalogItemResponseDefaultPriceConfiguration.md) |  | [optional] 

## Example

```python
from pandadoc_client.models.product_catalog_item_response_variants_inner import ProductCatalogItemResponseVariantsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ProductCatalogItemResponseVariantsInner from a JSON string
product_catalog_item_response_variants_inner_instance = ProductCatalogItemResponseVariantsInner.from_json(json)
# print the JSON string representation of the object
print(ProductCatalogItemResponseVariantsInner.to_json())

# convert the object into a dict
product_catalog_item_response_variants_inner_dict = product_catalog_item_response_variants_inner_instance.to_dict()
# create an instance of ProductCatalogItemResponseVariantsInner from a dict
product_catalog_item_response_variants_inner_from_dict = ProductCatalogItemResponseVariantsInner.from_dict(product_catalog_item_response_variants_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


