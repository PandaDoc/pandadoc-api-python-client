# BulkDeleteDocumentsRequestItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Document ID to delete. | 

## Example

```python
from pandadoc_client.models.bulk_delete_documents_request_item import BulkDeleteDocumentsRequestItem

# TODO update the JSON string below
json = "{}"
# create an instance of BulkDeleteDocumentsRequestItem from a JSON string
bulk_delete_documents_request_item_instance = BulkDeleteDocumentsRequestItem.from_json(json)
# print the JSON string representation of the object
print(BulkDeleteDocumentsRequestItem.to_json())

# convert the object into a dict
bulk_delete_documents_request_item_dict = bulk_delete_documents_request_item_instance.to_dict()
# create an instance of BulkDeleteDocumentsRequestItem from a dict
bulk_delete_documents_request_item_from_dict = BulkDeleteDocumentsRequestItem.from_dict(bulk_delete_documents_request_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


