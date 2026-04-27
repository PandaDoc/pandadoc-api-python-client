# RecipientsGroupAssignedToAllOfMembers


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 

## Example

```python
from pandadoc_client.models.recipients_group_assigned_to_all_of_members import RecipientsGroupAssignedToAllOfMembers

# TODO update the JSON string below
json = "{}"
# create an instance of RecipientsGroupAssignedToAllOfMembers from a JSON string
recipients_group_assigned_to_all_of_members_instance = RecipientsGroupAssignedToAllOfMembers.from_json(json)
# print the JSON string representation of the object
print(RecipientsGroupAssignedToAllOfMembers.to_json())

# convert the object into a dict
recipients_group_assigned_to_all_of_members_dict = recipients_group_assigned_to_all_of_members_instance.to_dict()
# create an instance of RecipientsGroupAssignedToAllOfMembers from a dict
recipients_group_assigned_to_all_of_members_from_dict = RecipientsGroupAssignedToAllOfMembers.from_dict(recipients_group_assigned_to_all_of_members_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


