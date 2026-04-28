# ListDocumentsByLinkedObjectsResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**date_created** | **str** |  | [optional] 
**template_id** | **str** |  | [optional] 

## Example

```python
from pandadoc_client.models.list_documents_by_linked_objects_response_inner import ListDocumentsByLinkedObjectsResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of ListDocumentsByLinkedObjectsResponseInner from a JSON string
list_documents_by_linked_objects_response_inner_instance = ListDocumentsByLinkedObjectsResponseInner.from_json(json)
# print the JSON string representation of the object
print(ListDocumentsByLinkedObjectsResponseInner.to_json())

# convert the object into a dict
list_documents_by_linked_objects_response_inner_dict = list_documents_by_linked_objects_response_inner_instance.to_dict()
# create an instance of ListDocumentsByLinkedObjectsResponseInner from a dict
list_documents_by_linked_objects_response_inner_from_dict = ListDocumentsByLinkedObjectsResponseInner.from_dict(list_documents_by_linked_objects_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


