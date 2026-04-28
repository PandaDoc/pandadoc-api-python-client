# AppendCLIDataResponseCli

Settings of the appended to a document CLI. Name property can be different from what you passed if there were collisions

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | CLI ID appended to the first section. | 
**pages** | [**List[AppendCLIDataResponseCliPagesInner]**](AppendCLIDataResponseCliPagesInner.md) | The list of the CLI&#39;s pages you have changed in a result document | [optional] 

## Example

```python
from pandadoc_client.models.append_cli_data_response_cli import AppendCLIDataResponseCli

# TODO update the JSON string below
json = "{}"
# create an instance of AppendCLIDataResponseCli from a JSON string
append_cli_data_response_cli_instance = AppendCLIDataResponseCli.from_json(json)
# print the JSON string representation of the object
print(AppendCLIDataResponseCli.to_json())

# convert the object into a dict
append_cli_data_response_cli_dict = append_cli_data_response_cli_instance.to_dict()
# create an instance of AppendCLIDataResponseCli from a dict
append_cli_data_response_cli_from_dict = AppendCLIDataResponseCli.from_dict(append_cli_data_response_cli_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


