# ContactDetailsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | A unique identifier of the contact | [optional] 
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
from pandadoc_client.models.contact_details_response import ContactDetailsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ContactDetailsResponse from a JSON string
contact_details_response_instance = ContactDetailsResponse.from_json(json)
# print the JSON string representation of the object
print(ContactDetailsResponse.to_json())

# convert the object into a dict
contact_details_response_dict = contact_details_response_instance.to_dict()
# create an instance of ContactDetailsResponse from a dict
contact_details_response_from_dict = ContactDetailsResponse.from_dict(contact_details_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


