# DocumentSendRequestSelectedApproversStepsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Step ID. | 
**group** | [**DocumentSendRequestSelectedApproversStepsInnerGroup**](DocumentSendRequestSelectedApproversStepsInnerGroup.md) |  | 

## Example

```python
from pandadoc_client.models.document_send_request_selected_approvers_steps_inner import DocumentSendRequestSelectedApproversStepsInner

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentSendRequestSelectedApproversStepsInner from a JSON string
document_send_request_selected_approvers_steps_inner_instance = DocumentSendRequestSelectedApproversStepsInner.from_json(json)
# print the JSON string representation of the object
print(DocumentSendRequestSelectedApproversStepsInner.to_json())

# convert the object into a dict
document_send_request_selected_approvers_steps_inner_dict = document_send_request_selected_approvers_steps_inner_instance.to_dict()
# create an instance of DocumentSendRequestSelectedApproversStepsInner from a dict
document_send_request_selected_approvers_steps_inner_from_dict = DocumentSendRequestSelectedApproversStepsInner.from_dict(document_send_request_selected_approvers_steps_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


