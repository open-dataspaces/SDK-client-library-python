# TokenClientResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token** | **str** |  | [optional] 
**expires_in** | **int** |  | [optional] 
**token_type** | **str** |  | [optional] 
**not_before_policy** | **int** |  | [optional] 
**scope** | **str** |  | [optional] 

## Example

```python
from ods_sdk_L3.models.token_client_response import TokenClientResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TokenClientResponse from a JSON string
token_client_response_instance = TokenClientResponse.from_json(json)
# print the JSON string representation of the object
print(TokenClientResponse.to_json())

# convert the object into a dict
token_client_response_dict = token_client_response_instance.to_dict()
# create an instance of TokenClientResponse from a dict
token_client_response_from_dict = TokenClientResponse.from_dict(token_client_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


