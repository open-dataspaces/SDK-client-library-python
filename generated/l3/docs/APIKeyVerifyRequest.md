# APIKeyVerifyRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**verify_apikey** | **str** |  | 

## Example

```python
from ods_sdk_L3.models.api_key_verify_request import APIKeyVerifyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of APIKeyVerifyRequest from a JSON string
api_key_verify_request_instance = APIKeyVerifyRequest.from_json(json)
# print the JSON string representation of the object
print(APIKeyVerifyRequest.to_json())

# convert the object into a dict
api_key_verify_request_dict = api_key_verify_request_instance.to_dict()
# create an instance of APIKeyVerifyRequest from a dict
api_key_verify_request_from_dict = APIKeyVerifyRequest.from_dict(api_key_verify_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


