# APILogListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[APILogListResponseResultsInner]**](APILogListResponseResultsInner.md) |  | [optional] 

## Example

```python
from pandadoc_client.models.api_log_list_response import APILogListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of APILogListResponse from a JSON string
api_log_list_response_instance = APILogListResponse.from_json(json)
# print the JSON string representation of the object
print(APILogListResponse.to_json())

# convert the object into a dict
api_log_list_response_dict = api_log_list_response_instance.to_dict()
# create an instance of APILogListResponse from a dict
api_log_list_response_from_dict = APILogListResponse.from_dict(api_log_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


