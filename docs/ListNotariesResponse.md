# ListNotariesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[ListNotariesResponseResultsInner]**](ListNotariesResponseResultsInner.md) | Array of notary objects | [optional] 
**count** | **int** | Total number of notaries matching the criteria | [optional] 

## Example

```python
from pandadoc_client.models.list_notaries_response import ListNotariesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListNotariesResponse from a JSON string
list_notaries_response_instance = ListNotariesResponse.from_json(json)
# print the JSON string representation of the object
print(ListNotariesResponse.to_json())

# convert the object into a dict
list_notaries_response_dict = list_notaries_response_instance.to_dict()
# create an instance of ListNotariesResponse from a dict
list_notaries_response_from_dict = ListNotariesResponse.from_dict(list_notaries_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


