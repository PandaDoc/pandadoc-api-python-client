# ListNotaries403Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**details** | [**List[ListLogsV2400ResponseDetailsInner]**](ListLogsV2400ResponseDetailsInner.md) |  | [optional] 

## Example

```python
from pandadoc_client.models.list_notaries403_response import ListNotaries403Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListNotaries403Response from a JSON string
list_notaries403_response_instance = ListNotaries403Response.from_json(json)
# print the JSON string representation of the object
print(ListNotaries403Response.to_json())

# convert the object into a dict
list_notaries403_response_dict = list_notaries403_response_instance.to_dict()
# create an instance of ListNotaries403Response from a dict
list_notaries403_response_from_dict = ListNotaries403Response.from_dict(list_notaries403_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


