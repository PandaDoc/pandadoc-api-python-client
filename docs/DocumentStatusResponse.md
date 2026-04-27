# DocumentStatusResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**date_created** | **str** |  | [optional] 
**date_modified** | **str** |  | [optional] 
**date_completed** | **str** |  | [optional] 
**expiration_date** | **str** |  | [optional] 
**version** | **str** |  | [optional] 
**uuid** | **str** |  | [optional] 

## Example

```python
from pandadoc_client.models.document_status_response import DocumentStatusResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentStatusResponse from a JSON string
document_status_response_instance = DocumentStatusResponse.from_json(json)
# print the JSON string representation of the object
print(DocumentStatusResponse.to_json())

# convert the object into a dict
document_status_response_dict = document_status_response_instance.to_dict()
# create an instance of DocumentStatusResponse from a dict
document_status_response_from_dict = DocumentStatusResponse.from_dict(document_status_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


