# MemberListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[MemberDetailsResponse]**](MemberDetailsResponse.md) |  | [optional] 

## Example

```python
from pandadoc_client.models.member_list_response import MemberListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MemberListResponse from a JSON string
member_list_response_instance = MemberListResponse.from_json(json)
# print the JSON string representation of the object
print(MemberListResponse.to_json())

# convert the object into a dict
member_list_response_dict = member_list_response_instance.to_dict()
# create an instance of MemberListResponse from a dict
member_list_response_from_dict = MemberListResponse.from_dict(member_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


