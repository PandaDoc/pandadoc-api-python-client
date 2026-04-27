# ListNotarizationRequestsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[ListNotarizationRequestsResponseResultsInner]**](ListNotarizationRequestsResponseResultsInner.md) | Array of notarization request objects. | [optional] 
**count** | **int** | Total number of notarization requests matching the criteria. | [optional] 

## Example

```python
from pandadoc_client.models.list_notarization_requests_response import ListNotarizationRequestsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListNotarizationRequestsResponse from a JSON string
list_notarization_requests_response_instance = ListNotarizationRequestsResponse.from_json(json)
# print the JSON string representation of the object
print(ListNotarizationRequestsResponse.to_json())

# convert the object into a dict
list_notarization_requests_response_dict = list_notarization_requests_response_instance.to_dict()
# create an instance of ListNotarizationRequestsResponse from a dict
list_notarization_requests_response_from_dict = ListNotarizationRequestsResponse.from_dict(list_notarization_requests_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


