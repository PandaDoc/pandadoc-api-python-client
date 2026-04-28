# RecipientAssignedTo

Recipient

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

## Example

```python
from pandadoc_client.models.recipient_assigned_to import RecipientAssignedTo

# TODO update the JSON string below
json = "{}"
# create an instance of RecipientAssignedTo from a JSON string
recipient_assigned_to_instance = RecipientAssignedTo.from_json(json)
# print the JSON string representation of the object
print(RecipientAssignedTo.to_json())

# convert the object into a dict
recipient_assigned_to_dict = recipient_assigned_to_instance.to_dict()
# create an instance of RecipientAssignedTo from a dict
recipient_assigned_to_from_dict = RecipientAssignedTo.from_dict(recipient_assigned_to_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


