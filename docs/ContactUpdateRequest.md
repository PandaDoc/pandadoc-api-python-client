# ContactUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**company** | **str** |  | [optional] 
**job_title** | **str** |  | [optional] 
**phone** | **str** |  | [optional] 
**state** | **str** |  | [optional] 
**street_address** | **str** |  | [optional] 
**city** | **str** |  | [optional] 
**postal_code** | **str** |  | [optional] 

## Example

```python
from pandadoc_client.models.contact_update_request import ContactUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ContactUpdateRequest from a JSON string
contact_update_request_instance = ContactUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(ContactUpdateRequest.to_json())

# convert the object into a dict
contact_update_request_dict = contact_update_request_instance.to_dict()
# create an instance of ContactUpdateRequest from a dict
contact_update_request_from_dict = ContactUpdateRequest.from_dict(contact_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


