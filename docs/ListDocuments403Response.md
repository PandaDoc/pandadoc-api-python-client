# ListDocuments403Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**detail** | **str** |  | [optional] 
**info_message** | **str** | Human-readable explanation of the permission error. | [optional] 
**links** | [**List[ListDocuments403ResponseLinksInner]**](ListDocuments403ResponseLinksInner.md) | Optional links related to the error (e.g. a status endpoint). | [optional] 

## Example

```python
from pandadoc_client.models.list_documents403_response import ListDocuments403Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListDocuments403Response from a JSON string
list_documents403_response_instance = ListDocuments403Response.from_json(json)
# print the JSON string representation of the object
print(ListDocuments403Response.to_json())

# convert the object into a dict
list_documents403_response_dict = list_documents403_response_instance.to_dict()
# create an instance of ListDocuments403Response from a dict
list_documents403_response_from_dict = ListDocuments403Response.from_dict(list_documents403_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


