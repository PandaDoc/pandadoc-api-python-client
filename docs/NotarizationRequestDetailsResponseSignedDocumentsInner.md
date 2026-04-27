# NotarizationRequestDetailsResponseSignedDocumentsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | Secure URL to download signed PDF document. | [optional] 
**document_name** | **str** | A signer document name. | [optional] 
**size** | **float** | A signer document size in bytes. | [optional] 
**document_type** | **str** | A type of the signed document. | [optional] 

## Example

```python
from pandadoc_client.models.notarization_request_details_response_signed_documents_inner import NotarizationRequestDetailsResponseSignedDocumentsInner

# TODO update the JSON string below
json = "{}"
# create an instance of NotarizationRequestDetailsResponseSignedDocumentsInner from a JSON string
notarization_request_details_response_signed_documents_inner_instance = NotarizationRequestDetailsResponseSignedDocumentsInner.from_json(json)
# print the JSON string representation of the object
print(NotarizationRequestDetailsResponseSignedDocumentsInner.to_json())

# convert the object into a dict
notarization_request_details_response_signed_documents_inner_dict = notarization_request_details_response_signed_documents_inner_instance.to_dict()
# create an instance of NotarizationRequestDetailsResponseSignedDocumentsInner from a dict
notarization_request_details_response_signed_documents_inner_from_dict = NotarizationRequestDetailsResponseSignedDocumentsInner.from_dict(notarization_request_details_response_signed_documents_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


