# DocumentDetailsResponseGrandTotal

Document grand total.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **str** | Total amount. | [optional] 
**currency** | **str** | Currency type. | [optional] 

## Example

```python
from pandadoc_client.models.document_details_response_grand_total import DocumentDetailsResponseGrandTotal

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentDetailsResponseGrandTotal from a JSON string
document_details_response_grand_total_instance = DocumentDetailsResponseGrandTotal.from_json(json)
# print the JSON string representation of the object
print(DocumentDetailsResponseGrandTotal.to_json())

# convert the object into a dict
document_details_response_grand_total_dict = document_details_response_grand_total_instance.to_dict()
# create an instance of DocumentDetailsResponseGrandTotal from a dict
document_details_response_grand_total_from_dict = DocumentDetailsResponseGrandTotal.from_dict(document_details_response_grand_total_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


