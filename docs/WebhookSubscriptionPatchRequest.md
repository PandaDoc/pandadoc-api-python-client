# WebhookSubscriptionPatchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Set a new name for the Webhooks subscription. | [optional] 
**url** | **str** | Set the new Webhooks subscription URL. | [optional] 
**active** | **bool** | Set the status of the Webhooks subscription. | [optional] [default to True]
**payload** | [**List[WebhookSubscriptionPayloadEnum]**](WebhookSubscriptionPayloadEnum.md) | Set a new payload structure. | [optional] 
**triggers** | [**List[WebhookSubscriptionTriggerEnum]**](WebhookSubscriptionTriggerEnum.md) | Set trigger events for the Webhooks subscription. | [optional] 

## Example

```python
from pandadoc_client.models.webhook_subscription_patch_request import WebhookSubscriptionPatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookSubscriptionPatchRequest from a JSON string
webhook_subscription_patch_request_instance = WebhookSubscriptionPatchRequest.from_json(json)
# print the JSON string representation of the object
print(WebhookSubscriptionPatchRequest.to_json())

# convert the object into a dict
webhook_subscription_patch_request_dict = webhook_subscription_patch_request_instance.to_dict()
# create an instance of WebhookSubscriptionPatchRequest from a dict
webhook_subscription_patch_request_from_dict = WebhookSubscriptionPatchRequest.from_dict(webhook_subscription_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


