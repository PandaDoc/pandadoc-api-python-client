# NotarizationRequestDetailsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | A unique identifier of the notarization request. | [optional] 
**status** | **str** | Current status of the notarization request. | [optional] 
**document_id** | **str** | A unique identifier of the document for notarization. | [optional] 
**date_created** | **datetime** | A date when a notarization request was created. | [optional] 
**date_started** | **datetime** | A date when a notarization session was started. | [optional] 
**date_completed** | **datetime** | A date when a notarization session was completed. | [optional] 
**created_by** | [**NotarizationRequestDetailsResponseCreatedBy**](NotarizationRequestDetailsResponseCreatedBy.md) |  | [optional] 
**invitees** | [**List[NotarizationRequestDetailsResponseInviteesInner]**](NotarizationRequestDetailsResponseInviteesInner.md) |  | [optional] 
**signed_documents** | [**List[NotarizationRequestDetailsResponseSignedDocumentsInner]**](NotarizationRequestDetailsResponseSignedDocumentsInner.md) |  | [optional] 
**recording** | [**NotarizationRequestDetailsResponseRecording**](NotarizationRequestDetailsResponseRecording.md) |  | [optional] 
**termination_reason** | **str** | The reason why the notarization session was terminated. Only present when the request status is INCOMPLETE. | [optional] 
**termination_details** | **str** | Additional details about the termination reason provided by the notary. Only present when the request status is INCOMPLETE. | [optional] 

## Example

```python
from pandadoc_client.models.notarization_request_details_response import NotarizationRequestDetailsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NotarizationRequestDetailsResponse from a JSON string
notarization_request_details_response_instance = NotarizationRequestDetailsResponse.from_json(json)
# print the JSON string representation of the object
print(NotarizationRequestDetailsResponse.to_json())

# convert the object into a dict
notarization_request_details_response_dict = notarization_request_details_response_instance.to_dict()
# create an instance of NotarizationRequestDetailsResponse from a dict
notarization_request_details_response_from_dict = NotarizationRequestDetailsResponse.from_dict(notarization_request_details_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


