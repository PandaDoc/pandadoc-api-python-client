# WebhookSubscriptionListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[WebhookSubscriptionItemResponse]**](WebhookSubscriptionItemResponse.md) |  | [optional] 

## Example

```python
from pandadoc_client.models.webhook_subscription_list_response import WebhookSubscriptionListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookSubscriptionListResponse from a JSON string
webhook_subscription_list_response_instance = WebhookSubscriptionListResponse.from_json(json)
# print the JSON string representation of the object
print(WebhookSubscriptionListResponse.to_json())

# convert the object into a dict
webhook_subscription_list_response_dict = webhook_subscription_list_response_instance.to_dict()
# create an instance of WebhookSubscriptionListResponse from a dict
webhook_subscription_list_response_from_dict = WebhookSubscriptionListResponse.from_dict(webhook_subscription_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


