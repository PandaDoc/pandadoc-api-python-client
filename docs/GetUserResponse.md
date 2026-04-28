# GetUserResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** | A unique identifier of the user in the organization. | [optional] 
**email** | **str** | A user&#39;s email address. | [optional] 
**first_name** | **str** | A user&#39;s first name. | [optional] 
**last_name** | **str** | A user&#39;s last name. | [optional] 
**phone_number** | **str** | A user&#39;s phone number. | [optional] 
**license** | **str** | A user&#39;s license in the organization. | [optional] 
**is_organization_owner** | **bool** | Whether the user is the owner of the organization. | [optional] 
**workspaces** | [**List[GetUserResponseWorkspacesInner]**](GetUserResponseWorkspacesInner.md) |  | [optional] 

## Example

```python
from pandadoc_client.models.get_user_response import GetUserResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetUserResponse from a JSON string
get_user_response_instance = GetUserResponse.from_json(json)
# print the JSON string representation of the object
print(GetUserResponse.to_json())

# convert the object into a dict
get_user_response_dict = get_user_response_instance.to_dict()
# create an instance of GetUserResponse from a dict
get_user_response_from_dict = GetUserResponse.from_dict(get_user_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


