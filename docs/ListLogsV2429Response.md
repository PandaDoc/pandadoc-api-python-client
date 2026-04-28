# ListLogsV2429Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**details** | [**List[ListLogsV2400ResponseDetailsInner]**](ListLogsV2400ResponseDetailsInner.md) |  | [optional] 

## Example

```python
from pandadoc_client.models.list_logs_v2429_response import ListLogsV2429Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListLogsV2429Response from a JSON string
list_logs_v2429_response_instance = ListLogsV2429Response.from_json(json)
# print the JSON string representation of the object
print(ListLogsV2429Response.to_json())

# convert the object into a dict
list_logs_v2429_response_dict = list_logs_v2429_response_instance.to_dict()
# create an instance of ListLogsV2429Response from a dict
list_logs_v2429_response_from_dict = ListLogsV2429Response.from_dict(list_logs_v2429_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


