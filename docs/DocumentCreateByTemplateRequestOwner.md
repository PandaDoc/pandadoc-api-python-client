# DocumentCreateByTemplateRequestOwner

The owner of the document. Pass either `email` or `membership_id` of the user in the workspace.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | [optional] 
**membership_id** | **str** |  | [optional] 

## Example

```python
from pandadoc_client.models.document_create_by_template_request_owner import DocumentCreateByTemplateRequestOwner

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentCreateByTemplateRequestOwner from a JSON string
document_create_by_template_request_owner_instance = DocumentCreateByTemplateRequestOwner.from_json(json)
# print the JSON string representation of the object
print(DocumentCreateByTemplateRequestOwner.to_json())

# convert the object into a dict
document_create_by_template_request_owner_dict = document_create_by_template_request_owner_instance.to_dict()
# create an instance of DocumentCreateByTemplateRequestOwner from a dict
document_create_by_template_request_owner_from_dict = DocumentCreateByTemplateRequestOwner.from_dict(document_create_by_template_request_owner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


