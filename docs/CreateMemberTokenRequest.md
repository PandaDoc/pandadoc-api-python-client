# CreateMemberTokenRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lifetime** | **int** | Token lifetime in seconds. | [optional] [default to 3600]

## Example

```python
from pandadoc_client.models.create_member_token_request import CreateMemberTokenRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateMemberTokenRequest from a JSON string
create_member_token_request_instance = CreateMemberTokenRequest.from_json(json)
# print the JSON string representation of the object
print(CreateMemberTokenRequest.to_json())

# convert the object into a dict
create_member_token_request_dict = create_member_token_request_instance.to_dict()
# create an instance of CreateMemberTokenRequest from a dict
create_member_token_request_from_dict = CreateMemberTokenRequest.from_dict(create_member_token_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


