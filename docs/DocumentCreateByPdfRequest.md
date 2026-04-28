# DocumentCreateByPdfRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parse_form_fields** | **bool** | Set this parameter as &#x60;true&#x60; if you create a document from a PDF with form fields and as &#x60;false&#x60; if you upload a PDF with field tags. | [optional] 
**fields** | [**Dict[str, DocumentCreateByTemplateRequestFieldsValue]**](DocumentCreateByTemplateRequestFieldsValue.md) | Set specific values to the fields. This object maps merge field names to their corresponding values.  Each key represents a merge field name, and each value is an object containing the data to populate that field with. The structure allows you to pre-populate various field types including text inputs, checkboxes, dropdowns, and date fields.  **Key Points:** - Keys must match the exact merge field names from your template or file. - Values must be wrapped in an object with a &#x60;value&#x60; property. - Supported value types: string, number, boolean. - Date fields should use RFC 3339 format (e.g., &#39;2019-12-31T00:00:00.000Z&#39;). - Signature fields cannot be pre-filled.  **Example Usage:** - Text field: &#x60;\&quot;CustomerName\&quot;: {\&quot;value\&quot;: \&quot;John Doe\&quot;}&#x60; - Checkbox: &#x60;\&quot;AgreeToTerms\&quot;: {\&quot;value\&quot;: true}&#x60; - Date field: &#x60;\&quot;DeliveryDate\&quot;: {\&quot;value\&quot;: \&quot;2019-12-31T00:00:00.000Z\&quot;}&#x60;  | [optional] 
**name** | **str** | Name the document you are creating. | 
**folder_uuid** | **str** | ID of the folder where the created document should be stored. | [optional] 
**owner** | [**DocumentCreateByTemplateRequestOwner**](DocumentCreateByTemplateRequestOwner.md) |  | [optional] 
**recipients** | [**List[CreateDocumentActor]**](CreateDocumentActor.md) | The list of recipients to whom the document will be sent. Either &#x60;email&#x60; or &#x60;phone&#x60; is required. Specifying the &#x60;role&#x60; assigns all matching fields to the recipient or group. If &#x60;first_name&#x60; and &#x60;last_name&#x60; are not specified, the system looks them up in the workspace contacts list using the &#x60;email&#x60; or &#x60;phone number&#x60;. If &#x60;first_name&#x60; and &#x60;last_name&#x60; are provided, they override the existing contact&#39;s data. | [optional] 
**tokens** | [**List[DocumentCreateByTemplateRequestTokensInner]**](DocumentCreateByTemplateRequestTokensInner.md) | Also known as variables. Pass values for the variables in the template to render them into the created document or make them available for insertion later. | [optional] 
**metadata** | **object** | You can pass any data in a key-value format to associate it with a document. Searching by metadata is available in the List Documents endpoint and is also included in the Document Details response. | [optional] 
**tags** | **List[str]** | Mark your document with one or more tags. Tags are displayed in the UI, and you can filter by tags in the List Documents endpoint. | [optional] 

## Example

```python
from pandadoc_client.models.document_create_by_pdf_request import DocumentCreateByPdfRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentCreateByPdfRequest from a JSON string
document_create_by_pdf_request_instance = DocumentCreateByPdfRequest.from_json(json)
# print the JSON string representation of the object
print(DocumentCreateByPdfRequest.to_json())

# convert the object into a dict
document_create_by_pdf_request_dict = document_create_by_pdf_request_instance.to_dict()
# create an instance of DocumentCreateByPdfRequest from a dict
document_create_by_pdf_request_from_dict = DocumentCreateByPdfRequest.from_dict(document_create_by_pdf_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


