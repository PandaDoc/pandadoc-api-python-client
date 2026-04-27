# DocumentFieldAssignmentItem

Specifies a field and the recipient it should be assigned or unassigned to.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**field_id** | **str** | UUID of the field to assign or unassign. | 
**assigned_to** | **str** | UUID of the recipient to assign the field to. Set to &#x60;null&#x60; to unassign the field from its current recipient.  | 

## Example

```python
from pandadoc_client.models.document_field_assignment_item import DocumentFieldAssignmentItem

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentFieldAssignmentItem from a JSON string
document_field_assignment_item_instance = DocumentFieldAssignmentItem.from_json(json)
# print the JSON string representation of the object
print(DocumentFieldAssignmentItem.to_json())

# convert the object into a dict
document_field_assignment_item_dict = document_field_assignment_item_instance.to_dict()
# create an instance of DocumentFieldAssignmentItem from a dict
document_field_assignment_item_from_dict = DocumentFieldAssignmentItem.from_dict(document_field_assignment_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


