# DocumentCreateByMarkdownRequest

Request body for creating a document from an uploaded Markdown file.  > **Alpha:** Markdown file upload is currently in alpha. This functionality may change or be removed without notice. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name the document you are creating. | 
**folder_uuid** | **str** | ID of the folder where the created document should be stored. | [optional] 
**owner** | [**DocumentCreateByTemplateRequestOwner**](DocumentCreateByTemplateRequestOwner.md) |  | [optional] 
**recipients** | [**List[CreateDocumentActor]**](CreateDocumentActor.md) | The list of recipients to whom the document will be sent. Either &#x60;email&#x60; or &#x60;phone&#x60; is required. Specifying the &#x60;role&#x60; assigns all matching fields to the recipient or group. If &#x60;first_name&#x60; and &#x60;last_name&#x60; are not specified, the system looks them up in the workspace contacts list using the &#x60;email&#x60; or &#x60;phone number&#x60;. If &#x60;first_name&#x60; and &#x60;last_name&#x60; are provided, they override the existing contact&#39;s data. | [optional] 
**tokens** | [**List[DocumentCreateByTemplateRequestTokensInner]**](DocumentCreateByTemplateRequestTokensInner.md) | Also known as variables. Pass values for the variables in the template to render them into the created document or make them available for insertion later. | [optional] 
**metadata** | **object** | You can pass any data in a key-value format to associate it with a document. Searching by metadata is available in the List Documents endpoint and is also included in the Document Details response. | [optional] 
**tags** | **List[str]** | Mark your document with one or more tags. Tags are displayed in the UI, and you can filter by tags in the List Documents endpoint. | [optional] 
**fields_mapping** | **Dict[str, List[str]]** | Map recipient roles to document field identifiers. Each key is a recipient role name (must match a &#x60;role&#x60; defined in &#x60;recipients&#x60;), and the value is a list of field identifiers to assign to that recipient.  Field identifiers reference fields created from the Markdown content. The system validates that all specified field identifiers exist in the document and that all referenced roles are present in the &#x60;recipients&#x60; list.  | [optional] 

## Example

```python
from pandadoc_client.models.document_create_by_markdown_request import DocumentCreateByMarkdownRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentCreateByMarkdownRequest from a JSON string
document_create_by_markdown_request_instance = DocumentCreateByMarkdownRequest.from_json(json)
# print the JSON string representation of the object
print(DocumentCreateByMarkdownRequest.to_json())

# convert the object into a dict
document_create_by_markdown_request_dict = document_create_by_markdown_request_instance.to_dict()
# create an instance of DocumentCreateByMarkdownRequest from a dict
document_create_by_markdown_request_from_dict = DocumentCreateByMarkdownRequest.from_dict(document_create_by_markdown_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


