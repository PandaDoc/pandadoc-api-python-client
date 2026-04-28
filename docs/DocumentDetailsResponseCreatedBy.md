# DocumentDetailsResponseCreatedBy

Document creator details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Creator ID. | [optional] 
**membership_id** | **str** | Creator membership ID. | [optional] 
**email** | **str** | Creator email. | [optional] 
**first_name** | **str** | Creator first name. | [optional] 
**last_name** | **str** | Creator last name. | [optional] 
**avatar** | **str** | Creator avatar URL. | [optional] 

## Example

```python
from pandadoc_client.models.document_details_response_created_by import DocumentDetailsResponseCreatedBy

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentDetailsResponseCreatedBy from a JSON string
document_details_response_created_by_instance = DocumentDetailsResponseCreatedBy.from_json(json)
# print the JSON string representation of the object
print(DocumentDetailsResponseCreatedBy.to_json())

# convert the object into a dict
document_details_response_created_by_dict = document_details_response_created_by_instance.to_dict()
# create an instance of DocumentDetailsResponseCreatedBy from a dict
document_details_response_created_by_from_dict = DocumentDetailsResponseCreatedBy.from_dict(document_details_response_created_by_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


