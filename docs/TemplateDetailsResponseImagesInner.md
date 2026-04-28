# TemplateDetailsResponseImagesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**block_uuid** | **str** |  | [optional] 
**urls** | **List[str]** |  | [optional] 

## Example

```python
from pandadoc_client.models.template_details_response_images_inner import TemplateDetailsResponseImagesInner

# TODO update the JSON string below
json = "{}"
# create an instance of TemplateDetailsResponseImagesInner from a JSON string
template_details_response_images_inner_instance = TemplateDetailsResponseImagesInner.from_json(json)
# print the JSON string representation of the object
print(TemplateDetailsResponseImagesInner.to_json())

# convert the object into a dict
template_details_response_images_inner_dict = template_details_response_images_inner_instance.to_dict()
# create an instance of TemplateDetailsResponseImagesInner from a dict
template_details_response_images_inner_from_dict = TemplateDetailsResponseImagesInner.from_dict(template_details_response_images_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


