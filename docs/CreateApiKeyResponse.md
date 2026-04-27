# CreateApiKeyResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** | A unique identifier of the user. | [optional] 
**type** | [**ApiKeyTypeEnum**](ApiKeyTypeEnum.md) |  | [optional] [default to ApiKeyTypeEnum.SANDBOX]
**workspace_id** | **str** | A unique identifier of the workspace. | [optional] 
**key** | **str** | A New Public API key. | [optional] 

## Example

```python
from pandadoc_client.models.create_api_key_response import CreateApiKeyResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateApiKeyResponse from a JSON string
create_api_key_response_instance = CreateApiKeyResponse.from_json(json)
# print the JSON string representation of the object
print(CreateApiKeyResponse.to_json())

# convert the object into a dict
create_api_key_response_dict = create_api_key_response_instance.to_dict()
# create an instance of CreateApiKeyResponse from a dict
create_api_key_response_from_dict = CreateApiKeyResponse.from_dict(create_api_key_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


