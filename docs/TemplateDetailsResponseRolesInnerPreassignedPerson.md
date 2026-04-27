# TemplateDetailsResponseRolesInnerPreassignedPerson


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | [optional] 
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**placeholder_name** | **str** |  | [optional] 
**placeholder_source** | **str** |  | [optional] 
**members** | [**List[TemplateDetailsResponseRolesInnerPreassignedPersonMembersInner]**](TemplateDetailsResponseRolesInnerPreassignedPersonMembersInner.md) | List of contacts in the group. Only present for type \&quot;preassigned contact group\&quot;. | [optional] 

## Example

```python
from pandadoc_client.models.template_details_response_roles_inner_preassigned_person import TemplateDetailsResponseRolesInnerPreassignedPerson

# TODO update the JSON string below
json = "{}"
# create an instance of TemplateDetailsResponseRolesInnerPreassignedPerson from a JSON string
template_details_response_roles_inner_preassigned_person_instance = TemplateDetailsResponseRolesInnerPreassignedPerson.from_json(json)
# print the JSON string representation of the object
print(TemplateDetailsResponseRolesInnerPreassignedPerson.to_json())

# convert the object into a dict
template_details_response_roles_inner_preassigned_person_dict = template_details_response_roles_inner_preassigned_person_instance.to_dict()
# create an instance of TemplateDetailsResponseRolesInnerPreassignedPerson from a dict
template_details_response_roles_inner_preassigned_person_from_dict = TemplateDetailsResponseRolesInnerPreassignedPerson.from_dict(template_details_response_roles_inner_preassigned_person_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


