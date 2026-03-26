# PostPlantRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operator_id** | **str** |  | 
**plant_name** | **str** |  | 
**plant_address** | **str** |  | 
**open_plant_id** | **str** |  | 
**global_plant_id** | **str** |  | [optional] 
**effective_start_date** | **str** |  | [optional] 
**effective_end_date** | **str** |  | [optional] 

## Example

```python
from ods_sdk_L3.models.post_plant_request import PostPlantRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostPlantRequest from a JSON string
post_plant_request_instance = PostPlantRequest.from_json(json)
# print the JSON string representation of the object
print(PostPlantRequest.to_json())

# convert the object into a dict
post_plant_request_dict = post_plant_request_instance.to_dict()
# create an instance of PostPlantRequest from a dict
post_plant_request_from_dict = PostPlantRequest.from_dict(post_plant_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


