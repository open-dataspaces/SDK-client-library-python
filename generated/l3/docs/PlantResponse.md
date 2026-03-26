# PlantResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**plant_id** | **str** |  | 
**operator_id** | **str** |  | 
**plant_name** | **str** |  | 
**plant_address** | **str** |  | 
**open_plant_id** | **str** |  | 
**global_plant_id** | **str** |  | [optional] 
**effective_start_date** | **date** |  | 
**effective_end_date** | **date** |  | 
**deleted_flag** | **bool** |  | [optional] 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from ods_sdk_L3.models.plant_response import PlantResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PlantResponse from a JSON string
plant_response_instance = PlantResponse.from_json(json)
# print the JSON string representation of the object
print(PlantResponse.to_json())

# convert the object into a dict
plant_response_dict = plant_response_instance.to_dict()
# create an instance of PlantResponse from a dict
plant_response_from_dict = PlantResponse.from_dict(plant_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


