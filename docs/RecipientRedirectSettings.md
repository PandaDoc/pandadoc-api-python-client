# RecipientRedirectSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_enabled** | **bool** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from pandadoc_client.models.recipient_redirect_settings import RecipientRedirectSettings

# TODO update the JSON string below
json = "{}"
# create an instance of RecipientRedirectSettings from a JSON string
recipient_redirect_settings_instance = RecipientRedirectSettings.from_json(json)
# print the JSON string representation of the object
print(RecipientRedirectSettings.to_json())

# convert the object into a dict
recipient_redirect_settings_dict = recipient_redirect_settings_instance.to_dict()
# create an instance of RecipientRedirectSettings from a dict
recipient_redirect_settings_from_dict = RecipientRedirectSettings.from_dict(recipient_redirect_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


