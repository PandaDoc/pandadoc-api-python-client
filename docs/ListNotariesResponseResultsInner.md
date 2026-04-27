# ListNotariesResponseResultsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the notary | [optional] 
**email** | **str** | Email address of the notary | [optional] 
**name** | **str** | Full name of the notary | [optional] 
**status** | **str** | Current status of the notary | [optional] 
**commission_state** | **str** |  | [optional] 

## Example

```python
from pandadoc_client.models.list_notaries_response_results_inner import ListNotariesResponseResultsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ListNotariesResponseResultsInner from a JSON string
list_notaries_response_results_inner_instance = ListNotariesResponseResultsInner.from_json(json)
# print the JSON string representation of the object
print(ListNotariesResponseResultsInner.to_json())

# convert the object into a dict
list_notaries_response_results_inner_dict = list_notaries_response_results_inner_instance.to_dict()
# create an instance of ListNotariesResponseResultsInner from a dict
list_notaries_response_results_inner_from_dict = ListNotariesResponseResultsInner.from_dict(list_notaries_response_results_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


