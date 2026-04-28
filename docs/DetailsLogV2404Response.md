# DetailsLogV2404Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**details** | [**List[ListLogsV2400ResponseDetailsInner]**](ListLogsV2400ResponseDetailsInner.md) |  | [optional] 

## Example

```python
from pandadoc_client.models.details_log_v2404_response import DetailsLogV2404Response

# TODO update the JSON string below
json = "{}"
# create an instance of DetailsLogV2404Response from a JSON string
details_log_v2404_response_instance = DetailsLogV2404Response.from_json(json)
# print the JSON string representation of the object
print(DetailsLogV2404Response.to_json())

# convert the object into a dict
details_log_v2404_response_dict = details_log_v2404_response_instance.to_dict()
# create an instance of DetailsLogV2404Response from a dict
details_log_v2404_response_from_dict = DetailsLogV2404Response.from_dict(details_log_v2404_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


