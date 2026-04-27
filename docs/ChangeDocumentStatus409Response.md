# ChangeDocumentStatus409Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**info_message** | **str** |  | [optional] 

## Example

```python
from pandadoc_client.models.change_document_status409_response import ChangeDocumentStatus409Response

# TODO update the JSON string below
json = "{}"
# create an instance of ChangeDocumentStatus409Response from a JSON string
change_document_status409_response_instance = ChangeDocumentStatus409Response.from_json(json)
# print the JSON string representation of the object
print(ChangeDocumentStatus409Response.to_json())

# convert the object into a dict
change_document_status409_response_dict = change_document_status409_response_instance.to_dict()
# create an instance of ChangeDocumentStatus409Response from a dict
change_document_status409_response_from_dict = ChangeDocumentStatus409Response.from_dict(change_document_status409_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


