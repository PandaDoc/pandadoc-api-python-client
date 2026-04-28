# ListUsersResponseResultsInner


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
**workspaces** | [**List[ListUsersResponseResultsInnerWorkspacesInner]**](ListUsersResponseResultsInnerWorkspacesInner.md) |  | [optional] 

## Example

```python
from pandadoc_client.models.list_users_response_results_inner import ListUsersResponseResultsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ListUsersResponseResultsInner from a JSON string
list_users_response_results_inner_instance = ListUsersResponseResultsInner.from_json(json)
# print the JSON string representation of the object
print(ListUsersResponseResultsInner.to_json())

# convert the object into a dict
list_users_response_results_inner_dict = list_users_response_results_inner_instance.to_dict()
# create an instance of ListUsersResponseResultsInner from a dict
list_users_response_results_inner_from_dict = ListUsersResponseResultsInner.from_dict(list_users_response_results_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


