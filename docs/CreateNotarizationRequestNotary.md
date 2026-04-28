# CreateNotarizationRequestNotary

Optional notary assignment for in-house notary requests. Used for Bring you own notary use case. Only ACTIVE notaries can be used

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID of an ACTIVE notary | 
**scheduled_at** | **datetime** | ISO 8601 timestamp for scheduled notarization | 
**message** | **str** | Optional custom message for the notary in the invitation email | [optional] 

## Example

```python
from pandadoc_client.models.create_notarization_request_notary import CreateNotarizationRequestNotary

# TODO update the JSON string below
json = "{}"
# create an instance of CreateNotarizationRequestNotary from a JSON string
create_notarization_request_notary_instance = CreateNotarizationRequestNotary.from_json(json)
# print the JSON string representation of the object
print(CreateNotarizationRequestNotary.to_json())

# convert the object into a dict
create_notarization_request_notary_dict = create_notarization_request_notary_instance.to_dict()
# create an instance of CreateNotarizationRequestNotary from a dict
create_notarization_request_notary_from_dict = CreateNotarizationRequestNotary.from_dict(create_notarization_request_notary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


