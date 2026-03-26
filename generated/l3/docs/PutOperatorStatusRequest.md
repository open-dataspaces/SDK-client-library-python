# PutOperatorStatusRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**updated_at** | **str** |  | 
**effective_start_date** | **str** |  | [optional] 
**effective_end_date** | **str** |  | [optional] 
**deleted_flag** | **bool** |  | [optional] 

## Example

```python
from ods_sdk_L3.models.put_operator_status_request import PutOperatorStatusRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PutOperatorStatusRequest from a JSON string
put_operator_status_request_instance = PutOperatorStatusRequest.from_json(json)
# print the JSON string representation of the object
print(PutOperatorStatusRequest.to_json())

# convert the object into a dict
put_operator_status_request_dict = put_operator_status_request_instance.to_dict()
# create an instance of PutOperatorStatusRequest from a dict
put_operator_status_request_from_dict = PutOperatorStatusRequest.from_dict(put_operator_status_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


