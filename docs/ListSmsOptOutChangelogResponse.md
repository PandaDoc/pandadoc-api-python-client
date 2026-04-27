# ListSmsOptOutChangelogResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[ListSmsOptOutChangelogResponseResultsInner]**](ListSmsOptOutChangelogResponseResultsInner.md) |  | [optional] 

## Example

```python
from pandadoc_client.models.list_sms_opt_out_changelog_response import ListSmsOptOutChangelogResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListSmsOptOutChangelogResponse from a JSON string
list_sms_opt_out_changelog_response_instance = ListSmsOptOutChangelogResponse.from_json(json)
# print the JSON string representation of the object
print(ListSmsOptOutChangelogResponse.to_json())

# convert the object into a dict
list_sms_opt_out_changelog_response_dict = list_sms_opt_out_changelog_response_instance.to_dict()
# create an instance of ListSmsOptOutChangelogResponse from a dict
list_sms_opt_out_changelog_response_from_dict = ListSmsOptOutChangelogResponse.from_dict(list_sms_opt_out_changelog_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


