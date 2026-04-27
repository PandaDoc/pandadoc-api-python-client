# DocumentSendRequestForwardingSettings

Set settings for Document and Signature forwarding.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**forwarding_allowed** | **bool** | Your recipient will be able/not able to forward the document to another email address. | [optional] 
**forwarding_with_reassigning_allowed** | **bool** | Your recipient will be able/not able to forward the right to fill out all fields (including signature) assigned to them to another email address. | [optional] 

## Example

```python
from pandadoc_client.models.document_send_request_forwarding_settings import DocumentSendRequestForwardingSettings

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentSendRequestForwardingSettings from a JSON string
document_send_request_forwarding_settings_instance = DocumentSendRequestForwardingSettings.from_json(json)
# print the JSON string representation of the object
print(DocumentSendRequestForwardingSettings.to_json())

# convert the object into a dict
document_send_request_forwarding_settings_dict = document_send_request_forwarding_settings_instance.to_dict()
# create an instance of DocumentSendRequestForwardingSettings from a dict
document_send_request_forwarding_settings_from_dict = DocumentSendRequestForwardingSettings.from_dict(document_send_request_forwarding_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


