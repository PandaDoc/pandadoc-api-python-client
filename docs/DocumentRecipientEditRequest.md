# DocumentRecipientEditRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | You cannot use the email of another contact when updating a recipient contact. | [optional] 
**phone** | **str** |  | [optional] 
**delivery_methods** | [**RecipientDeliveryMethods**](RecipientDeliveryMethods.md) |  | [optional] 
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**company** | **str** |  | [optional] 
**job_title** | **str** |  | [optional] 
**state** | **str** |  | [optional] 
**street_address** | **str** |  | [optional] 
**city** | **str** |  | [optional] 
**postal_code** | **str** |  | [optional] 
**verification_settings** | [**RecipientVerificationSettings**](RecipientVerificationSettings.md) |  | [optional] 
**redirect** | [**RecipientRedirect**](RecipientRedirect.md) |  | [optional] 

## Example

```python
from pandadoc_client.models.document_recipient_edit_request import DocumentRecipientEditRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentRecipientEditRequest from a JSON string
document_recipient_edit_request_instance = DocumentRecipientEditRequest.from_json(json)
# print the JSON string representation of the object
print(DocumentRecipientEditRequest.to_json())

# convert the object into a dict
document_recipient_edit_request_dict = document_recipient_edit_request_instance.to_dict()
# create an instance of DocumentRecipientEditRequest from a dict
document_recipient_edit_request_from_dict = DocumentRecipientEditRequest.from_dict(document_recipient_edit_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


