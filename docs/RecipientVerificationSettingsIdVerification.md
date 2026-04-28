# RecipientVerificationSettingsIdVerification

Sets the ID verification.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** |  | [optional] 

## Example

```python
from pandadoc_client.models.recipient_verification_settings_id_verification import RecipientVerificationSettingsIdVerification

# TODO update the JSON string below
json = "{}"
# create an instance of RecipientVerificationSettingsIdVerification from a JSON string
recipient_verification_settings_id_verification_instance = RecipientVerificationSettingsIdVerification.from_json(json)
# print the JSON string representation of the object
print(RecipientVerificationSettingsIdVerification.to_json())

# convert the object into a dict
recipient_verification_settings_id_verification_dict = recipient_verification_settings_id_verification_instance.to_dict()
# create an instance of RecipientVerificationSettingsIdVerification from a dict
recipient_verification_settings_id_verification_from_dict = RecipientVerificationSettingsIdVerification.from_dict(recipient_verification_settings_id_verification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


