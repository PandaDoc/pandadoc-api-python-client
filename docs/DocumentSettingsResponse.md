# DocumentSettingsResponse

Document settings response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**language** | [**DocumentLanguageEnum**](DocumentLanguageEnum.md) |  | 
**qualified_electronic_signature** | **bool** | Indicates whether the document requires a Qualified Electronic Signature (QES) during the signing process. If &#x60;true&#x60;, signers must complete the document using a third-party qualified electronic signature provider according to supported verification rules.  | 
**expires_in** | **int** | Document expiration in days. If not explicitly set, defaults to the system default expiration.  | 

## Example

```python
from pandadoc_client.models.document_settings_response import DocumentSettingsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentSettingsResponse from a JSON string
document_settings_response_instance = DocumentSettingsResponse.from_json(json)
# print the JSON string representation of the object
print(DocumentSettingsResponse.to_json())

# convert the object into a dict
document_settings_response_dict = document_settings_response_instance.to_dict()
# create an instance of DocumentSettingsResponse from a dict
document_settings_response_from_dict = DocumentSettingsResponse.from_dict(document_settings_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


