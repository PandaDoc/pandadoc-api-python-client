# ProductCatalogItemRequestImagesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_main** | **bool** |  | [optional] 
**order** | **float** |  | [optional] 
**src** | **str** |  | [optional] 

## Example

```python
from pandadoc_client.models.product_catalog_item_request_images_inner import ProductCatalogItemRequestImagesInner

# TODO update the JSON string below
json = "{}"
# create an instance of ProductCatalogItemRequestImagesInner from a JSON string
product_catalog_item_request_images_inner_instance = ProductCatalogItemRequestImagesInner.from_json(json)
# print the JSON string representation of the object
print(ProductCatalogItemRequestImagesInner.to_json())

# convert the object into a dict
product_catalog_item_request_images_inner_dict = product_catalog_item_request_images_inner_instance.to_dict()
# create an instance of ProductCatalogItemRequestImagesInner from a dict
product_catalog_item_request_images_inner_from_dict = ProductCatalogItemRequestImagesInner.from_dict(product_catalog_item_request_images_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


