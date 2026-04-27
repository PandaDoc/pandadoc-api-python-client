# BaseActor


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role** | **str** | A recipient&#39;s role in the document from the template. A recipient will be added in CC if a role parameter is not provided. | [optional] 
**signing_order** | **int** | Set a signing order for a recipient. Learn more: https://developers.pandadoc.com/docs/set-signing-order  | [optional] 

## Example

```python
from pandadoc_client.models.base_actor import BaseActor

# TODO update the JSON string below
json = "{}"
# create an instance of BaseActor from a JSON string
base_actor_instance = BaseActor.from_json(json)
# print the JSON string representation of the object
print(BaseActor.to_json())

# convert the object into a dict
base_actor_dict = base_actor_instance.to_dict()
# create an instance of BaseActor from a dict
base_actor_from_dict = BaseActor.from_dict(base_actor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


