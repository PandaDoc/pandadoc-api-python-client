# ListNotarizationRequestsResponseResultsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | A unique identifier of the notarization request. | [optional] 
**status** | **str** | Current status of the notarization request. | [optional] 
**name** | **str** | Name of the notarization request. | [optional] 
**document_id** | **str** | A unique identifier of the document for notarization. | [optional] 
**date_created** | **datetime** | A date when a notarization request was created. | [optional] 
**date_started** | **datetime** | A date when a notarization session was started. | [optional] 
**date_completed** | **datetime** | A date when a notarization session was completed. | [optional] 
**created_by_user_id** | **str** | Public user id of the request creator. | [optional] 

## Example

```python
from pandadoc_client.models.list_notarization_requests_response_results_inner import ListNotarizationRequestsResponseResultsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ListNotarizationRequestsResponseResultsInner from a JSON string
list_notarization_requests_response_results_inner_instance = ListNotarizationRequestsResponseResultsInner.from_json(json)
# print the JSON string representation of the object
print(ListNotarizationRequestsResponseResultsInner.to_json())

# convert the object into a dict
list_notarization_requests_response_results_inner_dict = list_notarization_requests_response_results_inner_instance.to_dict()
# create an instance of ListNotarizationRequestsResponseResultsInner from a dict
list_notarization_requests_response_results_inner_from_dict = ListNotarizationRequestsResponseResultsInner.from_dict(list_notarization_requests_response_results_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


