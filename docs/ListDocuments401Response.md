# ListDocuments401Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**detail** | **str** |  | [optional] 

## Example

```python
from pandadoc_client.models.list_documents401_response import ListDocuments401Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListDocuments401Response from a JSON string
list_documents401_response_instance = ListDocuments401Response.from_json(json)
# print the JSON string representation of the object
print(ListDocuments401Response.to_json())

# convert the object into a dict
list_documents401_response_dict = list_documents401_response_instance.to_dict()
# create an instance of ListDocuments401Response from a dict
list_documents401_response_from_dict = ListDocuments401Response.from_dict(list_documents401_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


