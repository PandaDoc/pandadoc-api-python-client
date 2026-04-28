# SectionInfoResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**document_uuid** | **str** |  | [optional] 

## Example

```python
from pandadoc_client.models.section_info_response import SectionInfoResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SectionInfoResponse from a JSON string
section_info_response_instance = SectionInfoResponse.from_json(json)
# print the JSON string representation of the object
print(SectionInfoResponse.to_json())

# convert the object into a dict
section_info_response_dict = section_info_response_instance.to_dict()
# create an instance of SectionInfoResponse from a dict
section_info_response_from_dict = SectionInfoResponse.from_dict(section_info_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


