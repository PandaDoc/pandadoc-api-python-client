# DocumentSummaryResponse

Summary response envelope. The `type` field echoes the `type` query parameter. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**DocumentSummaryType**](DocumentSummaryType.md) |  | 
**summary** | **str** | Summary text for the requested summary type.  | 

## Example

```python
from pandadoc_client.models.document_summary_response import DocumentSummaryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentSummaryResponse from a JSON string
document_summary_response_instance = DocumentSummaryResponse.from_json(json)
# print the JSON string representation of the object
print(DocumentSummaryResponse.to_json())

# convert the object into a dict
document_summary_response_dict = document_summary_response_instance.to_dict()
# create an instance of DocumentSummaryResponse from a dict
document_summary_response_from_dict = DocumentSummaryResponse.from_dict(document_summary_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


