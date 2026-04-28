# UploadSectionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**document_uuid** | **str** |  | [optional] 
**status** | [**UploadSectionStatusEnum**](UploadSectionStatusEnum.md) |  | [optional] 
**date_created** | **str** |  | [optional] 
**date_modified** | **str** |  | [optional] 
**date_completed** | **str** |  | [optional] 
**info_message** | **str** |  | [optional] 

## Example

```python
from pandadoc_client.models.upload_section_response import UploadSectionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UploadSectionResponse from a JSON string
upload_section_response_instance = UploadSectionResponse.from_json(json)
# print the JSON string representation of the object
print(UploadSectionResponse.to_json())

# convert the object into a dict
upload_section_response_dict = upload_section_response_instance.to_dict()
# create an instance of UploadSectionResponse from a dict
upload_section_response_from_dict = UploadSectionResponse.from_dict(upload_section_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


