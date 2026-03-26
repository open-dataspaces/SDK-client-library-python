# APIResponseAuthTokenResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**title** | **str** |  | 
**status** | **int** |  | [optional] 
**detail** | **str** |  | 
**data** | [**AuthTokenResponse**](AuthTokenResponse.md) |  | 

## Example

```python
from ods_sdk_L3.models.api_response_auth_token_response import APIResponseAuthTokenResponse

# TODO update the JSON string below
json = "{}"
# create an instance of APIResponseAuthTokenResponse from a JSON string
api_response_auth_token_response_instance = APIResponseAuthTokenResponse.from_json(json)
# print the JSON string representation of the object
print(APIResponseAuthTokenResponse.to_json())

# convert the object into a dict
api_response_auth_token_response_dict = api_response_auth_token_response_instance.to_dict()
# create an instance of APIResponseAuthTokenResponse from a dict
api_response_auth_token_response_from_dict = APIResponseAuthTokenResponse.from_dict(api_response_auth_token_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


