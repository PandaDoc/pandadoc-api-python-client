# AddDsvNamedItemsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[AddDsvNamedItemsRequestItemsInner]**](AddDsvNamedItemsRequestItemsInner.md) | List of named items representing structural elements of the document. | 

## Example

```python
from pandadoc_client.models.add_dsv_named_items_request import AddDsvNamedItemsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddDsvNamedItemsRequest from a JSON string
add_dsv_named_items_request_instance = AddDsvNamedItemsRequest.from_json(json)
# print the JSON string representation of the object
print(AddDsvNamedItemsRequest.to_json())

# convert the object into a dict
add_dsv_named_items_request_dict = add_dsv_named_items_request_instance.to_dict()
# create an instance of AddDsvNamedItemsRequest from a dict
add_dsv_named_items_request_from_dict = AddDsvNamedItemsRequest.from_dict(add_dsv_named_items_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


