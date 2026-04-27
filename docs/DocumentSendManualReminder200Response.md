# DocumentSendManualReminder200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**List[DocumentSendManualReminder200ResponseResultInner]**](DocumentSendManualReminder200ResponseResultInner.md) |  | [optional] 

## Example

```python
from pandadoc_client.models.document_send_manual_reminder200_response import DocumentSendManualReminder200Response

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentSendManualReminder200Response from a JSON string
document_send_manual_reminder200_response_instance = DocumentSendManualReminder200Response.from_json(json)
# print the JSON string representation of the object
print(DocumentSendManualReminder200Response.to_json())

# convert the object into a dict
document_send_manual_reminder200_response_dict = document_send_manual_reminder200_response_instance.to_dict()
# create an instance of DocumentSendManualReminder200Response from a dict
document_send_manual_reminder200_response_from_dict = DocumentSendManualReminder200Response.from_dict(document_send_manual_reminder200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


