# AppendCLIDataResponseBlockMappingTextsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**original_name** | **str** | The name of the block in the source Content Library Item. | [optional] 
**new_name** | **str** | The new, unique name of the block in the document after appending. | [optional] 

## Example

```python
from pandadoc_client.models.append_cli_data_response_block_mapping_texts_inner import AppendCLIDataResponseBlockMappingTextsInner

# TODO update the JSON string below
json = "{}"
# create an instance of AppendCLIDataResponseBlockMappingTextsInner from a JSON string
append_cli_data_response_block_mapping_texts_inner_instance = AppendCLIDataResponseBlockMappingTextsInner.from_json(json)
# print the JSON string representation of the object
print(AppendCLIDataResponseBlockMappingTextsInner.to_json())

# convert the object into a dict
append_cli_data_response_block_mapping_texts_inner_dict = append_cli_data_response_block_mapping_texts_inner_instance.to_dict()
# create an instance of AppendCLIDataResponseBlockMappingTextsInner from a dict
append_cli_data_response_block_mapping_texts_inner_from_dict = AppendCLIDataResponseBlockMappingTextsInner.from_dict(append_cli_data_response_block_mapping_texts_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


