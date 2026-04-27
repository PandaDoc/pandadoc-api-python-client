# ContactListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[ContactDetailsResponse]**](ContactDetailsResponse.md) |  | [optional] 

## Example

```python
from pandadoc_client.models.contact_list_response import ContactListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ContactListResponse from a JSON string
contact_list_response_instance = ContactListResponse.from_json(json)
# print the JSON string representation of the object
print(ContactListResponse.to_json())

# convert the object into a dict
contact_list_response_dict = contact_list_response_instance.to_dict()
# create an instance of ContactListResponse from a dict
contact_list_response_from_dict = ContactListResponse.from_dict(contact_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


