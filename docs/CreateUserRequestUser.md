# CreateUserRequestUser

User info

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | [optional] 
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**phone_number** | **str** |  | [optional] 

## Example

```python
from pandadoc_client.models.create_user_request_user import CreateUserRequestUser

# TODO update the JSON string below
json = "{}"
# create an instance of CreateUserRequestUser from a JSON string
create_user_request_user_instance = CreateUserRequestUser.from_json(json)
# print the JSON string representation of the object
print(CreateUserRequestUser.to_json())

# convert the object into a dict
create_user_request_user_dict = create_user_request_user_instance.to_dict()
# create an instance of CreateUserRequestUser from a dict
create_user_request_user_from_dict = CreateUserRequestUser.from_dict(create_user_request_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


