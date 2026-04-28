# AddDsvNamedItemsRequestItemsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The display name of the item (e.g., \&quot;Introduction\&quot;, \&quot;Chapter 1\&quot;). | 
**level** | **int** | Hierarchical level of the item.  Level 0 is the highest (top-level), with increasing numbers for nested structures.  | 
**page_name** | **str** | Internal reference or identifier for the page this item is associated with. | 

## Example

```python
from pandadoc_client.models.add_dsv_named_items_request_items_inner import AddDsvNamedItemsRequestItemsInner

# TODO update the JSON string below
json = "{}"
# create an instance of AddDsvNamedItemsRequestItemsInner from a JSON string
add_dsv_named_items_request_items_inner_instance = AddDsvNamedItemsRequestItemsInner.from_json(json)
# print the JSON string representation of the object
print(AddDsvNamedItemsRequestItemsInner.to_json())

# convert the object into a dict
add_dsv_named_items_request_items_inner_dict = add_dsv_named_items_request_items_inner_instance.to_dict()
# create an instance of AddDsvNamedItemsRequestItemsInner from a dict
add_dsv_named_items_request_items_inner_from_dict = AddDsvNamedItemsRequestItemsInner.from_dict(add_dsv_named_items_request_items_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


