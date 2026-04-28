# RecipientsGroupAssignedTo

Collection of Recipients

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**recipient_type** | **str** |  | [optional] 
**roles** | **List[str]** |  | [optional] 
**signing_order** | **int** |  | [optional] 
**has_completed** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 
**members** | [**List[RecipientsGroupAssignedToAllOfMembers]**](RecipientsGroupAssignedToAllOfMembers.md) |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from pandadoc_client.models.recipients_group_assigned_to import RecipientsGroupAssignedTo

# TODO update the JSON string below
json = "{}"
# create an instance of RecipientsGroupAssignedTo from a JSON string
recipients_group_assigned_to_instance = RecipientsGroupAssignedTo.from_json(json)
# print the JSON string representation of the object
print(RecipientsGroupAssignedTo.to_json())

# convert the object into a dict
recipients_group_assigned_to_dict = recipients_group_assigned_to_instance.to_dict()
# create an instance of RecipientsGroupAssignedTo from a dict
recipients_group_assigned_to_from_dict = RecipientsGroupAssignedTo.from_dict(recipients_group_assigned_to_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


