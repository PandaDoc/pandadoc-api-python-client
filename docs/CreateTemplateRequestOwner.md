# CreateTemplateRequestOwner

You can set an owner of a template as an `email` or `membership_id`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**membership_id** | **str** |  | [optional] 
**email** | **str** |  | [optional] 

## Example

```python
from pandadoc_client.models.create_template_request_owner import CreateTemplateRequestOwner

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTemplateRequestOwner from a JSON string
create_template_request_owner_instance = CreateTemplateRequestOwner.from_json(json)
# print the JSON string representation of the object
print(CreateTemplateRequestOwner.to_json())

# convert the object into a dict
create_template_request_owner_dict = create_template_request_owner_instance.to_dict()
# create an instance of CreateTemplateRequestOwner from a dict
create_template_request_owner_from_dict = CreateTemplateRequestOwner.from_dict(create_template_request_owner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


