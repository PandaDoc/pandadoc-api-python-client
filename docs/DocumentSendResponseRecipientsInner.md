# DocumentSendResponseRecipientsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**recipient_type** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**phone** | **str** |  | [optional] 
**delivery_methods** | [**RecipientDeliveryMethods**](RecipientDeliveryMethods.md) |  | [optional] 
**signing_order** | **int** |  | [optional] 
**shared_link** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from pandadoc_client.models.document_send_response_recipients_inner import DocumentSendResponseRecipientsInner

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentSendResponseRecipientsInner from a JSON string
document_send_response_recipients_inner_instance = DocumentSendResponseRecipientsInner.from_json(json)
# print the JSON string representation of the object
print(DocumentSendResponseRecipientsInner.to_json())

# convert the object into a dict
document_send_response_recipients_inner_dict = document_send_response_recipients_inner_instance.to_dict()
# create an instance of DocumentSendResponseRecipientsInner from a dict
document_send_response_recipients_inner_from_dict = DocumentSendResponseRecipientsInner.from_dict(document_send_response_recipients_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


