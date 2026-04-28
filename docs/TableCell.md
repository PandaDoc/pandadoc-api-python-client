# TableCell

Defines a single cell in the table, which can appear in either the header or the rows.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** | Cell text. | 
**col_span** | **int** | Represents how many columns the cell occupies. | [optional] 
**row_span** | **int** | Represents the number of rows the cell occupies. | [optional] 

## Example

```python
from pandadoc_client.models.table_cell import TableCell

# TODO update the JSON string below
json = "{}"
# create an instance of TableCell from a JSON string
table_cell_instance = TableCell.from_json(json)
# print the JSON string representation of the object
print(TableCell.to_json())

# convert the object into a dict
table_cell_dict = table_cell_instance.to_dict()
# create an instance of TableCell from a dict
table_cell_from_dict = TableCell.from_dict(table_cell_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


