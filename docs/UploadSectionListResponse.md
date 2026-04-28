# UploadSectionListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[UploadSectionListResponseResultsInner]**](UploadSectionListResponseResultsInner.md) |  | [optional] 

## Example

```python
from pandadoc_client.models.upload_section_list_response import UploadSectionListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UploadSectionListResponse from a JSON string
upload_section_list_response_instance = UploadSectionListResponse.from_json(json)
# print the JSON string representation of the object
print(UploadSectionListResponse.to_json())

# convert the object into a dict
upload_section_list_response_dict = upload_section_list_response_instance.to_dict()
# create an instance of UploadSectionListResponse from a dict
upload_section_list_response_from_dict = UploadSectionListResponse.from_dict(upload_section_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


