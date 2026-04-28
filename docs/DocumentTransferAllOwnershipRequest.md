# DocumentTransferAllOwnershipRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**from_membership_id** | **str** | A unique identifier of a workspace member from whom you want to transfer ownership. | [optional] 
**to_membership_id** | **str** | A unique identifier of a workspace member to whom you want to transfer ownership. | [optional] 

## Example

```python
from pandadoc_client.models.document_transfer_all_ownership_request import DocumentTransferAllOwnershipRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentTransferAllOwnershipRequest from a JSON string
document_transfer_all_ownership_request_instance = DocumentTransferAllOwnershipRequest.from_json(json)
# print the JSON string representation of the object
print(DocumentTransferAllOwnershipRequest.to_json())

# convert the object into a dict
document_transfer_all_ownership_request_dict = document_transfer_all_ownership_request_instance.to_dict()
# create an instance of DocumentTransferAllOwnershipRequest from a dict
document_transfer_all_ownership_request_from_dict = DocumentTransferAllOwnershipRequest.from_dict(document_transfer_all_ownership_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


