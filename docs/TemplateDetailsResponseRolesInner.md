# TemplateDetailsResponseRolesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**signing_order** | **str** |  | [optional] 
**preassigned_person** | [**TemplateDetailsResponseRolesInnerPreassignedPerson**](TemplateDetailsResponseRolesInnerPreassignedPerson.md) |  | [optional] 

## Example

```python
from pandadoc_client.models.template_details_response_roles_inner import TemplateDetailsResponseRolesInner

# TODO update the JSON string below
json = "{}"
# create an instance of TemplateDetailsResponseRolesInner from a JSON string
template_details_response_roles_inner_instance = TemplateDetailsResponseRolesInner.from_json(json)
# print the JSON string representation of the object
print(TemplateDetailsResponseRolesInner.to_json())

# convert the object into a dict
template_details_response_roles_inner_dict = template_details_response_roles_inner_instance.to_dict()
# create an instance of TemplateDetailsResponseRolesInner from a dict
template_details_response_roles_inner_from_dict = TemplateDetailsResponseRolesInner.from_dict(template_details_response_roles_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


