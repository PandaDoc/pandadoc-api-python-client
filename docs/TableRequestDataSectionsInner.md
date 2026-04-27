# TableRequestDataSectionsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**header** | [**List[TableCell]**](TableCell.md) |  | 
**rows** | **List[List[TableCell]]** |  | 

## Example

```python
from pandadoc_client.models.table_request_data_sections_inner import TableRequestDataSectionsInner

# TODO update the JSON string below
json = "{}"
# create an instance of TableRequestDataSectionsInner from a JSON string
table_request_data_sections_inner_instance = TableRequestDataSectionsInner.from_json(json)
# print the JSON string representation of the object
print(TableRequestDataSectionsInner.to_json())

# convert the object into a dict
table_request_data_sections_inner_dict = table_request_data_sections_inner_instance.to_dict()
# create an instance of TableRequestDataSectionsInner from a dict
table_request_data_sections_inner_from_dict = TableRequestDataSectionsInner.from_dict(table_request_data_sections_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


