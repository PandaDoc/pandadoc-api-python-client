# UploadSectionListResponseResultsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from pandadoc_client.models.upload_section_list_response_results_inner import UploadSectionListResponseResultsInner

# TODO update the JSON string below
json = "{}"
# create an instance of UploadSectionListResponseResultsInner from a JSON string
upload_section_list_response_results_inner_instance = UploadSectionListResponseResultsInner.from_json(json)
# print the JSON string representation of the object
print(UploadSectionListResponseResultsInner.to_json())

# convert the object into a dict
upload_section_list_response_results_inner_dict = upload_section_list_response_results_inner_instance.to_dict()
# create an instance of UploadSectionListResponseResultsInner from a dict
upload_section_list_response_results_inner_from_dict = UploadSectionListResponseResultsInner.from_dict(upload_section_list_response_results_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


