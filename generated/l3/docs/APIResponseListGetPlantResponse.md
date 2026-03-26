# APIResponseListGetPlantResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**title** | **str** |  | 
**status** | **int** |  | [optional] 
**detail** | **str** |  | 
**data** | [**List[GetPlantResponse]**](GetPlantResponse.md) |  | 

## Example

```python
from ods_sdk_L3.models.api_response_list_get_plant_response import APIResponseListGetPlantResponse

# TODO update the JSON string below
json = "{}"
# create an instance of APIResponseListGetPlantResponse from a JSON string
api_response_list_get_plant_response_instance = APIResponseListGetPlantResponse.from_json(json)
# print the JSON string representation of the object
print(APIResponseListGetPlantResponse.to_json())

# convert the object into a dict
api_response_list_get_plant_response_dict = api_response_list_get_plant_response_instance.to_dict()
# create an instance of APIResponseListGetPlantResponse from a dict
api_response_list_get_plant_response_from_dict = APIResponseListGetPlantResponse.from_dict(api_response_list_get_plant_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


