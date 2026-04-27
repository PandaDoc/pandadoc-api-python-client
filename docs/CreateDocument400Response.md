# CreateDocument400Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**detail** | **object** |  | [optional] 

## Example

```python
from pandadoc_client.models.create_document400_response import CreateDocument400Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateDocument400Response from a JSON string
create_document400_response_instance = CreateDocument400Response.from_json(json)
# print the JSON string representation of the object
print(CreateDocument400Response.to_json())

# convert the object into a dict
create_document400_response_dict = create_document400_response_instance.to_dict()
# create an instance of CreateDocument400Response from a dict
create_document400_response_from_dict = CreateDocument400Response.from_dict(create_document400_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


