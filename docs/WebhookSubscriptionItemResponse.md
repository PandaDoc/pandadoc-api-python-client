# WebhookSubscriptionItemResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**active** | **bool** |  | [optional] 
**payload** | [**List[WebhookSubscriptionPayloadEnum]**](WebhookSubscriptionPayloadEnum.md) |  | [optional] 
**triggers** | [**List[WebhookSubscriptionTriggerEnum]**](WebhookSubscriptionTriggerEnum.md) |  | [optional] 
**workspace_id** | **str** |  | [optional] 
**shared_key** | **str** |  | [optional] 
**status** | [**WebhookSubscriptionStatusEnum**](WebhookSubscriptionStatusEnum.md) |  | [optional] 

## Example

```python
from pandadoc_client.models.webhook_subscription_item_response import WebhookSubscriptionItemResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookSubscriptionItemResponse from a JSON string
webhook_subscription_item_response_instance = WebhookSubscriptionItemResponse.from_json(json)
# print the JSON string representation of the object
print(WebhookSubscriptionItemResponse.to_json())

# convert the object into a dict
webhook_subscription_item_response_dict = webhook_subscription_item_response_instance.to_dict()
# create an instance of WebhookSubscriptionItemResponse from a dict
webhook_subscription_item_response_from_dict = WebhookSubscriptionItemResponse.from_dict(webhook_subscription_item_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


