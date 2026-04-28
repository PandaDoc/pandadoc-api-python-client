# TableRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the table. | 
**data** | [**TableRequestData**](TableRequestData.md) |  | 

## Example

```python
from pandadoc_client.models.table_request import TableRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TableRequest from a JSON string
table_request_instance = TableRequest.from_json(json)
# print the JSON string representation of the object
print(TableRequest.to_json())

# convert the object into a dict
table_request_dict = table_request_instance.to_dict()
# create an instance of TableRequest from a dict
table_request_from_dict = TableRequest.from_dict(table_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


