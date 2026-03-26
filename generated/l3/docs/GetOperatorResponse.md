# GetOperatorResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
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

## Example

```python
from ods_sdk_L3.models.get_operator_response import GetOperatorResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetOperatorResponse from a JSON string
get_operator_response_instance = GetOperatorResponse.from_json(json)
# print the JSON string representation of the object
print(GetOperatorResponse.to_json())

# convert the object into a dict
get_operator_response_dict = get_operator_response_instance.to_dict()
# create an instance of GetOperatorResponse from a dict
get_operator_response_from_dict = GetOperatorResponse.from_dict(get_operator_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


