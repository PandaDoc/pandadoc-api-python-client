# DocumentAuditTrailResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | Total number of audit trail entries available. | [optional] 
**results** | [**List[DocumentAuditTrailResponseResultsInner]**](DocumentAuditTrailResponseResultsInner.md) | List of audit trail entries returned for the current page. | [optional] 

## Example

```python
from pandadoc_client.models.document_audit_trail_response import DocumentAuditTrailResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentAuditTrailResponse from a JSON string
document_audit_trail_response_instance = DocumentAuditTrailResponse.from_json(json)
# print the JSON string representation of the object
print(DocumentAuditTrailResponse.to_json())

# convert the object into a dict
document_audit_trail_response_dict = document_audit_trail_response_instance.to_dict()
# create an instance of DocumentAuditTrailResponse from a dict
document_audit_trail_response_from_dict = DocumentAuditTrailResponse.from_dict(document_audit_trail_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


