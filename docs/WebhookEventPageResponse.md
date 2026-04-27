# WebhookEventPageResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[WebhookEventItemResponse]**](WebhookEventItemResponse.md) |  | [optional] 

## Example

```python
from pandadoc_client.models.webhook_event_page_response import WebhookEventPageResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookEventPageResponse from a JSON string
webhook_event_page_response_instance = WebhookEventPageResponse.from_json(json)
# print the JSON string representation of the object
print(WebhookEventPageResponse.to_json())

# convert the object into a dict
webhook_event_page_response_dict = webhook_event_page_response_instance.to_dict()
# create an instance of WebhookEventPageResponse from a dict
webhook_event_page_response_from_dict = WebhookEventPageResponse.from_dict(webhook_event_page_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


