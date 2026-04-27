# NotarizationRequestDetailsResponseCreatedBy


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** | A unique identifier of the user who created a notarization request. | [optional] 
**email** | **str** | A user&#39;s email address. | [optional] 
**first_name** | **str** | A user&#39;s first name. | [optional] 
**last_name** | **str** | A user&#39;s last name. | [optional] 

## Example

```python
from pandadoc_client.models.notarization_request_details_response_created_by import NotarizationRequestDetailsResponseCreatedBy

# TODO update the JSON string below
json = "{}"
# create an instance of NotarizationRequestDetailsResponseCreatedBy from a JSON string
notarization_request_details_response_created_by_instance = NotarizationRequestDetailsResponseCreatedBy.from_json(json)
# print the JSON string representation of the object
print(NotarizationRequestDetailsResponseCreatedBy.to_json())

# convert the object into a dict
notarization_request_details_response_created_by_dict = notarization_request_details_response_created_by_instance.to_dict()
# create an instance of NotarizationRequestDetailsResponseCreatedBy from a dict
notarization_request_details_response_created_by_from_dict = NotarizationRequestDetailsResponseCreatedBy.from_dict(notarization_request_details_response_created_by_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


