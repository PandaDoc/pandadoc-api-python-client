# OAuth2AccessTokenResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token** | **str** |  | [optional] 
**token_type** | **str** |  | [optional] 
**expires_in** | **float** |  | [optional] 
**scope** | **str** |  | [optional] 
**refresh_token** | **str** |  | [optional] 

## Example

```python
from pandadoc_client.models.o_auth2_access_token_response import OAuth2AccessTokenResponse

# TODO update the JSON string below
json = "{}"
# create an instance of OAuth2AccessTokenResponse from a JSON string
o_auth2_access_token_response_instance = OAuth2AccessTokenResponse.from_json(json)
# print the JSON string representation of the object
print(OAuth2AccessTokenResponse.to_json())

# convert the object into a dict
o_auth2_access_token_response_dict = o_auth2_access_token_response_instance.to_dict()
# create an instance of OAuth2AccessTokenResponse from a dict
o_auth2_access_token_response_from_dict = OAuth2AccessTokenResponse.from_dict(o_auth2_access_token_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


