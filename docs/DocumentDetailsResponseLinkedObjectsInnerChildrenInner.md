# DocumentDetailsResponseLinkedObjectsInnerChildrenInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_type** | **str** | Linked object child entity type. | [optional] 
**entity_id** | **str** | Linked object child entity ID. | [optional] 
**id** | **str** | Linked object child ID. | [optional] 

## Example

```python
from pandadoc_client.models.document_details_response_linked_objects_inner_children_inner import DocumentDetailsResponseLinkedObjectsInnerChildrenInner

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentDetailsResponseLinkedObjectsInnerChildrenInner from a JSON string
document_details_response_linked_objects_inner_children_inner_instance = DocumentDetailsResponseLinkedObjectsInnerChildrenInner.from_json(json)
# print the JSON string representation of the object
print(DocumentDetailsResponseLinkedObjectsInnerChildrenInner.to_json())

# convert the object into a dict
document_details_response_linked_objects_inner_children_inner_dict = document_details_response_linked_objects_inner_children_inner_instance.to_dict()
# create an instance of DocumentDetailsResponseLinkedObjectsInnerChildrenInner from a dict
document_details_response_linked_objects_inner_children_inner_from_dict = DocumentDetailsResponseLinkedObjectsInnerChildrenInner.from_dict(document_details_response_linked_objects_inner_children_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


