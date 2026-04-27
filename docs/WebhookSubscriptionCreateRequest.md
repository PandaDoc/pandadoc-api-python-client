# WebhookSubscriptionCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Set a name for the Webhooks subscription. | 
**url** | **str** | Set the Webhooks subscription URL. | 
**active** | **bool** | Set the status of the Webhooks subscription. | [optional] [default to True]
**payload** | [**List[WebhookSubscriptionPayloadEnum]**](WebhookSubscriptionPayloadEnum.md) | Set a payload structure. | [optional] 
**triggers** | [**List[WebhookSubscriptionTriggerEnum]**](WebhookSubscriptionTriggerEnum.md) | Set trigger events for the Webhooks subscription. | 

## Example

```python
from pandadoc_client.models.webhook_subscription_create_request import WebhookSubscriptionCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookSubscriptionCreateRequest from a JSON string
webhook_subscription_create_request_instance = WebhookSubscriptionCreateRequest.from_json(json)
# print the JSON string representation of the object
print(WebhookSubscriptionCreateRequest.to_json())

# convert the object into a dict
webhook_subscription_create_request_dict = webhook_subscription_create_request_instance.to_dict()
# create an instance of WebhookSubscriptionCreateRequest from a dict
webhook_subscription_create_request_from_dict = WebhookSubscriptionCreateRequest.from_dict(webhook_subscription_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


