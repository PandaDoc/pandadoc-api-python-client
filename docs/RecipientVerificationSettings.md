# RecipientVerificationSettings

To set up recipient verification, fill in verification_place and specify the type: passcode_verification, phone_verification, kba_verification or id_verification. - For passcode_verification, provide the passcode. - For phone_verification, provide the phone_number. - For kba_verification and id_verification, set the enabled parameter to true. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**verification_place** | [**RecipientVerificationPlaceEnum**](RecipientVerificationPlaceEnum.md) |  | [optional] 
**passcode_verification** | [**RecipientVerificationSettingsPasscodeVerification**](RecipientVerificationSettingsPasscodeVerification.md) |  | [optional] 
**phone_verification** | [**RecipientVerificationSettingsPhoneVerification**](RecipientVerificationSettingsPhoneVerification.md) |  | [optional] 
**kba_verification** | [**RecipientVerificationSettingsKbaVerification**](RecipientVerificationSettingsKbaVerification.md) |  | [optional] 
**id_verification** | [**RecipientVerificationSettingsIdVerification**](RecipientVerificationSettingsIdVerification.md) |  | [optional] 

## Example

```python
from pandadoc_client.models.recipient_verification_settings import RecipientVerificationSettings

# TODO update the JSON string below
json = "{}"
# create an instance of RecipientVerificationSettings from a JSON string
recipient_verification_settings_instance = RecipientVerificationSettings.from_json(json)
# print the JSON string representation of the object
print(RecipientVerificationSettings.to_json())

# convert the object into a dict
recipient_verification_settings_dict = recipient_verification_settings_instance.to_dict()
# create an instance of RecipientVerificationSettings from a dict
recipient_verification_settings_from_dict = RecipientVerificationSettings.from_dict(recipient_verification_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


