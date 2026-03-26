# APIResponsePasswordUrlResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**title** | **str** |  | 
**status** | **int** |  | [optional] 
**detail** | **str** |  | 
**data** | [**PasswordUrlResponse**](PasswordUrlResponse.md) |  | 

## Example

```python
from ods_sdk_L3.models.api_response_password_url_response import APIResponsePasswordUrlResponse

# TODO update the JSON string below
json = "{}"
# create an instance of APIResponsePasswordUrlResponse from a JSON string
api_response_password_url_response_instance = APIResponsePasswordUrlResponse.from_json(json)
# print the JSON string representation of the object
print(APIResponsePasswordUrlResponse.to_json())

# convert the object into a dict
api_response_password_url_response_dict = api_response_password_url_response_instance.to_dict()
# create an instance of APIResponsePasswordUrlResponse from a dict
api_response_password_url_response_from_dict = APIResponsePasswordUrlResponse.from_dict(api_response_password_url_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


