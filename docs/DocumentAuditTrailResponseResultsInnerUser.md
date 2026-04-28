# DocumentAuditTrailResponseResultsInnerUser

The user who triggered the action.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the user. | [optional] 
**email** | **str** | User&#39;s email address. | [optional] 

## Example

```python
from pandadoc_client.models.document_audit_trail_response_results_inner_user import DocumentAuditTrailResponseResultsInnerUser

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentAuditTrailResponseResultsInnerUser from a JSON string
document_audit_trail_response_results_inner_user_instance = DocumentAuditTrailResponseResultsInnerUser.from_json(json)
# print the JSON string representation of the object
print(DocumentAuditTrailResponseResultsInnerUser.to_json())

# convert the object into a dict
document_audit_trail_response_results_inner_user_dict = document_audit_trail_response_results_inner_user_instance.to_dict()
# create an instance of DocumentAuditTrailResponseResultsInnerUser from a dict
document_audit_trail_response_results_inner_user_from_dict = DocumentAuditTrailResponseResultsInnerUser.from_dict(document_audit_trail_response_results_inner_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


