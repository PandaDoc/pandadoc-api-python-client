# FormListResponseResultsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**date_created** | **str** |  | [optional] 
**date_modified** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from pandadoc_client.models.form_list_response_results_inner import FormListResponseResultsInner

# TODO update the JSON string below
json = "{}"
# create an instance of FormListResponseResultsInner from a JSON string
form_list_response_results_inner_instance = FormListResponseResultsInner.from_json(json)
# print the JSON string representation of the object
print(FormListResponseResultsInner.to_json())

# convert the object into a dict
form_list_response_results_inner_dict = form_list_response_results_inner_instance.to_dict()
# create an instance of FormListResponseResultsInner from a dict
form_list_response_results_inner_from_dict = FormListResponseResultsInner.from_dict(form_list_response_results_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


