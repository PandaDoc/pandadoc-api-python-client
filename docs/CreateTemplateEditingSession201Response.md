# CreateTemplateEditingSession201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Internal id of the editing session. Don&#39;t use it, it&#39;s not a token. | [optional] 
**email** | **str** | Email associated with the editing session. | [optional] 
**expires_at** | **datetime** | Date and time when the editing session expires. | [optional] 
**key** | **str** | Same value as &#x60;token&#x60;, token for the embedded editor, aka E-Token. Deprecated — use &#x60;token&#x60; instead. | [optional] 
**token** | **str** | Token for the embedded editor, aka E-Token. Use it for your Embedding. | [optional] 
**template_id** | **str** | ID of the template | [optional] 

## Example

```python
from pandadoc_client.models.create_template_editing_session201_response import CreateTemplateEditingSession201Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTemplateEditingSession201Response from a JSON string
create_template_editing_session201_response_instance = CreateTemplateEditingSession201Response.from_json(json)
# print the JSON string representation of the object
print(CreateTemplateEditingSession201Response.to_json())

# convert the object into a dict
create_template_editing_session201_response_dict = create_template_editing_session201_response_instance.to_dict()
# create an instance of CreateTemplateEditingSession201Response from a dict
create_template_editing_session201_response_from_dict = CreateTemplateEditingSession201Response.from_dict(create_template_editing_session201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


