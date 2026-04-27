# LinkedObjectListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**linked_objects** | [**List[LinkedObjectCreateResponse]**](LinkedObjectCreateResponse.md) |  | [optional] 

## Example

```python
from pandadoc_client.models.linked_object_list_response import LinkedObjectListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LinkedObjectListResponse from a JSON string
linked_object_list_response_instance = LinkedObjectListResponse.from_json(json)
# print the JSON string representation of the object
print(LinkedObjectListResponse.to_json())

# convert the object into a dict
linked_object_list_response_dict = linked_object_list_response_instance.to_dict()
# create an instance of LinkedObjectListResponse from a dict
linked_object_list_response_from_dict = LinkedObjectListResponse.from_dict(linked_object_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


