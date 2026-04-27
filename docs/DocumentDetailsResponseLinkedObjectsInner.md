# DocumentDetailsResponseLinkedObjectsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider** | **str** | Linked object provider. | [optional] 
**entity_type** | **str** | Linked object entity type. | [optional] 
**entity_id** | **str** | Linked object entity ID. | [optional] 
**id** | **str** | Linked object ID. | [optional] 
**children** | [**List[DocumentDetailsResponseLinkedObjectsInnerChildrenInner]**](DocumentDetailsResponseLinkedObjectsInnerChildrenInner.md) | Linked object children array. | [optional] 

## Example

```python
from pandadoc_client.models.document_details_response_linked_objects_inner import DocumentDetailsResponseLinkedObjectsInner

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentDetailsResponseLinkedObjectsInner from a JSON string
document_details_response_linked_objects_inner_instance = DocumentDetailsResponseLinkedObjectsInner.from_json(json)
# print the JSON string representation of the object
print(DocumentDetailsResponseLinkedObjectsInner.to_json())

# convert the object into a dict
document_details_response_linked_objects_inner_dict = document_details_response_linked_objects_inner_instance.to_dict()
# create an instance of DocumentDetailsResponseLinkedObjectsInner from a dict
document_details_response_linked_objects_inner_from_dict = DocumentDetailsResponseLinkedObjectsInner.from_dict(document_details_response_linked_objects_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


