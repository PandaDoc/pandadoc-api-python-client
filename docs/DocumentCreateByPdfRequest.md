# DocumentCreateByPdfRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | Use a URL to specify the PDF. We support only URLs starting with https. | 
**recipients** | [**[DocumentCreateByPdfRequestRecipients]**](DocumentCreateByPdfRequestRecipients.md) | The list of recipients you&#39;re sending the document to. Every object must contain the &#x60;email&#x60; parameter. The &#x60;role&#x60;, &#x60;first_name&#x60; and &#x60;last_name&#x60; parameters are optional. If the &#x60;role&#x60; parameter is passed, a person is assigned all fields matching their corresponding role. If a role was not passed, a person receives a read-only link to view the document. If the &#x60;first_name&#x60; and &#x60;last_name&#x60; are not passed, the system does this 1. Creates a new contact, if none exists with the given &#x60;email&#x60;; or 2. Gets the existing contact with the given &#x60;email&#x60; that already exists. | 
**parse_form_fields** | **bool** | Set this parameter as &#x60;true&#x60; if you create a document from a PDF with form fields and as &#x60;false&#x60; if you upload a PDF with field tags. | 
**name** | **str** |  | [optional] 
**tags** | **[str]** | Mark your document with one or several tags. | [optional] 
**fields** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | If you are creating a document from a PDF with field tags, you can pass a list of the fields you&#39;d like to pre-fill in the document. If you are creating a document from a PDF with form fields, list all the fields and provide the &#x60;role&#x60; parameter so that the fields are assigned to document recipients. You can provide empty value for the field so that it&#39;s not pre-filled: \&quot;value\&quot;: \&quot;\&quot;.  | [optional] 
**metadata** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | You can pass arbitrary data in the key-value format to associate custom information with a document. This information is returned in any API requests for the document details by id. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


