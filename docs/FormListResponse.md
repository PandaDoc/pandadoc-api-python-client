# FormListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[FormListResponseResultsInner]**](FormListResponseResultsInner.md) |  | [optional] 
**has_next_page** | **bool** |  | [optional] 

## Example

```python
from pandadoc_client.models.form_list_response import FormListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FormListResponse from a JSON string
form_list_response_instance = FormListResponse.from_json(json)
# print the JSON string representation of the object
print(FormListResponse.to_json())

# convert the object into a dict
form_list_response_dict = form_list_response_instance.to_dict()
# create an instance of FormListResponse from a dict
form_list_response_from_dict = FormListResponse.from_dict(form_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


