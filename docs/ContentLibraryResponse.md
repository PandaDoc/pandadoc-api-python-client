# ContentLibraryResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**date_created** | **datetime** |  | [optional] 
**date_modified** | **datetime** |  | [optional] 
**version** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from pandadoc_client.models.content_library_response import ContentLibraryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ContentLibraryResponse from a JSON string
content_library_response_instance = ContentLibraryResponse.from_json(json)
# print the JSON string representation of the object
print(ContentLibraryResponse.to_json())

# convert the object into a dict
content_library_response_dict = content_library_response_instance.to_dict()
# create an instance of ContentLibraryResponse from a dict
content_library_response_from_dict = ContentLibraryResponse.from_dict(content_library_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


