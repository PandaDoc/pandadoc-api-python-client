# RecipientAssignmentDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**recipient_type** | **str** |  | [optional] 
**roles** | **List[str]** |  | [optional] 
**signing_order** | **int** |  | [optional] 
**has_completed** | **bool** |  | [optional] 

## Example

```python
from pandadoc_client.models.recipient_assignment_details import RecipientAssignmentDetails

# TODO update the JSON string below
json = "{}"
# create an instance of RecipientAssignmentDetails from a JSON string
recipient_assignment_details_instance = RecipientAssignmentDetails.from_json(json)
# print the JSON string representation of the object
print(RecipientAssignmentDetails.to_json())

# convert the object into a dict
recipient_assignment_details_dict = recipient_assignment_details_instance.to_dict()
# create an instance of RecipientAssignmentDetails from a dict
recipient_assignment_details_from_dict = RecipientAssignmentDetails.from_dict(recipient_assignment_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


