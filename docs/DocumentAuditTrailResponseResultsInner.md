# DocumentAuditTrailResponseResultsInner

Represents a single audit trail event for a document.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the audit trail entry. | [optional] 
**user** | [**DocumentAuditTrailResponseResultsInnerUser**](DocumentAuditTrailResponseResultsInnerUser.md) |  | [optional] 
**action** | **int** | Numeric code representing the type of action performed. Possible values:  | Integer Value | String Representation | |---------------|---------------------------------------------| | 1 | new document | | 2 | new revision | | 3 | approval request | | 4 | approved | | 5 | rejected | | 6 | sent | | 7 | completed by all | | 8 | viewed | | 9 | completed | | 10 | waiting pay | | 11 | paid | | 12 | forwarded | | 13 | expired | | 14 | bank account submitted | | 15 | bank account verified | | 16 | payment submitted | | 17 | payment failed | | 18 | completed manually | | 19 | expired manually | | 20 | paid manually | | 21 | approval deleted | | 22 | approval forced | | 23 | reassigned | | 24 | recipient edited | | 25 | recipient added | | 26 | recipient deleted | | 27 | declined manually | | 28 | approval step skipped | | 29 | suggest edits | | 43 | declined | | 44 | partly paid | | 45 | partly paid manually | | 47 | recipient verification with kba passed | | 48 | recipient verification with id passed | | 49 | recipient verification with text sms passed | | 50 | recipient verification with passcode passed | | 51 | recipient verification with kba failed | | 52 | recipient verification with id failed | | 53 | recipient verification with text sms failed | | 54 | recipient verification with passcode failed | | 55 | recipient signed with QES | | 56 | QES completed | | 57 | recipient QES attempt started | | 58 | recipient QES attempt expired | | 59 | Optional item in quote selected | | 60 | Optional item in quote deselected | | 61 | Item quantity in quote changed | | 62 | Item quantity in pricing table changed | | 63 | Optional item in pricing table selected | | 64 | Optional item in pricing table deselected | | 65 | Section item in pricing table selected (one of) | | 66 | Optional section in quote selected | | 67 | Optional section in quote deselected | | 68 | Section quantity in quote changed |  | [optional] 
**reason** | **str** | Optional reason or explanation for the action. | [optional] 
**date_created** | **datetime** | Timestamp when the action was performed (in ISO 8601 format). | [optional] 
**ip_address** | **str** | The IP address from which the action was performed. If a sandbox API key is used, this will be \&quot;hidden\&quot;. | [optional] 

## Example

```python
from pandadoc_client.models.document_audit_trail_response_results_inner import DocumentAuditTrailResponseResultsInner

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentAuditTrailResponseResultsInner from a JSON string
document_audit_trail_response_results_inner_instance = DocumentAuditTrailResponseResultsInner.from_json(json)
# print the JSON string representation of the object
print(DocumentAuditTrailResponseResultsInner.to_json())

# convert the object into a dict
document_audit_trail_response_results_inner_dict = document_audit_trail_response_results_inner_instance.to_dict()
# create an instance of DocumentAuditTrailResponseResultsInner from a dict
document_audit_trail_response_results_inner_from_dict = DocumentAuditTrailResponseResultsInner.from_dict(document_audit_trail_response_results_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


