# APIResponseAuthUrlResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**title** | **str** |  | 
**status** | **int** |  | [optional] 
**detail** | **str** |  | 
**data** | [**AuthUrlResponse**](AuthUrlResponse.md) |  | 

## Example

```python
from ods_sdk_L3.models.api_response_auth_url_response import APIResponseAuthUrlResponse

# TODO update the JSON string below
json = "{}"
# create an instance of APIResponseAuthUrlResponse from a JSON string
api_response_auth_url_response_instance = APIResponseAuthUrlResponse.from_json(json)
# print the JSON string representation of the object
print(APIResponseAuthUrlResponse.to_json())

# convert the object into a dict
api_response_auth_url_response_dict = api_response_auth_url_response_instance.to_dict()
# create an instance of APIResponseAuthUrlResponse from a dict
api_response_auth_url_response_from_dict = APIResponseAuthUrlResponse.from_dict(api_response_auth_url_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


