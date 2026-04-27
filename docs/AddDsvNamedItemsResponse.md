# AddDsvNamedItemsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[AddDsvNamedItemsResponseResultsInner]**](AddDsvNamedItemsResponseResultsInner.md) | List of DSV named items that were created. | 
**count** | **float** | Total number of items created. | 

## Example

```python
from pandadoc_client.models.add_dsv_named_items_response import AddDsvNamedItemsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AddDsvNamedItemsResponse from a JSON string
add_dsv_named_items_response_instance = AddDsvNamedItemsResponse.from_json(json)
# print the JSON string representation of the object
print(AddDsvNamedItemsResponse.to_json())

# convert the object into a dict
add_dsv_named_items_response_dict = add_dsv_named_items_response_instance.to_dict()
# create an instance of AddDsvNamedItemsResponse from a dict
add_dsv_named_items_response_from_dict = AddDsvNamedItemsResponse.from_dict(add_dsv_named_items_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


