# WebhookEventItemResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | Unique webhook subscription event identifier | [optional] 
**name** | **str** | Webhook subscription name | [optional] 
**type** | [**WebhookEventTriggerEnum**](WebhookEventTriggerEnum.md) |  | [optional] 
**http_status_code** | **int** | Webhook subscription event response http status code | [optional] 
**error** | [**WebhookEventErrorEnum**](WebhookEventErrorEnum.md) |  | [optional] 
**delivery_time** | **datetime** | Webhook subscription event delivery time | [optional] 

## Example

```python
from pandadoc_client.models.webhook_event_item_response import WebhookEventItemResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookEventItemResponse from a JSON string
webhook_event_item_response_instance = WebhookEventItemResponse.from_json(json)
# print the JSON string representation of the object
print(WebhookEventItemResponse.to_json())

# convert the object into a dict
webhook_event_item_response_dict = webhook_event_item_response_instance.to_dict()
# create an instance of WebhookEventItemResponse from a dict
webhook_event_item_response_from_dict = WebhookEventItemResponse.from_dict(webhook_event_item_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


