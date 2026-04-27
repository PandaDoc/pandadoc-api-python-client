# CreateNotarizationRequestInvitation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Optional message for invitation email. | [optional] 
**invitees** | [**List[CreateNotarizationRequestInvitationInviteesInner]**](CreateNotarizationRequestInvitationInviteesInner.md) |  | [optional] 

## Example

```python
from pandadoc_client.models.create_notarization_request_invitation import CreateNotarizationRequestInvitation

# TODO update the JSON string below
json = "{}"
# create an instance of CreateNotarizationRequestInvitation from a JSON string
create_notarization_request_invitation_instance = CreateNotarizationRequestInvitation.from_json(json)
# print the JSON string representation of the object
print(CreateNotarizationRequestInvitation.to_json())

# convert the object into a dict
create_notarization_request_invitation_dict = create_notarization_request_invitation_instance.to_dict()
# create an instance of CreateNotarizationRequestInvitation from a dict
create_notarization_request_invitation_from_dict = CreateNotarizationRequestInvitation.from_dict(create_notarization_request_invitation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


