# CreateUser400Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**detail** | **object** |  | [optional] 

## Example

```python
from pandadoc_client.models.create_user400_response import CreateUser400Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateUser400Response from a JSON string
create_user400_response_instance = CreateUser400Response.from_json(json)
# print the JSON string representation of the object
print(CreateUser400Response.to_json())

# convert the object into a dict
create_user400_response_dict = create_user400_response_instance.to_dict()
# create an instance of CreateUser400Response from a dict
create_user400_response_from_dict = CreateUser400Response.from_dict(create_user400_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


