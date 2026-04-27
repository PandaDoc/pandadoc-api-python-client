# WebhookEventDetailsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | Unique webhook subscription event identifier | [optional] 
**name** | **str** | Webhook subscription name | [optional] 
**type** | [**WebhookEventTriggerEnum**](WebhookEventTriggerEnum.md) |  | [optional] 
**http_status_code** | **int** | Webhook subscription event response http status code | [optional] 
**error** | [**WebhookEventErrorEnum**](WebhookEventErrorEnum.md) |  | [optional] 
**delivery_time** | **datetime** | Webhook subscription event delivery time | [optional] 
**url** | **str** | Webhook subscription event destination url | [optional] 
**signature** | **str** | Webhook subscription event digital signature | [optional] 
**request_body** | **str** | Webhook subscription event request body | [optional] 
**response_body** | **str** | Webhook subscription response body | [optional] 
**response_headers** | **str** | Webhook subscription response headers | [optional] 
**event_time** | **datetime** | Webhook subscription event trigger time | [optional] 

## Example

```python
from pandadoc_client.models.webhook_event_details_response import WebhookEventDetailsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookEventDetailsResponse from a JSON string
webhook_event_details_response_instance = WebhookEventDetailsResponse.from_json(json)
# print the JSON string representation of the object
print(WebhookEventDetailsResponse.to_json())

# convert the object into a dict
webhook_event_details_response_dict = webhook_event_details_response_instance.to_dict()
# create an instance of WebhookEventDetailsResponse from a dict
webhook_event_details_response_from_dict = WebhookEventDetailsResponse.from_dict(webhook_event_details_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


