# ListDocuments429Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**detail** | **str** |  | [optional] 

## Example

```python
from pandadoc_client.models.list_documents429_response import ListDocuments429Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListDocuments429Response from a JSON string
list_documents429_response_instance = ListDocuments429Response.from_json(json)
# print the JSON string representation of the object
print(ListDocuments429Response.to_json())

# convert the object into a dict
list_documents429_response_dict = list_documents429_response_instance.to_dict()
# create an instance of ListDocuments429Response from a dict
list_documents429_response_from_dict = ListDocuments429Response.from_dict(list_documents429_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


