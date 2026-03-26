# TokenPasswordResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token** | **str** |  | [optional] 
**expires_in** | **int** |  | [optional] 
**token_type** | **str** |  | [optional] 
**not_before_policy** | **int** |  | [optional] 
**scope** | **str** |  | [optional] 
**refresh_token** | **str** |  | [optional] 
**refresh_expires_in** | **int** |  | [optional] 

## Example

```python
from ods_sdk_L3.models.token_password_response import TokenPasswordResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TokenPasswordResponse from a JSON string
token_password_response_instance = TokenPasswordResponse.from_json(json)
# print the JSON string representation of the object
print(TokenPasswordResponse.to_json())

# convert the object into a dict
token_password_response_dict = token_password_response_instance.to_dict()
# create an instance of TokenPasswordResponse from a dict
token_password_response_from_dict = TokenPasswordResponse.from_dict(token_password_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


