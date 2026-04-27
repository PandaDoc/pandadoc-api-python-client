# CreateTemplateFromUrlRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the template. | [optional] 
**folder_uuid** | **str** | The ID of the folder where the created template should be stored. | [optional] 
**owner** | [**CreateTemplateRequestOwner**](CreateTemplateRequestOwner.md) |  | [optional] 
**metadata** | **object** | You can pass arbitrary data in the key-value format to associate custom information with a template. This information is returned in any API requests for the template details by id. | [optional] 
**tokens** | [**List[DocumentUpdateRequestTokensInner]**](DocumentUpdateRequestTokensInner.md) | Create or initialize multiple CUSTOM variables with their values using tokens/values list. Template&#39;s predefined variables are read-only. Any attempts to do so will be ignored. | [optional] 
**url** | **str** | Secure (HTTPS) and publicly accessible URL to the PDF document. | [optional] 

## Example

```python
from pandadoc_client.models.create_template_from_url_request import CreateTemplateFromUrlRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTemplateFromUrlRequest from a JSON string
create_template_from_url_request_instance = CreateTemplateFromUrlRequest.from_json(json)
# print the JSON string representation of the object
print(CreateTemplateFromUrlRequest.to_json())

# convert the object into a dict
create_template_from_url_request_dict = create_template_from_url_request_instance.to_dict()
# create an instance of CreateTemplateFromUrlRequest from a dict
create_template_from_url_request_from_dict = CreateTemplateFromUrlRequest.from_dict(create_template_from_url_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


