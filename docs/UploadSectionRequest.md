# UploadSectionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parse_form_fields** | **bool** | Set this parameter as &#x60;true&#x60; if you create a document from a PDF with form fields and as &#x60;false&#x60; if you upload a PDF with field tags. | [optional] 
**fields** | **object** | You can pass a list of fields/values to pre-fill fields used in a template. Note that the Signature field can&#39;t be pre-filled. Field values with the same merge id will override field values of the whole document by default, unless you set the merge_field_scope&#x3D;upload query parameter. | [optional] 
**name** | **str** | Name the document you are creating. | [optional] 
**recipients** | [**List[CreateDocumentActor]**](CreateDocumentActor.md) | The list of recipients you&#39;re sending the document to. Every object must contain the &#x60;email&#x60; parameter. The &#x60;role&#x60;, &#x60;first_name&#x60; and &#x60;last_name&#x60; parameters are optional. If the &#x60;role&#x60; parameter is passed, a person is assigned all fields matching their corresponding role. If a role was not passed, a person receives a read-only link to view the document. If the &#x60;first_name&#x60; and &#x60;last_name&#x60; are not passed, the system does this 1. Creates a new contact, if none exists with the given &#x60;email&#x60;; or 2. Gets the existing contact with the given &#x60;email&#x60; that already exists. | 
**tokens** | [**List[DocumentUpdateRequestTokensInner]**](DocumentUpdateRequestTokensInner.md) | You may pass a list of tokens/values to pre-fill tokens (variables) used in a template. Name is a token (variable) name in a template. Value is a real value you would like to replace a token (variable) with.  | [optional] 
**tags** | **List[str]** | Mark your document with one or several tags. | [optional] 
**url** | **str** | Secure (HTTPS) and publicly accessible URL to the PDF document. | 
**template_uuid** | **str** | The ID of a template you want to use. You can copy it from an in app template url such as &#x60;https://app.pandadoc.com/a/#/templates/{ID}/content&#x60;. A template ID is also obtained by listing templates. | 
**pricing_tables** | [**List[PricingTableRequest]**](PricingTableRequest.md) | Information to construct or populate a pricing table can be passed when creating a document. All product information must be passed when creating a new document. Products stored in PandaDoc cannot be used to populate table rows at this time. Keep in mind that this is an array, so multiple table objects can be passed to a document. Make sure that \&quot;Automatically add products to this table\&quot; is enabled in the PandaDoc template pricing tables you wish to populate via API. Each pricing table must have a unique name to populate it with data correctly. | [optional] 
**content_placeholders** | [**List[UploadSectionByTemplateRequestAllOfContentPlaceholders]**](UploadSectionByTemplateRequestAllOfContentPlaceholders.md) | You may replace Content Library Item Placeholders with a few content library items each and pre-fill fields/variables values, pricing table items, and assign recipients to roles from there. | [optional] 

## Example

```python
from pandadoc_client.models.upload_section_request import UploadSectionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UploadSectionRequest from a JSON string
upload_section_request_instance = UploadSectionRequest.from_json(json)
# print the JSON string representation of the object
print(UploadSectionRequest.to_json())

# convert the object into a dict
upload_section_request_dict = upload_section_request_instance.to_dict()
# create an instance of UploadSectionRequest from a dict
upload_section_request_from_dict = UploadSectionRequest.from_dict(upload_section_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


