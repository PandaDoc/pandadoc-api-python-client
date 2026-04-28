# ContentLibraryItemListResponseResultsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**date_created** | **str** |  | [optional] 
**date_modified** | **str** |  | [optional] 
**version** | **str** |  | [optional] 

## Example

```python
from pandadoc_client.models.content_library_item_list_response_results_inner import ContentLibraryItemListResponseResultsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ContentLibraryItemListResponseResultsInner from a JSON string
content_library_item_list_response_results_inner_instance = ContentLibraryItemListResponseResultsInner.from_json(json)
# print the JSON string representation of the object
print(ContentLibraryItemListResponseResultsInner.to_json())

# convert the object into a dict
content_library_item_list_response_results_inner_dict = content_library_item_list_response_results_inner_instance.to_dict()
# create an instance of ContentLibraryItemListResponseResultsInner from a dict
content_library_item_list_response_results_inner_from_dict = ContentLibraryItemListResponseResultsInner.from_dict(content_library_item_list_response_results_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


