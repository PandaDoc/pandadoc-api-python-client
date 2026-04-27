# CreateNotarizationResponseInviteesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | A unique identifier of the invitee. | [optional] 
**email** | **str** | A invitee&#39;s email address. | [optional] 
**first_name** | **str** | A invitee&#39;s first name. | [optional] 
**last_name** | **str** | A invitee&#39;s last name. | [optional] 
**notarization_link** | **str** | A secure link to join a notarization request. | [optional] 

## Example

```python
from pandadoc_client.models.create_notarization_response_invitees_inner import CreateNotarizationResponseInviteesInner

# TODO update the JSON string below
json = "{}"
# create an instance of CreateNotarizationResponseInviteesInner from a JSON string
create_notarization_response_invitees_inner_instance = CreateNotarizationResponseInviteesInner.from_json(json)
# print the JSON string representation of the object
print(CreateNotarizationResponseInviteesInner.to_json())

# convert the object into a dict
create_notarization_response_invitees_inner_dict = create_notarization_response_invitees_inner_instance.to_dict()
# create an instance of CreateNotarizationResponseInviteesInner from a dict
create_notarization_response_invitees_inner_from_dict = CreateNotarizationResponseInviteesInner.from_dict(create_notarization_response_invitees_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


