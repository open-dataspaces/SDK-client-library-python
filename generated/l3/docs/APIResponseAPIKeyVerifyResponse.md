# APIResponseAPIKeyVerifyResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**title** | **str** |  | 
**status** | **int** |  | [optional] 
**detail** | **str** |  | 
**data** | [**APIKeyVerifyResponse**](APIKeyVerifyResponse.md) |  | 

## Example

```python
from ods_sdk_L3.models.api_response_api_key_verify_response import APIResponseAPIKeyVerifyResponse

# TODO update the JSON string below
json = "{}"
# create an instance of APIResponseAPIKeyVerifyResponse from a JSON string
api_response_api_key_verify_response_instance = APIResponseAPIKeyVerifyResponse.from_json(json)
# print the JSON string representation of the object
print(APIResponseAPIKeyVerifyResponse.to_json())

# convert the object into a dict
api_response_api_key_verify_response_dict = api_response_api_key_verify_response_instance.to_dict()
# create an instance of APIResponseAPIKeyVerifyResponse from a dict
api_response_api_key_verify_response_from_dict = APIResponseAPIKeyVerifyResponse.from_dict(api_response_api_key_verify_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


