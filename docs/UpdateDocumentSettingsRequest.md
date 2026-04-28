# UpdateDocumentSettingsRequest

Document settings update request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**language** | [**DocumentLanguageEnum**](DocumentLanguageEnum.md) |  | [optional] 
**qualified_electronic_signature** | **bool** | Indicates whether the document requires a Qualified Electronic Signature (QES) during the signing process. If &#x60;true&#x60;, signers must complete the document using a third-party qualified electronic signature provider according to supported verification rules.  | [optional] 
**expires_in** | **int** | Document expiration in days. Minimum is 1 day.  | [optional] 

## Example

```python
from pandadoc_client.models.update_document_settings_request import UpdateDocumentSettingsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateDocumentSettingsRequest from a JSON string
update_document_settings_request_instance = UpdateDocumentSettingsRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateDocumentSettingsRequest.to_json())

# convert the object into a dict
update_document_settings_request_dict = update_document_settings_request_instance.to_dict()
# create an instance of UpdateDocumentSettingsRequest from a dict
update_document_settings_request_from_dict = UpdateDocumentSettingsRequest.from_dict(update_document_settings_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


