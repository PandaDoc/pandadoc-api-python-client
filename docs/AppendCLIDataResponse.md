# AppendCLIDataResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cli** | [**AppendCLIDataResponseCli**](AppendCLIDataResponseCli.md) |  | [optional] 
**block_mapping** | [**AppendCLIDataResponseBlockMapping**](AppendCLIDataResponseBlockMapping.md) |  | [optional] 

## Example

```python
from pandadoc_client.models.append_cli_data_response import AppendCLIDataResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AppendCLIDataResponse from a JSON string
append_cli_data_response_instance = AppendCLIDataResponse.from_json(json)
# print the JSON string representation of the object
print(AppendCLIDataResponse.to_json())

# convert the object into a dict
append_cli_data_response_dict = append_cli_data_response_instance.to_dict()
# create an instance of AppendCLIDataResponse from a dict
append_cli_data_response_from_dict = AppendCLIDataResponse.from_dict(append_cli_data_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


