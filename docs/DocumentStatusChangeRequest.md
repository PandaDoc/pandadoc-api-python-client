# DocumentStatusChangeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**DocumentStatusChangeRequestStatusEnum**](DocumentStatusChangeRequestStatusEnum.md) |  | 
**note** | **str** | Provide “private notes” regarding the manual status change. | [optional] 
**notify_recipients** | **bool** | Send a notification email about the status change to all recipients. | [optional] 

## Example

```python
from pandadoc_client.models.document_status_change_request import DocumentStatusChangeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentStatusChangeRequest from a JSON string
document_status_change_request_instance = DocumentStatusChangeRequest.from_json(json)
# print the JSON string representation of the object
print(DocumentStatusChangeRequest.to_json())

# convert the object into a dict
document_status_change_request_dict = document_status_change_request_instance.to_dict()
# create an instance of DocumentStatusChangeRequest from a dict
document_status_change_request_from_dict = DocumentStatusChangeRequest.from_dict(document_status_change_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


