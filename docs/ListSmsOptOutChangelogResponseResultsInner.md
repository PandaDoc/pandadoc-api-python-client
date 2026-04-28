# ListSmsOptOutChangelogResponseResultsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**phone_number** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**opt_out_changed** | **datetime** |  | [optional] 

## Example

```python
from pandadoc_client.models.list_sms_opt_out_changelog_response_results_inner import ListSmsOptOutChangelogResponseResultsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ListSmsOptOutChangelogResponseResultsInner from a JSON string
list_sms_opt_out_changelog_response_results_inner_instance = ListSmsOptOutChangelogResponseResultsInner.from_json(json)
# print the JSON string representation of the object
print(ListSmsOptOutChangelogResponseResultsInner.to_json())

# convert the object into a dict
list_sms_opt_out_changelog_response_results_inner_dict = list_sms_opt_out_changelog_response_results_inner_instance.to_dict()
# create an instance of ListSmsOptOutChangelogResponseResultsInner from a dict
list_sms_opt_out_changelog_response_results_inner_from_dict = ListSmsOptOutChangelogResponseResultsInner.from_dict(list_sms_opt_out_changelog_response_results_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


