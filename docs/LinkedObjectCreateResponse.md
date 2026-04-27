# LinkedObjectCreateResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Linked object identifier (link_id). | [optional] 
**provider** | **str** | CRM name (lowercase).  See the list of available providers: https://developers.pandadoc.com/reference/link-service#examples-of-the-most-popular-crms  | [optional] 
**entity_type** | **str** | Entity type.  See the available entity types: https://developers.pandadoc.com/reference/link-service#examples-of-the-most-popular-crms  | [optional] 
**entity_id** | **str** | Entity unique identifier. The system validates if the entity exists. | [optional] 
**children** | [**List[LinkedObjectChild]**](LinkedObjectChild.md) |  | [optional] 

## Example

```python
from pandadoc_client.models.linked_object_create_response import LinkedObjectCreateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LinkedObjectCreateResponse from a JSON string
linked_object_create_response_instance = LinkedObjectCreateResponse.from_json(json)
# print the JSON string representation of the object
print(LinkedObjectCreateResponse.to_json())

# convert the object into a dict
linked_object_create_response_dict = linked_object_create_response_instance.to_dict()
# create an instance of LinkedObjectCreateResponse from a dict
linked_object_create_response_from_dict = LinkedObjectCreateResponse.from_dict(linked_object_create_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


