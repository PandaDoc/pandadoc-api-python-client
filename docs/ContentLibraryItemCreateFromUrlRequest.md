# ContentLibraryItemCreateFromUrlRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the Content Library Item. | [optional] 
**url** | **str** | Secure (HTTPS) and publicly accessible URL to the PDF document. | [optional] 

## Example

```python
from pandadoc_client.models.content_library_item_create_from_url_request import ContentLibraryItemCreateFromUrlRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ContentLibraryItemCreateFromUrlRequest from a JSON string
content_library_item_create_from_url_request_instance = ContentLibraryItemCreateFromUrlRequest.from_json(json)
# print the JSON string representation of the object
print(ContentLibraryItemCreateFromUrlRequest.to_json())

# convert the object into a dict
content_library_item_create_from_url_request_dict = content_library_item_create_from_url_request_instance.to_dict()
# create an instance of ContentLibraryItemCreateFromUrlRequest from a dict
content_library_item_create_from_url_request_from_dict = ContentLibraryItemCreateFromUrlRequest.from_dict(content_library_item_create_from_url_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


