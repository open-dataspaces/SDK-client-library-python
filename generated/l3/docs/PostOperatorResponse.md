# PostOperatorResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**login_user_id** | **str** |  | [optional] 
**operator_id** | **str** |  | [optional] 
**operator_name** | **str** |  | [optional] 
**operator_address** | **str** |  | [optional] 
**open_operator_id** | **str** |  | [optional] 
**global_operator_id** | **str** |  | [optional] 
**effective_start_date** | **date** |  | [optional] 
**effective_end_date** | **date** |  | [optional] 
**deleted_flag** | **bool** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**password** | **str** |  | [optional] 

## Example

```python
from ods_sdk_L3.models.post_operator_response import PostOperatorResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PostOperatorResponse from a JSON string
post_operator_response_instance = PostOperatorResponse.from_json(json)
# print the JSON string representation of the object
print(PostOperatorResponse.to_json())

# convert the object into a dict
post_operator_response_dict = post_operator_response_instance.to_dict()
# create an instance of PostOperatorResponse from a dict
post_operator_response_from_dict = PostOperatorResponse.from_dict(post_operator_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


