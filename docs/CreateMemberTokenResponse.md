# CreateMemberTokenResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token** | **str** |  | [optional] 

## Example

```python
from pandadoc_client.models.create_member_token_response import CreateMemberTokenResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateMemberTokenResponse from a JSON string
create_member_token_response_instance = CreateMemberTokenResponse.from_json(json)
# print the JSON string representation of the object
print(CreateMemberTokenResponse.to_json())

# convert the object into a dict
create_member_token_response_dict = create_member_token_response_instance.to_dict()
# create an instance of CreateMemberTokenResponse from a dict
create_member_token_response_from_dict = CreateMemberTokenResponse.from_dict(create_member_token_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


