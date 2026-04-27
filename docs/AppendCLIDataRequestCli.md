# AppendCLIDataRequestCli

Settings to append a CLI to a document, with ability to change some parameters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | CLI ID to append to the first section. | 
**pages** | [**List[AppendCLIDataRequestCliPagesInner]**](AppendCLIDataRequestCliPagesInner.md) | The list of the CLI&#39;s pages you want to change in a result document | [optional] 

## Example

```python
from pandadoc_client.models.append_cli_data_request_cli import AppendCLIDataRequestCli

# TODO update the JSON string below
json = "{}"
# create an instance of AppendCLIDataRequestCli from a JSON string
append_cli_data_request_cli_instance = AppendCLIDataRequestCli.from_json(json)
# print the JSON string representation of the object
print(AppendCLIDataRequestCli.to_json())

# convert the object into a dict
append_cli_data_request_cli_dict = append_cli_data_request_cli_instance.to_dict()
# create an instance of AppendCLIDataRequestCli from a dict
append_cli_data_request_cli_from_dict = AppendCLIDataRequestCli.from_dict(append_cli_data_request_cli_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


