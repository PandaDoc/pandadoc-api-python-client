# DocumentSendResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**date_created** | **str** |  | [optional] 
**date_modified** | **str** |  | [optional] 
**date_completed** | **str** | Document completion date. | [optional] 
**expiration_date** | **str** |  | [optional] 
**version** | **str** |  | [optional] 
**uuid** | **str** |  | [optional] 
**recipients** | [**List[DocumentSendResponseRecipientsInner]**](DocumentSendResponseRecipientsInner.md) |  | [optional] 

## Example

```python
from pandadoc_client.models.document_send_response import DocumentSendResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentSendResponse from a JSON string
document_send_response_instance = DocumentSendResponse.from_json(json)
# print the JSON string representation of the object
print(DocumentSendResponse.to_json())

# convert the object into a dict
document_send_response_dict = document_send_response_instance.to_dict()
# create an instance of DocumentSendResponse from a dict
document_send_response_from_dict = DocumentSendResponse.from_dict(document_send_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


