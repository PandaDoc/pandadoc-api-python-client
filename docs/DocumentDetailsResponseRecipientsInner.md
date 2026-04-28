# DocumentDetailsResponseRecipientsInner


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
**last_name** | **str** |  | [optional] 
**contact_id** | **str** |  | [optional] 
**first_name** | **str** |  | [optional] 
**phone** | **str** |  | [optional] 
**delivery_methods** | [**RecipientDeliveryMethods**](RecipientDeliveryMethods.md) |  | [optional] 
**shared_link** | **str** |  | [optional] 
**signature_date** | **str** |  | [optional] 
**verification_settings** | [**RecipientVerificationSettings**](RecipientVerificationSettings.md) |  | [optional] 
**redirect** | [**RecipientRedirect**](RecipientRedirect.md) |  | [optional] 
**avatar** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**members** | [**List[DocumentDetailsRecipientGroupMember]**](DocumentDetailsRecipientGroupMember.md) |  | [optional] 

## Example

```python
from pandadoc_client.models.document_details_response_recipients_inner import DocumentDetailsResponseRecipientsInner

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentDetailsResponseRecipientsInner from a JSON string
document_details_response_recipients_inner_instance = DocumentDetailsResponseRecipientsInner.from_json(json)
# print the JSON string representation of the object
print(DocumentDetailsResponseRecipientsInner.to_json())

# convert the object into a dict
document_details_response_recipients_inner_dict = document_details_response_recipients_inner_instance.to_dict()
# create an instance of DocumentDetailsResponseRecipientsInner from a dict
document_details_response_recipients_inner_from_dict = DocumentDetailsResponseRecipientsInner.from_dict(document_details_response_recipients_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


