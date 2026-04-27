# ProductCatalogItemRequestCustomFieldsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**value** | **str** |  | [optional] 

## Example

```python
from pandadoc_client.models.product_catalog_item_request_custom_fields_inner import ProductCatalogItemRequestCustomFieldsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ProductCatalogItemRequestCustomFieldsInner from a JSON string
product_catalog_item_request_custom_fields_inner_instance = ProductCatalogItemRequestCustomFieldsInner.from_json(json)
# print the JSON string representation of the object
print(ProductCatalogItemRequestCustomFieldsInner.to_json())

# convert the object into a dict
product_catalog_item_request_custom_fields_inner_dict = product_catalog_item_request_custom_fields_inner_instance.to_dict()
# create an instance of ProductCatalogItemRequestCustomFieldsInner from a dict
product_catalog_item_request_custom_fields_inner_from_dict = ProductCatalogItemRequestCustomFieldsInner.from_dict(product_catalog_item_request_custom_fields_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


