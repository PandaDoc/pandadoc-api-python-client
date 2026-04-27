# DocumentDetailsRecipient


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

## Example

```python
from pandadoc_client.models.document_details_recipient import DocumentDetailsRecipient

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentDetailsRecipient from a JSON string
document_details_recipient_instance = DocumentDetailsRecipient.from_json(json)
# print the JSON string representation of the object
print(DocumentDetailsRecipient.to_json())

# convert the object into a dict
document_details_recipient_dict = document_details_recipient_instance.to_dict()
# create an instance of DocumentDetailsRecipient from a dict
document_details_recipient_from_dict = DocumentDetailsRecipient.from_dict(document_details_recipient_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


