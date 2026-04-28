# AppendCLIDataRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cli** | [**AppendCLIDataRequestCli**](AppendCLIDataRequestCli.md) |  | [optional] 

## Example

```python
from pandadoc_client.models.append_cli_data_request import AppendCLIDataRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AppendCLIDataRequest from a JSON string
append_cli_data_request_instance = AppendCLIDataRequest.from_json(json)
# print the JSON string representation of the object
print(AppendCLIDataRequest.to_json())

# convert the object into a dict
append_cli_data_request_dict = append_cli_data_request_instance.to_dict()
# create an instance of AppendCLIDataRequest from a dict
append_cli_data_request_from_dict = AppendCLIDataRequest.from_dict(append_cli_data_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


