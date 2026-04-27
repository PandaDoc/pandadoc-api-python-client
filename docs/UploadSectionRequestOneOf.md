# UploadSectionRequestOneOf


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parse_form_fields** | **bool** | Set this parameter as &#x60;true&#x60; if you create a document from a PDF with form fields and as &#x60;false&#x60; if you upload a PDF with field tags. | [optional] 
**fields** | **object** | If you are upload a section from a PDF with field tags, you can pass a list of the fields you&#39;d like to pre-fill in the document. If you are upload a section from a PDF with form fields, list all the fields and provide the &#x60;role&#x60; parameter so that the fields are assigned to document recipients. You can provide empty value for the field so that it&#39;s not pre-filled: \&quot;value\&quot;: \&quot;\&quot;. Please note Signature field can&#39;t be pre-filled.  | [optional] 
**name** | **str** | Name the document you are creating. | [optional] 
**recipients** | [**List[CreateDocumentActor]**](CreateDocumentActor.md) | The list of recipients you&#39;re sending the document to. Every object must contain the &#x60;email&#x60; parameter. The &#x60;role&#x60;, &#x60;first_name&#x60; and &#x60;last_name&#x60; parameters are optional. If the &#x60;role&#x60; parameter is passed, a person is assigned all fields matching their corresponding role. If a role was not passed, a person receives a read-only link to view the document. If the &#x60;first_name&#x60; and &#x60;last_name&#x60; are not passed, the system does this 1. Creates a new contact, if none exists with the given &#x60;email&#x60;; or 2. Gets the existing contact with the given &#x60;email&#x60; that already exists. | 
**tokens** | [**List[DocumentUpdateRequestTokensInner]**](DocumentUpdateRequestTokensInner.md) | You may pass a list of tokens/values to pre-fill tokens (variables) used in a template. Name is a token (variable) name in a template. Value is a real value you would like to replace a token (variable) with.  | [optional] 
**tags** | **List[str]** | Mark your document with one or several tags. | [optional] 
**url** | **str** | Secure (HTTPS) and publicly accessible URL to the PDF document. | 

## Example

```python
from pandadoc_client.models.upload_section_request_one_of import UploadSectionRequestOneOf

# TODO update the JSON string below
json = "{}"
# create an instance of UploadSectionRequestOneOf from a JSON string
upload_section_request_one_of_instance = UploadSectionRequestOneOf.from_json(json)
# print the JSON string representation of the object
print(UploadSectionRequestOneOf.to_json())

# convert the object into a dict
upload_section_request_one_of_dict = upload_section_request_one_of_instance.to_dict()
# create an instance of UploadSectionRequestOneOf from a dict
upload_section_request_one_of_from_dict = UploadSectionRequestOneOf.from_dict(upload_section_request_one_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


