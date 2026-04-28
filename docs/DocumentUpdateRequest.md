# DocumentUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the document. | [optional] 
**recipients** | [**List[UpdateDocumentActor]**](UpdateDocumentActor.md) | The list of recipients you&#39;re sending the document to. The ID or email are required. If the ID is passed, an existing recipient will be updated. If the email is passed, a new recipient will be added to CC. | [optional] 
**fields** | [**Dict[str, DocumentUpdateRequestFieldValue]**](DocumentUpdateRequestFieldValue.md) | Set specific values to the fields. This object maps merge field names to their corresponding values.  Each key represents a merge field name, and each value is an object containing the data to populate that field with. The structure allows you to pre-populate various field types including text inputs, checkboxes, dropdowns, and date fields.  **Key Points:** - Keys must match the exact merge field names from your template or file. - Values must be wrapped in an object with a &#x60;value&#x60; property. - Supported value types: string, number, boolean. - Date fields should use RFC 3339 format (e.g., &#39;2019-12-31T00:00:00.000Z&#39;). - Signature fields cannot be pre-filled.  **Example Usage:** - Text field: &#x60;\&quot;CustomerName\&quot;: {\&quot;value\&quot;: \&quot;John Doe\&quot;}&#x60; - Checkbox: &#x60;\&quot;AgreeToTerms\&quot;: {\&quot;value\&quot;: true}&#x60; - Date field: &#x60;\&quot;DeliveryDate\&quot;: {\&quot;value\&quot;: \&quot;2019-12-31T00:00:00.000Z\&quot;}&#x60;  | [optional] 
**tokens** | [**List[DocumentUpdateRequestTokensInner]**](DocumentUpdateRequestTokensInner.md) | Create or initialize multiple variables with their values using tokens/values list. | [optional] 
**tags** | **List[str]** | Mark your document with one or several tags. | [optional] 
**metadata** | **object** | You can pass arbitrary data in the key-value format to associate custom information with a document. This information is returned in any API requests for the document details by id. If metadata exists in a document then the value will be updated. Otherwise, metadata will be added to the document. | [optional] 
**pricing_tables** | [**List[PricingTableRequest]**](PricingTableRequest.md) |  | [optional] 
**tables** | [**List[TableRequest]**](TableRequest.md) |  | [optional] 
**images** | [**List[DocumentUpdateRequestImagesInner]**](DocumentUpdateRequestImagesInner.md) | You can pass a list of images to image blocks (one image in one block) for replacement. | [optional] 
**texts** | [**List[DocumentUpdateRequestTextsInner]**](DocumentUpdateRequestTextsInner.md) | You can pass a list of texts to text blocks for replacement. | [optional] 

## Example

```python
from pandadoc_client.models.document_update_request import DocumentUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentUpdateRequest from a JSON string
document_update_request_instance = DocumentUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(DocumentUpdateRequest.to_json())

# convert the object into a dict
document_update_request_dict = document_update_request_instance.to_dict()
# create an instance of DocumentUpdateRequest from a dict
document_update_request_from_dict = DocumentUpdateRequest.from_dict(document_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


