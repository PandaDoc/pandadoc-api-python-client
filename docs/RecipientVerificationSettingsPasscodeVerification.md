# RecipientVerificationSettingsPasscodeVerification

Sets the passcode.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**passcode** | **str** | Document passcode. | 

## Example

```python
from pandadoc_client.models.recipient_verification_settings_passcode_verification import RecipientVerificationSettingsPasscodeVerification

# TODO update the JSON string below
json = "{}"
# create an instance of RecipientVerificationSettingsPasscodeVerification from a JSON string
recipient_verification_settings_passcode_verification_instance = RecipientVerificationSettingsPasscodeVerification.from_json(json)
# print the JSON string representation of the object
print(RecipientVerificationSettingsPasscodeVerification.to_json())

# convert the object into a dict
recipient_verification_settings_passcode_verification_dict = recipient_verification_settings_passcode_verification_instance.to_dict()
# create an instance of RecipientVerificationSettingsPasscodeVerification from a dict
recipient_verification_settings_passcode_verification_from_dict = RecipientVerificationSettingsPasscodeVerification.from_dict(recipient_verification_settings_passcode_verification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


