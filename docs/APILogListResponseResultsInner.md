# APILogListResponseResultsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**status** | **int** |  | [optional] 
**request_time** | **str** |  | [optional] 
**response_time** | **str** |  | [optional] 

## Example

```python
from pandadoc_client.models.api_log_list_response_results_inner import APILogListResponseResultsInner

# TODO update the JSON string below
json = "{}"
# create an instance of APILogListResponseResultsInner from a JSON string
api_log_list_response_results_inner_instance = APILogListResponseResultsInner.from_json(json)
# print the JSON string representation of the object
print(APILogListResponseResultsInner.to_json())

# convert the object into a dict
api_log_list_response_results_inner_dict = api_log_list_response_results_inner_instance.to_dict()
# create an instance of APILogListResponseResultsInner from a dict
api_log_list_response_results_inner_from_dict = APILogListResponseResultsInner.from_dict(api_log_list_response_results_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


