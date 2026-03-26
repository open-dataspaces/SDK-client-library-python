# AuthTokenResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token** | **str** |  | 
**expires_in** | **int** |  | [optional] 
**token_type** | **str** |  | 
**not_before_policy** | **int** |  | [optional] 
**scope** | **str** |  | 
**refresh_token** | **str** |  | 
**refresh_expires_in** | **int** |  | [optional] 
**id_token** | **str** |  | 

## Example

```python
from ods_sdk_L3.models.auth_token_response import AuthTokenResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AuthTokenResponse from a JSON string
auth_token_response_instance = AuthTokenResponse.from_json(json)
# print the JSON string representation of the object
print(AuthTokenResponse.to_json())

# convert the object into a dict
auth_token_response_dict = auth_token_response_instance.to_dict()
# create an instance of AuthTokenResponse from a dict
auth_token_response_from_dict = AuthTokenResponse.from_dict(auth_token_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


