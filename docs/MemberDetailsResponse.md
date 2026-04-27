# MemberDetailsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** | A unique identifier of the user in the organization. | [optional] 
**membership_id** | **str** | A unique identifier of the user in the workspace. | [optional] 
**email** | **str** | A user&#39;s email address. | [optional] 
**first_name** | **str** | A user&#39;s first name. | [optional] 
**last_name** | **str** | A user&#39;s last name. | [optional] 
**is_active** | **bool** | A boolean value that identifies if a member is active in the workspace. | [optional] 
**workspace** | **str** | A unique identifier of the user&#39;s current active workspace. | [optional] 
**workspace_name** | **str** | A name of the user&#39;s current active workspace. | [optional] 
**emails_verified** | **bool** | A boolean value that identifies if the email is verified. | [optional] 
**role** | **str** | A member&#39;s role in the workspace. | [optional] 
**user_license** | **str** | A user license in the organization. | [optional] 
**date_created** | **str** | A date when a member was added to the workspace. | [optional] 
**date_modified** | **str** | Last modified date of a member. | [optional] 

## Example

```python
from pandadoc_client.models.member_details_response import MemberDetailsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MemberDetailsResponse from a JSON string
member_details_response_instance = MemberDetailsResponse.from_json(json)
# print the JSON string representation of the object
print(MemberDetailsResponse.to_json())

# convert the object into a dict
member_details_response_dict = member_details_response_instance.to_dict()
# create an instance of MemberDetailsResponse from a dict
member_details_response_from_dict = MemberDetailsResponse.from_dict(member_details_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


