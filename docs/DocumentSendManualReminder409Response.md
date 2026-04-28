# DocumentSendManualReminder409Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**info_message** | **str** |  | [optional] 

## Example

```python
from pandadoc_client.models.document_send_manual_reminder409_response import DocumentSendManualReminder409Response

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentSendManualReminder409Response from a JSON string
document_send_manual_reminder409_response_instance = DocumentSendManualReminder409Response.from_json(json)
# print the JSON string representation of the object
print(DocumentSendManualReminder409Response.to_json())

# convert the object into a dict
document_send_manual_reminder409_response_dict = document_send_manual_reminder409_response_instance.to_dict()
# create an instance of DocumentSendManualReminder409Response from a dict
document_send_manual_reminder409_response_from_dict = DocumentSendManualReminder409Response.from_dict(document_send_manual_reminder409_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


