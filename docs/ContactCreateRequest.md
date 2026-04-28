# ContactCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | An email address of the contact | [optional] 
**first_name** | **str** | Contact&#39;s first name | [optional] 
**last_name** | **str** | Contact&#39;s last name | [optional] 
**company** | **str** | Contact&#39;s company name | [optional] 
**job_title** | **str** | Contact&#39;s job title | [optional] 
**phone** | **str** | A phone number | [optional] 
**country** | **str** | A country name | [optional] 
**state** | **str** | A state name | [optional] 
**street_address** | **str** | A street address | [optional] 
**city** | **str** | A city name | [optional] 
**postal_code** | **str** | A postal code | [optional] 

## Example

```python
from pandadoc_client.models.contact_create_request import ContactCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ContactCreateRequest from a JSON string
contact_create_request_instance = ContactCreateRequest.from_json(json)
# print the JSON string representation of the object
print(ContactCreateRequest.to_json())

# convert the object into a dict
contact_create_request_dict = contact_create_request_instance.to_dict()
# create an instance of ContactCreateRequest from a dict
contact_create_request_from_dict = ContactCreateRequest.from_dict(contact_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


