# BaseIdentity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | A recipient&#39;s email address. | [optional] 
**phone** | **str** | A recipient&#39;s phone number. | [optional] 
**first_name** | **str** | A recipient&#39;s first name. We automatically take the first name from contact data if this field is missed. | [optional] 
**last_name** | **str** | A recipient&#39;s last name. We automatically take the last name from contact data if this field is missed. | [optional] 

## Example

```python
from pandadoc_client.models.base_identity import BaseIdentity

# TODO update the JSON string below
json = "{}"
# create an instance of BaseIdentity from a JSON string
base_identity_instance = BaseIdentity.from_json(json)
# print the JSON string representation of the object
print(BaseIdentity.to_json())

# convert the object into a dict
base_identity_dict = base_identity_instance.to_dict()
# create an instance of BaseIdentity from a dict
base_identity_from_dict = BaseIdentity.from_dict(base_identity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


