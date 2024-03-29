# UploadSectionByTemplateRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**template_uuid** | **str** | The ID of a template you want to use. You can copy it from an in app template url such as &#x60;https://app.pandadoc.com/a/#/templates/{ID}/content&#x60;. A template ID is also obtained by listing templates. | 
**recipients** | [**[DocumentCreateByTemplateRequestRecipients]**](DocumentCreateByTemplateRequestRecipients.md) | The list of recipients you&#39;re sending the document to. Every object must contain the email parameter. The &#x60;role&#x60;, &#x60;first_name&#x60; and &#x60;last_name&#x60; parameters are optional. If the &#x60;role&#x60; parameter passed, a person is assigned all fields matching their corresponding role. If not passed, a person will receive a read-only link to view the document. If the &#x60;first_name&#x60; and &#x60;last_name&#x60; not passed the system 1. creates a new contact, if none exists with the given &#x60;email&#x60;; or 2. gets the existing contact with the given &#x60;email&#x60; that already exists. | 
**tokens** | [**[DocumentCreateByTemplateRequestTokens]**](DocumentCreateByTemplateRequestTokens.md) | You can pass a list of tokens/values to pre-fill tokens used in a template. Name is a token name in a template. Value is a real value you would like to replace a token with. | [optional] 
**fields** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | You can pass a list of fields/values to pre-fill fields used in a template. Note that the Signature field can&#39;t be pre-filled. | [optional] 
**pricing_tables** | [**[PricingTableRequest]**](PricingTableRequest.md) | Information to construct or populate a pricing table can be passed when creating a document. All product information must be passed when creating a new document. Products stored in PandaDoc cannot be used to populate table rows at this time. Keep in mind that this is an array, so multiple table objects can be passed to a document. Make sure that \&quot;Automatically add products to this table\&quot; is enabled in the PandaDoc template pricing tables you wish to populate via API. | [optional] 
**content_placeholders** | [**[DocumentCreateByTemplateRequestContentPlaceholders]**](DocumentCreateByTemplateRequestContentPlaceholders.md) | You may replace Content Library Item Placeholders with a few content library items each and pre-fill fields/variables values, pricing table items, and assign recipients to roles from there. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


