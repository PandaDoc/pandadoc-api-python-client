# AddDsvNamedItemsResponseResultsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the created DSV item. | 
**name** | **str** | The display name of the item. | 
**level** | **int** | The hierarchy level of the item. | 
**page_name** | **str** | Internal reference name for the page. | 
**page_uuid** | **str** | UUID of the associated page. | 

## Example

```python
from pandadoc_client.models.add_dsv_named_items_response_results_inner import AddDsvNamedItemsResponseResultsInner

# TODO update the JSON string below
json = "{}"
# create an instance of AddDsvNamedItemsResponseResultsInner from a JSON string
add_dsv_named_items_response_results_inner_instance = AddDsvNamedItemsResponseResultsInner.from_json(json)
# print the JSON string representation of the object
print(AddDsvNamedItemsResponseResultsInner.to_json())

# convert the object into a dict
add_dsv_named_items_response_results_inner_dict = add_dsv_named_items_response_results_inner_instance.to_dict()
# create an instance of AddDsvNamedItemsResponseResultsInner from a dict
add_dsv_named_items_response_results_inner_from_dict = AddDsvNamedItemsResponseResultsInner.from_dict(add_dsv_named_items_response_results_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


