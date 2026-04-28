# RecipientVerificationSettingsPhoneVerification

Sets the phone number to send a passcode to.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**phone_number** | **str** | A phone number to send a passcode to. | 

## Example

```python
from pandadoc_client.models.recipient_verification_settings_phone_verification import RecipientVerificationSettingsPhoneVerification

# TODO update the JSON string below
json = "{}"
# create an instance of RecipientVerificationSettingsPhoneVerification from a JSON string
recipient_verification_settings_phone_verification_instance = RecipientVerificationSettingsPhoneVerification.from_json(json)
# print the JSON string representation of the object
print(RecipientVerificationSettingsPhoneVerification.to_json())

# convert the object into a dict
recipient_verification_settings_phone_verification_dict = recipient_verification_settings_phone_verification_instance.to_dict()
# create an instance of RecipientVerificationSettingsPhoneVerification from a dict
recipient_verification_settings_phone_verification_from_dict = RecipientVerificationSettingsPhoneVerification.from_dict(recipient_verification_settings_phone_verification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


