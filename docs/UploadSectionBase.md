# UploadSectionBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name the document you are creating. | [optional] 
**recipients** | [**List[CreateDocumentActor]**](CreateDocumentActor.md) | The list of recipients you&#39;re sending the document to. Every object must contain the &#x60;email&#x60; parameter. The &#x60;role&#x60;, &#x60;first_name&#x60; and &#x60;last_name&#x60; parameters are optional. If the &#x60;role&#x60; parameter is passed, a person is assigned all fields matching their corresponding role. If a role was not passed, a person receives a read-only link to view the document. If the &#x60;first_name&#x60; and &#x60;last_name&#x60; are not passed, the system does this 1. Creates a new contact, if none exists with the given &#x60;email&#x60;; or 2. Gets the existing contact with the given &#x60;email&#x60; that already exists. | 
**tokens** | [**List[DocumentUpdateRequestTokensInner]**](DocumentUpdateRequestTokensInner.md) | You may pass a list of tokens/values to pre-fill tokens (variables) used in a template. Name is a token (variable) name in a template. Value is a real value you would like to replace a token (variable) with.  | [optional] 
**tags** | **List[str]** | Mark your document with one or several tags. | [optional] 

## Example

```python
from pandadoc_client.models.upload_section_base import UploadSectionBase

# TODO update the JSON string below
json = "{}"
# create an instance of UploadSectionBase from a JSON string
upload_section_base_instance = UploadSectionBase.from_json(json)
# print the JSON string representation of the object
print(UploadSectionBase.to_json())

# convert the object into a dict
upload_section_base_dict = upload_section_base_instance.to_dict()
# create an instance of UploadSectionBase from a dict
upload_section_base_from_dict = UploadSectionBase.from_dict(upload_section_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


