# DocumentDetailsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Document ID. | [optional] 
**name** | **str** | Document name. | [optional] 
**autonumbering_sequence_name_prefix** | **object** |  | [optional] 
**folder_uuid** | **str** | ID of the folder where the created document should be stored. | [optional] 
**date_created** | **str** | Document creation date. | [optional] 
**date_modified** | **str** | Document modification date. | [optional] 
**date_completed** | **str** | Document completion date. | [optional] 
**content_date_modified** | **str** | Document content modification date. | [optional] 
**date_sent** | **str** | Document sent date. | [optional] 
**ref_number** | **str** | Document reference number. | [optional] 
**created_by** | [**DocumentDetailsResponseCreatedBy**](DocumentDetailsResponseCreatedBy.md) |  | [optional] 
**template** | [**DocumentDetailsResponseTemplate**](DocumentDetailsResponseTemplate.md) |  | [optional] 
**expiration_date** | **str** | Document expiration date. | [optional] 
**metadata** | **object** | Document metadata. | [optional] 
**tokens** | **List[object]** | Document tokens. | [optional] 
**fields** | [**List[ModelField]**](ModelField.md) | Document fields. | [optional] 
**pricing** | [**PricingResponse**](PricingResponse.md) |  | [optional] 
**tables** | [**List[DocumentDetailsResponseTablesInner]**](DocumentDetailsResponseTablesInner.md) | Document tables. | [optional] 
**images** | [**List[DocumentDetailsResponseImagesInner]**](DocumentDetailsResponseImagesInner.md) | Document images. | [optional] 
**texts** | [**List[DocumentDetailsResponseTextsInner]**](DocumentDetailsResponseTextsInner.md) | Document text blocks. | [optional] 
**tags** | **List[str]** | Document tags. | [optional] 
**sent_by** | **object** | Document sent by. | [optional] 
**recipients** | [**List[DocumentDetailsResponseRecipientsInner]**](DocumentDetailsResponseRecipientsInner.md) | Document recipients. | [optional] 
**grand_total** | [**DocumentDetailsResponseGrandTotal**](DocumentDetailsResponseGrandTotal.md) |  | [optional] 
**linked_objects** | [**List[DocumentDetailsResponseLinkedObjectsInner]**](DocumentDetailsResponseLinkedObjectsInner.md) | Document linked objects. | [optional] 
**status** | **str** | Document status. | [optional] 
**approval_execution** | [**DocumentDetailsResponseApprovalExecution**](DocumentDetailsResponseApprovalExecution.md) |  | [optional] 
**version** | **str** | Document version. | [optional] 

## Example

```python
from pandadoc_client.models.document_details_response import DocumentDetailsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentDetailsResponse from a JSON string
document_details_response_instance = DocumentDetailsResponse.from_json(json)
# print the JSON string representation of the object
print(DocumentDetailsResponse.to_json())

# convert the object into a dict
document_details_response_dict = document_details_response_instance.to_dict()
# create an instance of DocumentDetailsResponse from a dict
document_details_response_from_dict = DocumentDetailsResponse.from_dict(document_details_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


