# DocumentESignDisclosureResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_enabled** | **bool** | Indicates whether the ESign disclosure feature is enabled for the document. | [optional] 
**company_name** | **str** |  | [optional] 
**esign_disclosure_text** | **str** | Rich text (HTML) of the pre-configured ESign disclosure. | [optional] 

## Example

```python
from pandadoc_client.models.document_e_sign_disclosure_result import DocumentESignDisclosureResult

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentESignDisclosureResult from a JSON string
document_e_sign_disclosure_result_instance = DocumentESignDisclosureResult.from_json(json)
# print the JSON string representation of the object
print(DocumentESignDisclosureResult.to_json())

# convert the object into a dict
document_e_sign_disclosure_result_dict = document_e_sign_disclosure_result_instance.to_dict()
# create an instance of DocumentESignDisclosureResult from a dict
document_e_sign_disclosure_result_from_dict = DocumentESignDisclosureResult.from_dict(document_e_sign_disclosure_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


