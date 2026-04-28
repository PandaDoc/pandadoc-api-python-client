# UpdateDocumentActor


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role** | **str** | A recipient&#39;s role in the document from the template. A recipient will be added in CC if a role parameter is not provided. | [optional] 
**signing_order** | **int** | Set a signing order for a recipient. Learn more: https://developers.pandadoc.com/docs/set-signing-order  | [optional] 
**email** | **str** | A recipient&#39;s email address. | [optional] 
**phone** | **str** | A recipient&#39;s phone number. | [optional] 
**first_name** | **str** | A recipient&#39;s first name. We automatically take the first name from contact data if this field is missed. | [optional] 
**last_name** | **str** | A recipient&#39;s last name. We automatically take the last name from contact data if this field is missed. | [optional] 
**id** | **str** |  | [optional] 
**delivery_methods** | [**RecipientDeliveryMethods**](RecipientDeliveryMethods.md) |  | [optional] 
**redirect** | [**RecipientRedirect**](RecipientRedirect.md) |  | [optional] 
**type** | **str** |  | [optional] 
**name** | **str** |  | 
**members** | [**List[BaseIdentity]**](BaseIdentity.md) |  | [optional] 

## Example

```python
from pandadoc_client.models.update_document_actor import UpdateDocumentActor

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateDocumentActor from a JSON string
update_document_actor_instance = UpdateDocumentActor.from_json(json)
# print the JSON string representation of the object
print(UpdateDocumentActor.to_json())

# convert the object into a dict
update_document_actor_dict = update_document_actor_instance.to_dict()
# create an instance of UpdateDocumentActor from a dict
update_document_actor_from_dict = UpdateDocumentActor.from_dict(update_document_actor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


