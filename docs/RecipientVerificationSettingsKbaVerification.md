# RecipientVerificationSettingsKbaVerification

Sets the KBA verification.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time_limit_sec** | **int** |  | [optional] 
**score_threshold** | **int** |  | [optional] 
**max_attempts_count** | **int** |  | [optional] 

## Example

```python
from pandadoc_client.models.recipient_verification_settings_kba_verification import RecipientVerificationSettingsKbaVerification

# TODO update the JSON string below
json = "{}"
# create an instance of RecipientVerificationSettingsKbaVerification from a JSON string
recipient_verification_settings_kba_verification_instance = RecipientVerificationSettingsKbaVerification.from_json(json)
# print the JSON string representation of the object
print(RecipientVerificationSettingsKbaVerification.to_json())

# convert the object into a dict
recipient_verification_settings_kba_verification_dict = recipient_verification_settings_kba_verification_instance.to_dict()
# create an instance of RecipientVerificationSettingsKbaVerification from a dict
recipient_verification_settings_kba_verification_from_dict = RecipientVerificationSettingsKbaVerification.from_dict(recipient_verification_settings_kba_verification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


