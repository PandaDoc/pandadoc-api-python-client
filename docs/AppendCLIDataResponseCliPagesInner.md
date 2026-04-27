# AppendCLIDataResponseCliPagesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**index** | **int** | The index of the CLI&#39;s page you have changed in a result document during appending the CLI | [optional] 
**name** | **str** | The real name in the page. It can be different from the one you passed if there were collisions (e.g. you appended the same CLI twice with the same names) | [optional] 

## Example

```python
from pandadoc_client.models.append_cli_data_response_cli_pages_inner import AppendCLIDataResponseCliPagesInner

# TODO update the JSON string below
json = "{}"
# create an instance of AppendCLIDataResponseCliPagesInner from a JSON string
append_cli_data_response_cli_pages_inner_instance = AppendCLIDataResponseCliPagesInner.from_json(json)
# print the JSON string representation of the object
print(AppendCLIDataResponseCliPagesInner.to_json())

# convert the object into a dict
append_cli_data_response_cli_pages_inner_dict = append_cli_data_response_cli_pages_inner_instance.to_dict()
# create an instance of AppendCLIDataResponseCliPagesInner from a dict
append_cli_data_response_cli_pages_inner_from_dict = AppendCLIDataResponseCliPagesInner.from_dict(append_cli_data_response_cli_pages_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


