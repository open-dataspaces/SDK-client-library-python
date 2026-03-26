# APIResponseTokenRefreshResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**title** | **str** |  | 
**status** | **int** |  | [optional] 
**detail** | **str** |  | 
**data** | [**TokenRefreshResponse**](TokenRefreshResponse.md) |  | 

## Example

```python
from ods_sdk_L3.models.api_response_token_refresh_response import APIResponseTokenRefreshResponse

# TODO update the JSON string below
json = "{}"
# create an instance of APIResponseTokenRefreshResponse from a JSON string
api_response_token_refresh_response_instance = APIResponseTokenRefreshResponse.from_json(json)
# print the JSON string representation of the object
print(APIResponseTokenRefreshResponse.to_json())

# convert the object into a dict
api_response_token_refresh_response_dict = api_response_token_refresh_response_instance.to_dict()
# create an instance of APIResponseTokenRefreshResponse from a dict
api_response_token_refresh_response_from_dict = APIResponseTokenRefreshResponse.from_dict(api_response_token_refresh_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


