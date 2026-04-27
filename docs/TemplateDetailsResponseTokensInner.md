# TemplateDetailsResponseTokensInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**value** | **str** |  | [optional] 

## Example

```python
from pandadoc_client.models.template_details_response_tokens_inner import TemplateDetailsResponseTokensInner

# TODO update the JSON string below
json = "{}"
# create an instance of TemplateDetailsResponseTokensInner from a JSON string
template_details_response_tokens_inner_instance = TemplateDetailsResponseTokensInner.from_json(json)
# print the JSON string representation of the object
print(TemplateDetailsResponseTokensInner.to_json())

# convert the object into a dict
template_details_response_tokens_inner_dict = template_details_response_tokens_inner_instance.to_dict()
# create an instance of TemplateDetailsResponseTokensInner from a dict
template_details_response_tokens_inner_from_dict = TemplateDetailsResponseTokensInner.from_dict(template_details_response_tokens_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


