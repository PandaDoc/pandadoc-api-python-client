# CreateDocumentActor


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role** | **str** | A recipient&#39;s role in the document from the template. A recipient will be added in CC if a role parameter is not provided. | [optional] 
**signing_order** | **int** | Set a signing order for a recipient. Learn more: https://developers.pandadoc.com/docs/set-signing-order  | [optional] 
**email** | **str** | A recipient&#39;s email address. | [optional] 
**phone** | **str** | A recipient&#39;s phone number. | [optional] 
**first_name** | **str** | A recipient&#39;s first name. We automatically take the first name from contact data if this field is missed. | [optional] 
**last_name** | **str** | A recipient&#39;s last name. We automatically take the last name from contact data if this field is missed. | [optional] 
**delivery_methods** | [**RecipientDeliveryMethods**](RecipientDeliveryMethods.md) |  | [optional] 
**redirect** | [**RecipientRedirect**](RecipientRedirect.md) |  | [optional] 
**type** | **str** |  | 
**verification_settings** | [**RecipientVerificationSettings**](RecipientVerificationSettings.md) |  | [optional] 
**name** | **str** |  | 
**members** | [**List[BaseIdentity]**](BaseIdentity.md) |  | [optional] 

## Example

```python
from pandadoc_client.models.create_document_actor import CreateDocumentActor

# TODO update the JSON string below
json = "{}"
# create an instance of CreateDocumentActor from a JSON string
create_document_actor_instance = CreateDocumentActor.from_json(json)
# print the JSON string representation of the object
print(CreateDocumentActor.to_json())

# convert the object into a dict
create_document_actor_dict = create_document_actor_instance.to_dict()
# create an instance of CreateDocumentActor from a dict
create_document_actor_from_dict = CreateDocumentActor.from_dict(create_document_actor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


