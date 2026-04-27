# CreateNotarizationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**document_id** | **str** | ID of the Document for notarization. | 
**disable_invitees_notifications** | **bool** | Disable all notifications for invitees including email with invitation for notarization. This is useful when you are using alternative delivery methods. | [optional] [default to False]
**invitation** | [**CreateNotarizationRequestInvitation**](CreateNotarizationRequestInvitation.md) |  | 
**notary** | [**CreateNotarizationRequestNotary**](CreateNotarizationRequestNotary.md) |  | [optional] 

## Example

```python
from pandadoc_client.models.create_notarization_request import CreateNotarizationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateNotarizationRequest from a JSON string
create_notarization_request_instance = CreateNotarizationRequest.from_json(json)
# print the JSON string representation of the object
print(CreateNotarizationRequest.to_json())

# convert the object into a dict
create_notarization_request_dict = create_notarization_request_instance.to_dict()
# create an instance of CreateNotarizationRequest from a dict
create_notarization_request_from_dict = CreateNotarizationRequest.from_dict(create_notarization_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


