# UploadSectionStatusResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** |  | [optional] 
**document_uuid** | **str** |  | [optional] 
**status** | [**UploadSectionStatusEnum**](UploadSectionStatusEnum.md) |  | [optional] 
**name** | **str** |  | [optional] 
**sections_uuids** | **List[str]** |  | [optional] 
**date_created** | **str** |  | [optional] 
**date_modified** | **str** |  | [optional] 

## Example

```python
from pandadoc_client.models.upload_section_status_response import UploadSectionStatusResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UploadSectionStatusResponse from a JSON string
upload_section_status_response_instance = UploadSectionStatusResponse.from_json(json)
# print the JSON string representation of the object
print(UploadSectionStatusResponse.to_json())

# convert the object into a dict
upload_section_status_response_dict = upload_section_status_response_instance.to_dict()
# create an instance of UploadSectionStatusResponse from a dict
upload_section_status_response_from_dict = UploadSectionStatusResponse.from_dict(upload_section_status_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


