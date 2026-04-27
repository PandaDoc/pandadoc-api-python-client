# DocumentCreateResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**status** | [**DocumentStatusEnum**](DocumentStatusEnum.md) |  | [optional] 
**date_created** | **str** |  | [optional] 
**date_modified** | **str** |  | [optional] 
**expiration_date** | **str** |  | [optional] 
**version** | **str** |  | [optional] 
**uuid** | **str** |  | [optional] 
**links** | [**List[DocumentCreateResponseLinksInner]**](DocumentCreateResponseLinksInner.md) |  | [optional] 
**info_message** | **str** |  | [optional] 

## Example

```python
from pandadoc_client.models.document_create_response import DocumentCreateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentCreateResponse from a JSON string
document_create_response_instance = DocumentCreateResponse.from_json(json)
# print the JSON string representation of the object
print(DocumentCreateResponse.to_json())

# convert the object into a dict
document_create_response_dict = document_create_response_instance.to_dict()
# create an instance of DocumentCreateResponse from a dict
document_create_response_from_dict = DocumentCreateResponse.from_dict(document_create_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


