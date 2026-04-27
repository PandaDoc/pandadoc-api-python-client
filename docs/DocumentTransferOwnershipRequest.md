# DocumentTransferOwnershipRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**membership_id** | **str** | A unique identifier of a workspace member. | [optional] 

## Example

```python
from pandadoc_client.models.document_transfer_ownership_request import DocumentTransferOwnershipRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentTransferOwnershipRequest from a JSON string
document_transfer_ownership_request_instance = DocumentTransferOwnershipRequest.from_json(json)
# print the JSON string representation of the object
print(DocumentTransferOwnershipRequest.to_json())

# convert the object into a dict
document_transfer_ownership_request_dict = document_transfer_ownership_request_instance.to_dict()
# create an instance of DocumentTransferOwnershipRequest from a dict
document_transfer_ownership_request_from_dict = DocumentTransferOwnershipRequest.from_dict(document_transfer_ownership_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


