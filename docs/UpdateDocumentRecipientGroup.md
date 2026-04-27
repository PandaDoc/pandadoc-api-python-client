# UpdateDocumentRecipientGroup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role** | **str** | A recipient&#39;s role in the document from the template. A recipient will be added in CC if a role parameter is not provided. | [optional] 
**signing_order** | **int** | Set a signing order for a recipient. Learn more: https://developers.pandadoc.com/docs/set-signing-order  | [optional] 
**id** | **str** |  | [optional] 
**name** | **str** |  | 
**type** | **str** |  | [optional] 
**members** | [**List[BaseIdentity]**](BaseIdentity.md) |  | [optional] 

## Example

```python
from pandadoc_client.models.update_document_recipient_group import UpdateDocumentRecipientGroup

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateDocumentRecipientGroup from a JSON string
update_document_recipient_group_instance = UpdateDocumentRecipientGroup.from_json(json)
# print the JSON string representation of the object
print(UpdateDocumentRecipientGroup.to_json())

# convert the object into a dict
update_document_recipient_group_dict = update_document_recipient_group_instance.to_dict()
# create an instance of UpdateDocumentRecipientGroup from a dict
update_document_recipient_group_from_dict = UpdateDocumentRecipientGroup.from_dict(update_document_recipient_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


