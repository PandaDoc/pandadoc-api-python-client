# ListLogsV2400Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**details** | [**List[ListLogsV2400ResponseDetailsInner]**](ListLogsV2400ResponseDetailsInner.md) |  | [optional] 

## Example

```python
from pandadoc_client.models.list_logs_v2400_response import ListLogsV2400Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListLogsV2400Response from a JSON string
list_logs_v2400_response_instance = ListLogsV2400Response.from_json(json)
# print the JSON string representation of the object
print(ListLogsV2400Response.to_json())

# convert the object into a dict
list_logs_v2400_response_dict = list_logs_v2400_response_instance.to_dict()
# create an instance of ListLogsV2400Response from a dict
list_logs_v2400_response_from_dict = ListLogsV2400Response.from_dict(list_logs_v2400_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


