# DocumentDetailsRecipientGroup


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
**name** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**members** | [**List[DocumentDetailsRecipientGroupMember]**](DocumentDetailsRecipientGroupMember.md) |  | [optional] 

## Example

```python
from pandadoc_client.models.document_details_recipient_group import DocumentDetailsRecipientGroup

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentDetailsRecipientGroup from a JSON string
document_details_recipient_group_instance = DocumentDetailsRecipientGroup.from_json(json)
# print the JSON string representation of the object
print(DocumentDetailsRecipientGroup.to_json())

# convert the object into a dict
document_details_recipient_group_dict = document_details_recipient_group_instance.to_dict()
# create an instance of DocumentDetailsRecipientGroup from a dict
document_details_recipient_group_from_dict = DocumentDetailsRecipientGroup.from_dict(document_details_recipient_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


