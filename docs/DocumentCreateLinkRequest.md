# DocumentCreateLinkRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recipient** | **str** | Email address of the person who will receive access to the document. | 
**lifetime** | **float** | The duration in seconds for which the document link will remain valid. The link will expire and become inaccessible after this time period. For security, we recommend setting the lifetime to less than one year (e.g., &#x60;\&quot;lifetime\&quot;: 31535999&#x60;). If not specified, the default value is 1 hour (3600 seconds).  | [optional] [default to 3600]

## Example

```python
from pandadoc_client.models.document_create_link_request import DocumentCreateLinkRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentCreateLinkRequest from a JSON string
document_create_link_request_instance = DocumentCreateLinkRequest.from_json(json)
# print the JSON string representation of the object
print(DocumentCreateLinkRequest.to_json())

# convert the object into a dict
document_create_link_request_dict = document_create_link_request_instance.to_dict()
# create an instance of DocumentCreateLinkRequest from a dict
document_create_link_request_from_dict = DocumentCreateLinkRequest.from_dict(document_create_link_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


