# TokenPasswordRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_id** | **str** |  | 
**client_secret** | **str** |  | 
**login_user_id** | **str** |  | 
**password** | **str** |  | 

## Example

```python
from ods_sdk_L3.models.token_password_request import TokenPasswordRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TokenPasswordRequest from a JSON string
token_password_request_instance = TokenPasswordRequest.from_json(json)
# print the JSON string representation of the object
print(TokenPasswordRequest.to_json())

# convert the object into a dict
token_password_request_dict = token_password_request_instance.to_dict()
# create an instance of TokenPasswordRequest from a dict
token_password_request_from_dict = TokenPasswordRequest.from_dict(token_password_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


