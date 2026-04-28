# DocumentSendRequestSelectedApprovers

Configuration for selected approvers.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**steps** | [**List[DocumentSendRequestSelectedApproversStepsInner]**](DocumentSendRequestSelectedApproversStepsInner.md) | Approval steps. | [optional] 

## Example

```python
from pandadoc_client.models.document_send_request_selected_approvers import DocumentSendRequestSelectedApprovers

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentSendRequestSelectedApprovers from a JSON string
document_send_request_selected_approvers_instance = DocumentSendRequestSelectedApprovers.from_json(json)
# print the JSON string representation of the object
print(DocumentSendRequestSelectedApprovers.to_json())

# convert the object into a dict
document_send_request_selected_approvers_dict = document_send_request_selected_approvers_instance.to_dict()
# create an instance of DocumentSendRequestSelectedApprovers from a dict
document_send_request_selected_approvers_from_dict = DocumentSendRequestSelectedApprovers.from_dict(document_send_request_selected_approvers_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


