# APIResponseTokenPasswordResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**title** | **str** |  | 
**status** | **int** |  | [optional] 
**detail** | **str** |  | 
**data** | [**TokenPasswordResponse**](TokenPasswordResponse.md) |  | 

## Example

```python
from ods_sdk_L3.models.api_response_token_password_response import APIResponseTokenPasswordResponse

# TODO update the JSON string below
json = "{}"
# create an instance of APIResponseTokenPasswordResponse from a JSON string
api_response_token_password_response_instance = APIResponseTokenPasswordResponse.from_json(json)
# print the JSON string representation of the object
print(APIResponseTokenPasswordResponse.to_json())

# convert the object into a dict
api_response_token_password_response_dict = api_response_token_password_response_instance.to_dict()
# create an instance of APIResponseTokenPasswordResponse from a dict
api_response_token_password_response_from_dict = APIResponseTokenPasswordResponse.from_dict(api_response_token_password_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


