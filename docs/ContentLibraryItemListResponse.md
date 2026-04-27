# ContentLibraryItemListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[ContentLibraryItemListResponseResultsInner]**](ContentLibraryItemListResponseResultsInner.md) |  | [optional] 

## Example

```python
from pandadoc_client.models.content_library_item_list_response import ContentLibraryItemListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ContentLibraryItemListResponse from a JSON string
content_library_item_list_response_instance = ContentLibraryItemListResponse.from_json(json)
# print the JSON string representation of the object
print(ContentLibraryItemListResponse.to_json())

# convert the object into a dict
content_library_item_list_response_dict = content_library_item_list_response_instance.to_dict()
# create an instance of ContentLibraryItemListResponse from a dict
content_library_item_list_response_from_dict = ContentLibraryItemListResponse.from_dict(content_library_item_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


