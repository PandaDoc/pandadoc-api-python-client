# WebhookSubscriptionSharedKeyResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shared_key** | **str** |  | [optional] 

## Example

```python
from pandadoc_client.models.webhook_subscription_shared_key_response import WebhookSubscriptionSharedKeyResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookSubscriptionSharedKeyResponse from a JSON string
webhook_subscription_shared_key_response_instance = WebhookSubscriptionSharedKeyResponse.from_json(json)
# print the JSON string representation of the object
print(WebhookSubscriptionSharedKeyResponse.to_json())

# convert the object into a dict
webhook_subscription_shared_key_response_dict = webhook_subscription_shared_key_response_instance.to_dict()
# create an instance of WebhookSubscriptionSharedKeyResponse from a dict
webhook_subscription_shared_key_response_from_dict = WebhookSubscriptionSharedKeyResponse.from_dict(webhook_subscription_shared_key_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


