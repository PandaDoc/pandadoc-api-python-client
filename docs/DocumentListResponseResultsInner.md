# DocumentListResponseResultsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**date_created** | **str** |  | [optional] 
**date_modified** | **str** |  | [optional] 
**date_completed** | **str** |  | [optional] 
**expiration_date** | **str** |  | [optional] 
**version** | **str** |  | [optional] 

## Example

```python
from pandadoc_client.models.document_list_response_results_inner import DocumentListResponseResultsInner

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentListResponseResultsInner from a JSON string
document_list_response_results_inner_instance = DocumentListResponseResultsInner.from_json(json)
# print the JSON string representation of the object
print(DocumentListResponseResultsInner.to_json())

# convert the object into a dict
document_list_response_results_inner_dict = document_list_response_results_inner_instance.to_dict()
# create an instance of DocumentListResponseResultsInner from a dict
document_list_response_results_inner_from_dict = DocumentListResponseResultsInner.from_dict(document_list_response_results_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


