# APIKeyVerifyResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**verify_result** | **bool** |  | [optional] 

## Example

```python
from ods_sdk_L3.models.api_key_verify_response import APIKeyVerifyResponse

# TODO update the JSON string below
json = "{}"
# create an instance of APIKeyVerifyResponse from a JSON string
api_key_verify_response_instance = APIKeyVerifyResponse.from_json(json)
# print the JSON string representation of the object
print(APIKeyVerifyResponse.to_json())

# convert the object into a dict
api_key_verify_response_dict = api_key_verify_response_instance.to_dict()
# create an instance of APIKeyVerifyResponse from a dict
api_key_verify_response_from_dict = APIKeyVerifyResponse.from_dict(api_key_verify_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


