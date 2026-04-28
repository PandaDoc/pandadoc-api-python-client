# EditingSessionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | Email of the user to create the editing session for | 
**lifetime** | **int** | Lifetime of the E-Token in seconds. | [optional] [default to 3600]

## Example

```python
from pandadoc_client.models.editing_session_request import EditingSessionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EditingSessionRequest from a JSON string
editing_session_request_instance = EditingSessionRequest.from_json(json)
# print the JSON string representation of the object
print(EditingSessionRequest.to_json())

# convert the object into a dict
editing_session_request_dict = editing_session_request_instance.to_dict()
# create an instance of EditingSessionRequest from a dict
editing_session_request_from_dict = EditingSessionRequest.from_dict(editing_session_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


