# AuthUrlRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_id** | **str** |  | 
**redirect_uri** | **str** |  | 
**code_challenge** | **str** |  | 

## Example

```python
from ods_sdk_L3.models.auth_url_request import AuthUrlRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AuthUrlRequest from a JSON string
auth_url_request_instance = AuthUrlRequest.from_json(json)
# print the JSON string representation of the object
print(AuthUrlRequest.to_json())

# convert the object into a dict
auth_url_request_dict = auth_url_request_instance.to_dict()
# create an instance of AuthUrlRequest from a dict
auth_url_request_from_dict = AuthUrlRequest.from_dict(auth_url_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


