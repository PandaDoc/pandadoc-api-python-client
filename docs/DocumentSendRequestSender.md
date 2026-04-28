# DocumentSendRequestSender

You can set a sender of a document as an `email` or `membership_id`

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**membership_id** | **str** | Membership ID. | [optional] 
**email** | **str** | Email. | [optional] 

## Example

```python
from pandadoc_client.models.document_send_request_sender import DocumentSendRequestSender

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentSendRequestSender from a JSON string
document_send_request_sender_instance = DocumentSendRequestSender.from_json(json)
# print the JSON string representation of the object
print(DocumentSendRequestSender.to_json())

# convert the object into a dict
document_send_request_sender_dict = document_send_request_sender_instance.to_dict()
# create an instance of DocumentSendRequestSender from a dict
document_send_request_sender_from_dict = DocumentSendRequestSender.from_dict(document_send_request_sender_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


