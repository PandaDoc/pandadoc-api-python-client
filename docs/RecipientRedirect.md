# RecipientRedirect


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_enabled** | **bool** |  | [default to False]
**url** | **str** | A URL to redirect to after the document is signed. | 

## Example

```python
from pandadoc_client.models.recipient_redirect import RecipientRedirect

# TODO update the JSON string below
json = "{}"
# create an instance of RecipientRedirect from a JSON string
recipient_redirect_instance = RecipientRedirect.from_json(json)
# print the JSON string representation of the object
print(RecipientRedirect.to_json())

# convert the object into a dict
recipient_redirect_dict = recipient_redirect_instance.to_dict()
# create an instance of RecipientRedirect from a dict
recipient_redirect_from_dict = RecipientRedirect.from_dict(recipient_redirect_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


