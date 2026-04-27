# AppendCLIDataResponseBlockMapping

Maps the original names of content blocks from the CLI to their new names in the document. Use the 'new_name' to target blocks in subsequent API calls.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tables** | [**List[AppendCLIDataResponseBlockMappingTablesInner]**](AppendCLIDataResponseBlockMappingTablesInner.md) | Mapping for Table blocks. | [optional] 
**pricing_tables** | [**List[AppendCLIDataResponseBlockMappingPricingTablesInner]**](AppendCLIDataResponseBlockMappingPricingTablesInner.md) | Mapping for Pricing Table blocks. | [optional] 
**images** | [**List[AppendCLIDataResponseBlockMappingImagesInner]**](AppendCLIDataResponseBlockMappingImagesInner.md) | Mapping for Image blocks. | [optional] 
**texts** | [**List[AppendCLIDataResponseBlockMappingTextsInner]**](AppendCLIDataResponseBlockMappingTextsInner.md) | Mapping for Text blocks. | [optional] 

## Example

```python
from pandadoc_client.models.append_cli_data_response_block_mapping import AppendCLIDataResponseBlockMapping

# TODO update the JSON string below
json = "{}"
# create an instance of AppendCLIDataResponseBlockMapping from a JSON string
append_cli_data_response_block_mapping_instance = AppendCLIDataResponseBlockMapping.from_json(json)
# print the JSON string representation of the object
print(AppendCLIDataResponseBlockMapping.to_json())

# convert the object into a dict
append_cli_data_response_block_mapping_dict = append_cli_data_response_block_mapping_instance.to_dict()
# create an instance of AppendCLIDataResponseBlockMapping from a dict
append_cli_data_response_block_mapping_from_dict = AppendCLIDataResponseBlockMapping.from_dict(append_cli_data_response_block_mapping_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


