# APIResponseListGetOperatorResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**title** | **str** |  | 
**status** | **int** |  | [optional] 
**detail** | **str** |  | 
**data** | [**List[GetOperatorResponse]**](GetOperatorResponse.md) |  | 

## Example

```python
from ods_sdk_L3.models.api_response_list_get_operator_response import APIResponseListGetOperatorResponse

# TODO update the JSON string below
json = "{}"
# create an instance of APIResponseListGetOperatorResponse from a JSON string
api_response_list_get_operator_response_instance = APIResponseListGetOperatorResponse.from_json(json)
# print the JSON string representation of the object
print(APIResponseListGetOperatorResponse.to_json())

# convert the object into a dict
api_response_list_get_operator_response_dict = api_response_list_get_operator_response_instance.to_dict()
# create an instance of APIResponseListGetOperatorResponse from a dict
api_response_list_get_operator_response_from_dict = APIResponseListGetOperatorResponse.from_dict(api_response_list_get_operator_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


