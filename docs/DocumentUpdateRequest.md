# DocumentUpdateRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the document. | [optional] 
**recipients** | [**[DocumentUpdateRequestRecipients]**](DocumentUpdateRequestRecipients.md) | The list of recipients you&#39;re sending the document to. The ID or email are required. If the ID is passed, an existing recipient will be updated. If the email is passed, a new recipient will be added to CC. | [optional] 
**fields** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | You may pass a list of fields/values which exist in a document. Please use &#x60;Merge Field&#x60; property of the fields like the key. | [optional] 
**tokens** | [**[DocumentCreateByTemplateRequestTokens]**](DocumentCreateByTemplateRequestTokens.md) | You can pass a list of tokens/values. If a token name exists in a document then the value will be updated. Otherwise, a new token will be added to the document. | [optional] 
**metadata** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | You can pass arbitrary data in the key-value format to associate custom information with a document. This information is returned in any API requests for the document details by id. If metadata exists in a document then the value will be updated. Otherwise, metadata will be added to the document. | [optional] 
**pricing_tables** | [**[PricingTableRequest]**](PricingTableRequest.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


