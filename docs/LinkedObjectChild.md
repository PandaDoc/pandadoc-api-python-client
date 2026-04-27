# LinkedObjectChild

Child entity reference in a hierarchical chain structure that provides essential metadata and direct access links for lazy-loading the complete object by ID.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Linked object identifier (link_id). | [optional] 
**entity_type** | **str** | Entity type.  See the available entity types: https://developers.pandadoc.com/reference/link-service#examples-of-the-most-popular-crms  | [optional] 
**entity_id** | **str** | Entity unique identifier. The system validates if the entity exists. | [optional] 

## Example

```python
from pandadoc_client.models.linked_object_child import LinkedObjectChild

# TODO update the JSON string below
json = "{}"
# create an instance of LinkedObjectChild from a JSON string
linked_object_child_instance = LinkedObjectChild.from_json(json)
# print the JSON string representation of the object
print(LinkedObjectChild.to_json())

# convert the object into a dict
linked_object_child_dict = linked_object_child_instance.to_dict()
# create an instance of LinkedObjectChild from a dict
linked_object_child_from_dict = LinkedObjectChild.from_dict(linked_object_child_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


