# ContentLibraryItemCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the Content Library Item. | [optional] 

## Example

```python
from pandadoc_client.models.content_library_item_create_request import ContentLibraryItemCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ContentLibraryItemCreateRequest from a JSON string
content_library_item_create_request_instance = ContentLibraryItemCreateRequest.from_json(json)
# print the JSON string representation of the object
print(ContentLibraryItemCreateRequest.to_json())

# convert the object into a dict
content_library_item_create_request_dict = content_library_item_create_request_instance.to_dict()
# create an instance of ContentLibraryItemCreateRequest from a dict
content_library_item_create_request_from_dict = ContentLibraryItemCreateRequest.from_dict(content_library_item_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


