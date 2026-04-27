# ContentLibraryItemResponseCreatedBy


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**avatar** | **str** |  | [optional] 

## Example

```python
from pandadoc_client.models.content_library_item_response_created_by import ContentLibraryItemResponseCreatedBy

# TODO update the JSON string below
json = "{}"
# create an instance of ContentLibraryItemResponseCreatedBy from a JSON string
content_library_item_response_created_by_instance = ContentLibraryItemResponseCreatedBy.from_json(json)
# print the JSON string representation of the object
print(ContentLibraryItemResponseCreatedBy.to_json())

# convert the object into a dict
content_library_item_response_created_by_dict = content_library_item_response_created_by_instance.to_dict()
# create an instance of ContentLibraryItemResponseCreatedBy from a dict
content_library_item_response_created_by_from_dict = ContentLibraryItemResponseCreatedBy.from_dict(content_library_item_response_created_by_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


