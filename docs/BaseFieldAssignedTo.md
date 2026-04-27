# BaseFieldAssignedTo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**recipient_type** | **str** |  | [optional] 
**roles** | **List[str]** |  | [optional] 
**signing_order** | **int** |  | [optional] 
**has_completed** | **bool** |  | [optional] 
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**phone** | **str** |  | [optional] 
**role** | **str** |  | [optional] 
**delivery_methods** | [**AssignedToRecipientDeliveryMethods**](AssignedToRecipientDeliveryMethods.md) |  | [optional] 
**redirect** | [**RecipientRedirectSettings**](RecipientRedirectSettings.md) |  | [optional] 
**type** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**members** | [**List[RecipientsGroupAssignedToAllOfMembers]**](RecipientsGroupAssignedToAllOfMembers.md) |  | [optional] 

## Example

```python
from pandadoc_client.models.base_field_assigned_to import BaseFieldAssignedTo

# TODO update the JSON string below
json = "{}"
# create an instance of BaseFieldAssignedTo from a JSON string
base_field_assigned_to_instance = BaseFieldAssignedTo.from_json(json)
# print the JSON string representation of the object
print(BaseFieldAssignedTo.to_json())

# convert the object into a dict
base_field_assigned_to_dict = base_field_assigned_to_instance.to_dict()
# create an instance of BaseFieldAssignedTo from a dict
base_field_assigned_to_from_dict = BaseFieldAssignedTo.from_dict(base_field_assigned_to_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


