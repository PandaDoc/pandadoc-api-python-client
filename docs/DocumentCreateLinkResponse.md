# DocumentCreateLinkResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The session ID. | [optional] 
**expires_at** | **str** | The date and time when the session will expire. | [optional] 

## Example

```python
from pandadoc_client.models.document_create_link_response import DocumentCreateLinkResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentCreateLinkResponse from a JSON string
document_create_link_response_instance = DocumentCreateLinkResponse.from_json(json)
# print the JSON string representation of the object
print(DocumentCreateLinkResponse.to_json())

# convert the object into a dict
document_create_link_response_dict = document_create_link_response_instance.to_dict()
# create an instance of DocumentCreateLinkResponse from a dict
document_create_link_response_from_dict = DocumentCreateLinkResponse.from_dict(document_create_link_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


