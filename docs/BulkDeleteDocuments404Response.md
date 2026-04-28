# BulkDeleteDocuments404Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**detail** | **str** |  | [optional] 

## Example

```python
from pandadoc_client.models.bulk_delete_documents404_response import BulkDeleteDocuments404Response

# TODO update the JSON string below
json = "{}"
# create an instance of BulkDeleteDocuments404Response from a JSON string
bulk_delete_documents404_response_instance = BulkDeleteDocuments404Response.from_json(json)
# print the JSON string representation of the object
print(BulkDeleteDocuments404Response.to_json())

# convert the object into a dict
bulk_delete_documents404_response_dict = bulk_delete_documents404_response_instance.to_dict()
# create an instance of BulkDeleteDocuments404Response from a dict
bulk_delete_documents404_response_from_dict = BulkDeleteDocuments404Response.from_dict(bulk_delete_documents404_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


