# DocumentDetailsResponseTemplate

Document template details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Template ID. | [optional] 
**name** | **str** | Template name. | [optional] 

## Example

```python
from pandadoc_client.models.document_details_response_template import DocumentDetailsResponseTemplate

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentDetailsResponseTemplate from a JSON string
document_details_response_template_instance = DocumentDetailsResponseTemplate.from_json(json)
# print the JSON string representation of the object
print(DocumentDetailsResponseTemplate.to_json())

# convert the object into a dict
document_details_response_template_dict = document_details_response_template_instance.to_dict()
# create an instance of DocumentDetailsResponseTemplate from a dict
document_details_response_template_from_dict = DocumentDetailsResponseTemplate.from_dict(document_details_response_template_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


