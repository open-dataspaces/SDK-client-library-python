# PostOperatorRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**login_user_id** | **str** |  | 
**operator_name** | **str** |  | 
**operator_address** | **str** |  | 
**open_operator_id** | **str** |  | 
**global_operator_id** | **str** |  | [optional] 
**effective_start_date** | **str** |  | [optional] 
**effective_end_date** | **str** |  | [optional] 
**create_password_flag** | **bool** |  | [optional] 
**password_temporary_flag** | **bool** |  | [optional] 

## Example

```python
from ods_sdk_L3.models.post_operator_request import PostOperatorRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostOperatorRequest from a JSON string
post_operator_request_instance = PostOperatorRequest.from_json(json)
# print the JSON string representation of the object
print(PostOperatorRequest.to_json())

# convert the object into a dict
post_operator_request_dict = post_operator_request_instance.to_dict()
# create an instance of PostOperatorRequest from a dict
post_operator_request_from_dict = PostOperatorRequest.from_dict(post_operator_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


