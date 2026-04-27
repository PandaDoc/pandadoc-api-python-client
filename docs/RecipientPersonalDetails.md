# RecipientPersonalDetails

Actor

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**recipient_type** | **str** |  | [optional] 
**role** | **str** |  | [optional] 
**roles** | **List[str]** |  | [optional] 
**signing_order** | **int** |  | [optional] 
**email** | **str** |  | [optional] 
**has_completed** | **bool** |  | [optional] 

## Example

```python
from pandadoc_client.models.recipient_personal_details import RecipientPersonalDetails

# TODO update the JSON string below
json = "{}"
# create an instance of RecipientPersonalDetails from a JSON string
recipient_personal_details_instance = RecipientPersonalDetails.from_json(json)
# print the JSON string representation of the object
print(RecipientPersonalDetails.to_json())

# convert the object into a dict
recipient_personal_details_dict = recipient_personal_details_instance.to_dict()
# create an instance of RecipientPersonalDetails from a dict
recipient_personal_details_from_dict = RecipientPersonalDetails.from_dict(recipient_personal_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


