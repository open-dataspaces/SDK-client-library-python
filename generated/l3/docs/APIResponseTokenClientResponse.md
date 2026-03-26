# APIResponseTokenClientResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**title** | **str** |  | 
**status** | **int** |  | [optional] 
**detail** | **str** |  | 
**data** | [**TokenClientResponse**](TokenClientResponse.md) |  | 

## Example

```python
from ods_sdk_L3.models.api_response_token_client_response import APIResponseTokenClientResponse

# TODO update the JSON string below
json = "{}"
# create an instance of APIResponseTokenClientResponse from a JSON string
api_response_token_client_response_instance = APIResponseTokenClientResponse.from_json(json)
# print the JSON string representation of the object
print(APIResponseTokenClientResponse.to_json())

# convert the object into a dict
api_response_token_client_response_dict = api_response_token_client_response_instance.to_dict()
# create an instance of APIResponseTokenClientResponse from a dict
api_response_token_client_response_from_dict = APIResponseTokenClientResponse.from_dict(api_response_token_client_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


