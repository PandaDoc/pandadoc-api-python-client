# BulkDeleteDocumentsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **List[str]** | Document IDs that were deleted, in the same order as processed by the API. | 

## Example

```python
from pandadoc_client.models.bulk_delete_documents_response import BulkDeleteDocumentsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BulkDeleteDocumentsResponse from a JSON string
bulk_delete_documents_response_instance = BulkDeleteDocumentsResponse.from_json(json)
# print the JSON string representation of the object
print(BulkDeleteDocumentsResponse.to_json())

# convert the object into a dict
bulk_delete_documents_response_dict = bulk_delete_documents_response_instance.to_dict()
# create an instance of BulkDeleteDocumentsResponse from a dict
bulk_delete_documents_response_from_dict = BulkDeleteDocumentsResponse.from_dict(bulk_delete_documents_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


