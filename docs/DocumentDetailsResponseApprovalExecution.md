# DocumentDetailsResponseApprovalExecution

Document approval execution.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**document_uuid** | **str** | Decoded uuid of related RegularDocument instance. | [optional] 
**revision_number** | **int** | Consequent number of revision for related RegularDocument. | [optional] 

## Example

```python
from pandadoc_client.models.document_details_response_approval_execution import DocumentDetailsResponseApprovalExecution

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentDetailsResponseApprovalExecution from a JSON string
document_details_response_approval_execution_instance = DocumentDetailsResponseApprovalExecution.from_json(json)
# print the JSON string representation of the object
print(DocumentDetailsResponseApprovalExecution.to_json())

# convert the object into a dict
document_details_response_approval_execution_dict = document_details_response_approval_execution_instance.to_dict()
# create an instance of DocumentDetailsResponseApprovalExecution from a dict
document_details_response_approval_execution_from_dict = DocumentDetailsResponseApprovalExecution.from_dict(document_details_response_approval_execution_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


