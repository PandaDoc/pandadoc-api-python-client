# QuoteResponseSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**selection_type** | **str** |  | [optional] 

## Example

```python
from pandadoc_client.models.quote_response_settings import QuoteResponseSettings

# TODO update the JSON string below
json = "{}"
# create an instance of QuoteResponseSettings from a JSON string
quote_response_settings_instance = QuoteResponseSettings.from_json(json)
# print the JSON string representation of the object
print(QuoteResponseSettings.to_json())

# convert the object into a dict
quote_response_settings_dict = quote_response_settings_instance.to_dict()
# create an instance of QuoteResponseSettings from a dict
quote_response_settings_from_dict = QuoteResponseSettings.from_dict(quote_response_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


