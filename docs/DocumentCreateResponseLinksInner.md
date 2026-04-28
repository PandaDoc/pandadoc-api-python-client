# DocumentCreateResponseLinksInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rel** | **str** |  | [optional] 
**href** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from pandadoc_client.models.document_create_response_links_inner import DocumentCreateResponseLinksInner

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentCreateResponseLinksInner from a JSON string
document_create_response_links_inner_instance = DocumentCreateResponseLinksInner.from_json(json)
# print the JSON string representation of the object
print(DocumentCreateResponseLinksInner.to_json())

# convert the object into a dict
document_create_response_links_inner_dict = document_create_response_links_inner_instance.to_dict()
# create an instance of DocumentCreateResponseLinksInner from a dict
document_create_response_links_inner_from_dict = DocumentCreateResponseLinksInner.from_dict(document_create_response_links_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


