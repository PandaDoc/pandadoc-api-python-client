# NotarizationRequestDetailsResponseRecording


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | Secure URL to download video recording of the notarization session. | [optional] 
**name** | **str** | Name of the video recording file. | [optional] 
**size** | **float** | Size of the video recording file in bytes. | [optional] 

## Example

```python
from pandadoc_client.models.notarization_request_details_response_recording import NotarizationRequestDetailsResponseRecording

# TODO update the JSON string below
json = "{}"
# create an instance of NotarizationRequestDetailsResponseRecording from a JSON string
notarization_request_details_response_recording_instance = NotarizationRequestDetailsResponseRecording.from_json(json)
# print the JSON string representation of the object
print(NotarizationRequestDetailsResponseRecording.to_json())

# convert the object into a dict
notarization_request_details_response_recording_dict = notarization_request_details_response_recording_instance.to_dict()
# create an instance of NotarizationRequestDetailsResponseRecording from a dict
notarization_request_details_response_recording_from_dict = NotarizationRequestDetailsResponseRecording.from_dict(notarization_request_details_response_recording_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


