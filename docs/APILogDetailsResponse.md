# APILogDetailsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**method** | **str** |  | [optional] 
**status** | **int** |  | [optional] 
**request_time** | **str** |  | [optional] 
**response_time** | **str** |  | [optional] 
**response_body** | **object** |  | [optional] 
**query_params_string** | **str** |  | [optional] 
**query_params_object** | **object** |  | [optional] 
**request_body** | **object** |  | [optional] 
**token_type** | **str** |  | [optional] 
**application** | **str** |  | [optional] 
**key** | **str** |  | [optional] 
**request_id** | **str** |  | [optional] 
**user_email** | **str** |  | [optional] 
**user_id** | **str** |  | [optional] 

## Example

```python
from pandadoc_client.models.api_log_details_response import APILogDetailsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of APILogDetailsResponse from a JSON string
api_log_details_response_instance = APILogDetailsResponse.from_json(json)
# print the JSON string representation of the object
print(APILogDetailsResponse.to_json())

# convert the object into a dict
api_log_details_response_dict = api_log_details_response_instance.to_dict()
# create an instance of APILogDetailsResponse from a dict
api_log_details_response_from_dict = APILogDetailsResponse.from_dict(api_log_details_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


