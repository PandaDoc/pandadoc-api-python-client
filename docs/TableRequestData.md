# TableRequestData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sections** | [**List[TableRequestDataSectionsInner]**](TableRequestDataSectionsInner.md) |  | 

## Example

```python
from pandadoc_client.models.table_request_data import TableRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of TableRequestData from a JSON string
table_request_data_instance = TableRequestData.from_json(json)
# print the JSON string representation of the object
print(TableRequestData.to_json())

# convert the object into a dict
table_request_data_dict = table_request_data_instance.to_dict()
# create an instance of TableRequestData from a dict
table_request_data_from_dict = TableRequestData.from_dict(table_request_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


