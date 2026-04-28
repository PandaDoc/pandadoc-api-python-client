# CreateNotarizationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | A unique identifier of the notarization request. | [optional] 
**name** | **str** | A name of the notarization request. | [optional] 
**status** | **str** | Current status of the notarization request. | [optional] 
**date_created** | **datetime** | A date when a notarization request was created. | [optional] 
**date_accepted** | **datetime** | A date when a notarization session was accepted by notary. | [optional] 
**created_by** | [**CreateNotarizationResponseCreatedBy**](CreateNotarizationResponseCreatedBy.md) |  | [optional] 
**invitees** | [**List[CreateNotarizationResponseInviteesInner]**](CreateNotarizationResponseInviteesInner.md) |  | [optional] 

## Example

```python
from pandadoc_client.models.create_notarization_response import CreateNotarizationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateNotarizationResponse from a JSON string
create_notarization_response_instance = CreateNotarizationResponse.from_json(json)
# print the JSON string representation of the object
print(CreateNotarizationResponse.to_json())

# convert the object into a dict
create_notarization_response_dict = create_notarization_response_instance.to_dict()
# create an instance of CreateNotarizationResponse from a dict
create_notarization_response_from_dict = CreateNotarizationResponse.from_dict(create_notarization_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


