# WebhookEventDetailsResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str, none_type** | Unique webhook subscription event identifier | [optional] 
**name** | **str** | Webhook subscription name | [optional] 
**type** | [**WebhookEventTriggerEnum**](WebhookEventTriggerEnum.md) |  | [optional] 
**http_status_code** | **int, none_type** | Webhook subscription event response http status code | [optional] 
**error** | [**WebhookEventErrorEnum**](WebhookEventErrorEnum.md) |  | [optional] 
**delivery_time** | **datetime** | Webhook subscription event delivery time | [optional] 
**url** | **str** | Webhook subscription event destination url | [optional] 
**signature** | **str** | Webhook subscription event digital signature | [optional] 
**request_body** | **str** | Webhook subscription event request body | [optional] 
**response_body** | **str, none_type** | Webhook subscription response body | [optional] 
**response_headers** | **str, none_type** | Webhook subscription response headers | [optional] 
**event_time** | **datetime** | Webhook subscription event trigger time | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


