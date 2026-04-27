# RecipientDeliveryMethods


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **bool** |  | [optional] 
**sms** | **bool** |  | [optional] 

## Example

```python
from pandadoc_client.models.recipient_delivery_methods import RecipientDeliveryMethods

# TODO update the JSON string below
json = "{}"
# create an instance of RecipientDeliveryMethods from a JSON string
recipient_delivery_methods_instance = RecipientDeliveryMethods.from_json(json)
# print the JSON string representation of the object
print(RecipientDeliveryMethods.to_json())

# convert the object into a dict
recipient_delivery_methods_dict = recipient_delivery_methods_instance.to_dict()
# create an instance of RecipientDeliveryMethods from a dict
recipient_delivery_methods_from_dict = RecipientDeliveryMethods.from_dict(recipient_delivery_methods_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


