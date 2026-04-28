# ProductCatalogItemPriceTier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **float** |  | 
**min_qty** | **float** |  | 

## Example

```python
from pandadoc_client.models.product_catalog_item_price_tier import ProductCatalogItemPriceTier

# TODO update the JSON string below
json = "{}"
# create an instance of ProductCatalogItemPriceTier from a JSON string
product_catalog_item_price_tier_instance = ProductCatalogItemPriceTier.from_json(json)
# print the JSON string representation of the object
print(ProductCatalogItemPriceTier.to_json())

# convert the object into a dict
product_catalog_item_price_tier_dict = product_catalog_item_price_tier_instance.to_dict()
# create an instance of ProductCatalogItemPriceTier from a dict
product_catalog_item_price_tier_from_dict = ProductCatalogItemPriceTier.from_dict(product_catalog_item_price_tier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


