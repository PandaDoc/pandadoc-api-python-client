# DocumentSendRequestSelectedApproversStepsInnerGroup

Group information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Group ID. | 
**type** | **str** | Group type. | 
**assignees** | [**List[DocumentSendRequestSelectedApproversStepsInnerGroupAssigneesInner]**](DocumentSendRequestSelectedApproversStepsInnerGroupAssigneesInner.md) | Assignees for the group. | 

## Example

```python
from pandadoc_client.models.document_send_request_selected_approvers_steps_inner_group import DocumentSendRequestSelectedApproversStepsInnerGroup

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentSendRequestSelectedApproversStepsInnerGroup from a JSON string
document_send_request_selected_approvers_steps_inner_group_instance = DocumentSendRequestSelectedApproversStepsInnerGroup.from_json(json)
# print the JSON string representation of the object
print(DocumentSendRequestSelectedApproversStepsInnerGroup.to_json())

# convert the object into a dict
document_send_request_selected_approvers_steps_inner_group_dict = document_send_request_selected_approvers_steps_inner_group_instance.to_dict()
# create an instance of DocumentSendRequestSelectedApproversStepsInnerGroup from a dict
document_send_request_selected_approvers_steps_inner_group_from_dict = DocumentSendRequestSelectedApproversStepsInnerGroup.from_dict(document_send_request_selected_approvers_steps_inner_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


