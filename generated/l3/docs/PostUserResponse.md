# PostUserResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**login_user_id** | **str** |  | [optional] 
**operator_id** | **str** |  | [optional] 
**password** | **str** |  | [optional] 

## Example

```python
from ods_sdk_L3.models.post_user_response import PostUserResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PostUserResponse from a JSON string
post_user_response_instance = PostUserResponse.from_json(json)
# print the JSON string representation of the object
print(PostUserResponse.to_json())

# convert the object into a dict
post_user_response_dict = post_user_response_instance.to_dict()
# create an instance of PostUserResponse from a dict
post_user_response_from_dict = PostUserResponse.from_dict(post_user_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


