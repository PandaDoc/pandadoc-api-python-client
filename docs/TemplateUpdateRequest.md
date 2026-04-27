# TemplateUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tokens** | [**List[DocumentUpdateRequestTokensInner]**](DocumentUpdateRequestTokensInner.md) | Create or initialize multiple CUSTOM variables with their values using tokens/values list. Template&#39;s predefined variables are read-only. Any attempts to do so will be ignored. | [optional] 

## Example

```python
from pandadoc_client.models.template_update_request import TemplateUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TemplateUpdateRequest from a JSON string
template_update_request_instance = TemplateUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(TemplateUpdateRequest.to_json())

# convert the object into a dict
template_update_request_dict = template_update_request_instance.to_dict()
# create an instance of TemplateUpdateRequest from a dict
template_update_request_from_dict = TemplateUpdateRequest.from_dict(template_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


