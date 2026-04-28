# ListLogsV2400ResponseDetailsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | 
**pointer** | **str** | JSON Pointer. | [optional] 
**data** | **Dict[str, object]** | Details data. | [optional] 

## Example

```python
from pandadoc_client.models.list_logs_v2400_response_details_inner import ListLogsV2400ResponseDetailsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ListLogsV2400ResponseDetailsInner from a JSON string
list_logs_v2400_response_details_inner_instance = ListLogsV2400ResponseDetailsInner.from_json(json)
# print the JSON string representation of the object
print(ListLogsV2400ResponseDetailsInner.to_json())

# convert the object into a dict
list_logs_v2400_response_details_inner_dict = list_logs_v2400_response_details_inner_instance.to_dict()
# create an instance of ListLogsV2400ResponseDetailsInner from a dict
list_logs_v2400_response_details_inner_from_dict = ListLogsV2400ResponseDetailsInner.from_dict(list_logs_v2400_response_details_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


