# ProductCatalogItemResponseDefaultPriceConfiguration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency** | **str** |  | 
**price** | **float** |  | [optional] 
**cost** | **float** |  | [optional] 
**billing_type** | **str** |  | [optional] 
**billing_cycle** | **str** |  | [optional] 
**tiers** | [**List[ProductCatalogItemPriceTier]**](ProductCatalogItemPriceTier.md) | only for volume based pricing | [optional] 
**pricing_method** | **float** |  | 
**uuid** | **str** |  | [optional] 

## Example

```python
from pandadoc_client.models.product_catalog_item_response_default_price_configuration import ProductCatalogItemResponseDefaultPriceConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of ProductCatalogItemResponseDefaultPriceConfiguration from a JSON string
product_catalog_item_response_default_price_configuration_instance = ProductCatalogItemResponseDefaultPriceConfiguration.from_json(json)
# print the JSON string representation of the object
print(ProductCatalogItemResponseDefaultPriceConfiguration.to_json())

# convert the object into a dict
product_catalog_item_response_default_price_configuration_dict = product_catalog_item_response_default_price_configuration_instance.to_dict()
# create an instance of ProductCatalogItemResponseDefaultPriceConfiguration from a dict
product_catalog_item_response_default_price_configuration_from_dict = ProductCatalogItemResponseDefaultPriceConfiguration.from_dict(product_catalog_item_response_default_price_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


