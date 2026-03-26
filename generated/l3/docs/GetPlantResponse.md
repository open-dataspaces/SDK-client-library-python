# GetPlantResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operator_id** | **str** |  | [optional] 
**plant_id** | **str** |  | [optional] 
**open_plant_id** | **str** |  | [optional] 
**global_plant_id** | **str** |  | [optional] 
**plant_name** | **str** |  | [optional] 
**plant_address** | **str** |  | [optional] 
**effective_start_date** | **date** |  | [optional] 
**effective_end_date** | **date** |  | [optional] 
**deleted_flag** | **bool** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from ods_sdk_L3.models.get_plant_response import GetPlantResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetPlantResponse from a JSON string
get_plant_response_instance = GetPlantResponse.from_json(json)
# print the JSON string representation of the object
print(GetPlantResponse.to_json())

# convert the object into a dict
get_plant_response_dict = get_plant_response_instance.to_dict()
# create an instance of GetPlantResponse from a dict
get_plant_response_from_dict = GetPlantResponse.from_dict(get_plant_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


