# LinkedObjectCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider** | **str** | CRM name (lowercase).  See the list of available providers: https://developers.pandadoc.com/reference/link-service#examples-of-the-most-popular-crms  | 
**entity_type** | **str** | Entity type.  See the available entity types: https://developers.pandadoc.com/reference/link-service#examples-of-the-most-popular-crms  | 
**entity_id** | **str** | Entity unique identifier. The system validates if the entity exists. | 

## Example

```python
from pandadoc_client.models.linked_object_create_request import LinkedObjectCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of LinkedObjectCreateRequest from a JSON string
linked_object_create_request_instance = LinkedObjectCreateRequest.from_json(json)
# print the JSON string representation of the object
print(LinkedObjectCreateRequest.to_json())

# convert the object into a dict
linked_object_create_request_dict = linked_object_create_request_instance.to_dict()
# create an instance of LinkedObjectCreateRequest from a dict
linked_object_create_request_from_dict = LinkedObjectCreateRequest.from_dict(linked_object_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


