# DocumentCreateByTemplateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**template_uuid** | **str** | The ID of a template you want to use. You can copy it from an in app template url such as &#x60;https://app.pandadoc.com/a/#/templates/{ID}/content&#x60;. A template ID is also obtained by listing templates. | 
**fields** | [**Dict[str, DocumentCreateByTemplateRequestFieldsValue]**](DocumentCreateByTemplateRequestFieldsValue.md) | Set specific values to the fields. This object maps merge field names to their corresponding values.  Each key represents a merge field name, and each value is an object containing the data to populate that field with. The structure allows you to pre-populate various field types including text inputs, checkboxes, dropdowns, and date fields.  **Key Points:** - Keys must match the exact merge field names from your template or file. - Values must be wrapped in an object with a &#x60;value&#x60; property. - Supported value types: string, number, boolean. - Date fields should use RFC 3339 format (e.g., &#39;2019-12-31T00:00:00.000Z&#39;). - Signature fields cannot be pre-filled.  **Example Usage:** - Text field: &#x60;\&quot;CustomerName\&quot;: {\&quot;value\&quot;: \&quot;John Doe\&quot;}&#x60; - Checkbox: &#x60;\&quot;AgreeToTerms\&quot;: {\&quot;value\&quot;: true}&#x60; - Date field: &#x60;\&quot;DeliveryDate\&quot;: {\&quot;value\&quot;: \&quot;2019-12-31T00:00:00.000Z\&quot;}&#x60;  | [optional] 
**images** | [**List[DocumentCreateByTemplateRequestImagesInner]**](DocumentCreateByTemplateRequestImagesInner.md) | You can pass a list of images to image blocks (one image in one block) for replacement. | [optional] 
**pricing_tables** | [**List[PricingTableRequest]**](PricingTableRequest.md) | Information to construct or populate a pricing table can be passed when creating a document. All product information must be passed when creating a new document. Products stored in PandaDoc cannot be used to populate table rows at this time. Keep in mind that this is an array, so multiple table objects can be passed to a document. Make sure that \&quot;Automatically add products to this table\&quot; is enabled in the PandaDoc template pricing tables you wish to populate via API. | [optional] 
**tables** | [**List[TableRequest]**](TableRequest.md) | Information to construct or populate a table can be passed when creating a document. Keep in mind that this is an array, so multiple table objects can be passed to a document. | [optional] 
**texts** | [**List[DocumentCreateByTemplateRequestTextsInner]**](DocumentCreateByTemplateRequestTextsInner.md) | You can pass a list of rich text values to pre-fill text blocks in a template. This is useful for inserting dynamic content like introductions or terms and conditions. Markdown is supported. | [optional] 
**detect_title_variables** | **bool** | Set this parameter as true if you want to detect title variables in the document. | [optional] 
**content_placeholders** | [**List[DocumentCreateByTemplateRequestContentPlaceholdersInner]**](DocumentCreateByTemplateRequestContentPlaceholdersInner.md) | You may replace Content Library Item Placeholders with a few content library items each and pre-fill fields/variables values, pricing table items, and assign recipients to roles from there. | [optional] 
**name** | **str** | Name the document you are creating. | [optional] 
**folder_uuid** | **str** | ID of the folder where the created document should be stored. | [optional] 
**owner** | [**DocumentCreateByTemplateRequestOwner**](DocumentCreateByTemplateRequestOwner.md) |  | [optional] 
**recipients** | [**List[CreateDocumentActor]**](CreateDocumentActor.md) | The list of recipients to whom the document will be sent. Either &#x60;email&#x60; or &#x60;phone&#x60; is required. Specifying the &#x60;role&#x60; assigns all matching fields to the recipient or group. If &#x60;first_name&#x60; and &#x60;last_name&#x60; are not specified, the system looks them up in the workspace contacts list using the &#x60;email&#x60; or &#x60;phone number&#x60;. If &#x60;first_name&#x60; and &#x60;last_name&#x60; are provided, they override the existing contact&#39;s data. | 
**tokens** | [**List[DocumentCreateByTemplateRequestTokensInner]**](DocumentCreateByTemplateRequestTokensInner.md) | Also known as variables. Pass values for the variables in the template to render them into the created document or make them available for insertion later. | [optional] 
**metadata** | **object** | You can pass any data in a key-value format to associate it with a document. Searching by metadata is available in the List Documents endpoint and is also included in the Document Details response. | [optional] 
**tags** | **List[str]** | Mark your document with one or more tags. Tags are displayed in the UI, and you can filter by tags in the List Documents endpoint. | [optional] 

## Example

```python
from pandadoc_client.models.document_create_by_template_request import DocumentCreateByTemplateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentCreateByTemplateRequest from a JSON string
document_create_by_template_request_instance = DocumentCreateByTemplateRequest.from_json(json)
# print the JSON string representation of the object
print(DocumentCreateByTemplateRequest.to_json())

# convert the object into a dict
document_create_by_template_request_dict = document_create_by_template_request_instance.to_dict()
# create an instance of DocumentCreateByTemplateRequest from a dict
document_create_by_template_request_from_dict = DocumentCreateByTemplateRequest.from_dict(document_create_by_template_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


