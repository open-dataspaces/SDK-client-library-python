# PasswordUrlRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_id** | **str** |  | 
**redirect_uri** | **str** |  | 
**code_challenge** | **str** |  | 

## Example

```python
from ods_sdk_L3.models.password_url_request import PasswordUrlRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PasswordUrlRequest from a JSON string
password_url_request_instance = PasswordUrlRequest.from_json(json)
# print the JSON string representation of the object
print(PasswordUrlRequest.to_json())

# convert the object into a dict
password_url_request_dict = password_url_request_instance.to_dict()
# create an instance of PasswordUrlRequest from a dict
password_url_request_from_dict = PasswordUrlRequest.from_dict(password_url_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


