# PasswordRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**old_password** | **str** |  | 
**new_password** | **str** |  | 

## Example

```python
from ods_sdk_L3.models.password_request import PasswordRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PasswordRequest from a JSON string
password_request_instance = PasswordRequest.from_json(json)
# print the JSON string representation of the object
print(PasswordRequest.to_json())

# convert the object into a dict
password_request_dict = password_request_instance.to_dict()
# create an instance of PasswordRequest from a dict
password_request_from_dict = PasswordRequest.from_dict(password_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


