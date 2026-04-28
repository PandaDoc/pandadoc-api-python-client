# NotarizationRequestDetailsResponseInviteesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | A unique identifier of the invitee. | [optional] 
**email** | **str** | A invitee&#39;s email address. | [optional] 
**first_name** | **str** | A invitee&#39;s first name. | [optional] 
**last_name** | **str** | A invitee&#39;s last name. | [optional] 

## Example

```python
from pandadoc_client.models.notarization_request_details_response_invitees_inner import NotarizationRequestDetailsResponseInviteesInner

# TODO update the JSON string below
json = "{}"
# create an instance of NotarizationRequestDetailsResponseInviteesInner from a JSON string
notarization_request_details_response_invitees_inner_instance = NotarizationRequestDetailsResponseInviteesInner.from_json(json)
# print the JSON string representation of the object
print(NotarizationRequestDetailsResponseInviteesInner.to_json())

# convert the object into a dict
notarization_request_details_response_invitees_inner_dict = notarization_request_details_response_invitees_inner_instance.to_dict()
# create an instance of NotarizationRequestDetailsResponseInviteesInner from a dict
notarization_request_details_response_invitees_inner_from_dict = NotarizationRequestDetailsResponseInviteesInner.from_dict(notarization_request_details_response_invitees_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


