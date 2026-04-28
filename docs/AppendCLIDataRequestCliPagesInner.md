# AppendCLIDataRequestCliPagesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**index** | **int** | The index of the CLI&#39;s page you want to change in a result document during appending the CLI | [optional] 
**name** | **str** | The name you want to apply to the CLI&#39;s page in a result document during appending the CLI | [optional] 

## Example

```python
from pandadoc_client.models.append_cli_data_request_cli_pages_inner import AppendCLIDataRequestCliPagesInner

# TODO update the JSON string below
json = "{}"
# create an instance of AppendCLIDataRequestCliPagesInner from a JSON string
append_cli_data_request_cli_pages_inner_instance = AppendCLIDataRequestCliPagesInner.from_json(json)
# print the JSON string representation of the object
print(AppendCLIDataRequestCliPagesInner.to_json())

# convert the object into a dict
append_cli_data_request_cli_pages_inner_dict = append_cli_data_request_cli_pages_inner_instance.to_dict()
# create an instance of AppendCLIDataRequestCliPagesInner from a dict
append_cli_data_request_cli_pages_inner_from_dict = AppendCLIDataRequestCliPagesInner.from_dict(append_cli_data_request_cli_pages_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


