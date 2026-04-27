# AssignedToRecipientDeliveryMethods


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sms** | **bool** |  | [optional] 
**email** | **bool** |  | [optional] 

## Example

```python
from pandadoc_client.models.assigned_to_recipient_delivery_methods import AssignedToRecipientDeliveryMethods

# TODO update the JSON string below
json = "{}"
# create an instance of AssignedToRecipientDeliveryMethods from a JSON string
assigned_to_recipient_delivery_methods_instance = AssignedToRecipientDeliveryMethods.from_json(json)
# print the JSON string representation of the object
print(AssignedToRecipientDeliveryMethods.to_json())

# convert the object into a dict
assigned_to_recipient_delivery_methods_dict = assigned_to_recipient_delivery_methods_instance.to_dict()
# create an instance of AssignedToRecipientDeliveryMethods from a dict
assigned_to_recipient_delivery_methods_from_dict = AssignedToRecipientDeliveryMethods.from_dict(assigned_to_recipient_delivery_methods_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


