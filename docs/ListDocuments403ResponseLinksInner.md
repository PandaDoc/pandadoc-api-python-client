# ListDocuments403ResponseLinksInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rel** | **str** |  | [optional] 
**href** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from pandadoc_client.models.list_documents403_response_links_inner import ListDocuments403ResponseLinksInner

# TODO update the JSON string below
json = "{}"
# create an instance of ListDocuments403ResponseLinksInner from a JSON string
list_documents403_response_links_inner_instance = ListDocuments403ResponseLinksInner.from_json(json)
# print the JSON string representation of the object
print(ListDocuments403ResponseLinksInner.to_json())

# convert the object into a dict
list_documents403_response_links_inner_dict = list_documents403_response_links_inner_instance.to_dict()
# create an instance of ListDocuments403ResponseLinksInner from a dict
list_documents403_response_links_inner_from_dict = ListDocuments403ResponseLinksInner.from_dict(list_documents403_response_links_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


