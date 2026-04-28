# ListDocuments400Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**detail** | **object** |  | [optional] 

## Example

```python
from pandadoc_client.models.list_documents400_response import ListDocuments400Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListDocuments400Response from a JSON string
list_documents400_response_instance = ListDocuments400Response.from_json(json)
# print the JSON string representation of the object
print(ListDocuments400Response.to_json())

# convert the object into a dict
list_documents400_response_dict = list_documents400_response_instance.to_dict()
# create an instance of ListDocuments400Response from a dict
list_documents400_response_from_dict = ListDocuments400Response.from_dict(list_documents400_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


