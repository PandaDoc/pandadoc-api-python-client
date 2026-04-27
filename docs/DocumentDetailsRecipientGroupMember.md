# DocumentDetailsRecipientGroupMember

Recipient Group Member

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**shared_link** | **str** |  | [optional] 
**avatar** | **str** |  | [optional] 
**signature_date** | **str** |  | [optional] 

## Example

```python
from pandadoc_client.models.document_details_recipient_group_member import DocumentDetailsRecipientGroupMember

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentDetailsRecipientGroupMember from a JSON string
document_details_recipient_group_member_instance = DocumentDetailsRecipientGroupMember.from_json(json)
# print the JSON string representation of the object
print(DocumentDetailsRecipientGroupMember.to_json())

# convert the object into a dict
document_details_recipient_group_member_dict = document_details_recipient_group_member_instance.to_dict()
# create an instance of DocumentDetailsRecipientGroupMember from a dict
document_details_recipient_group_member_from_dict = DocumentDetailsRecipientGroupMember.from_dict(document_details_recipient_group_member_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


