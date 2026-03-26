# APIResponsePlantResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**title** | **str** |  | 
**status** | **int** |  | [optional] 
**detail** | **str** |  | 
**data** | [**PlantResponse**](PlantResponse.md) |  | 

## Example

```python
from ods_sdk_L3.models.api_response_plant_response import APIResponsePlantResponse

# TODO update the JSON string below
json = "{}"
# create an instance of APIResponsePlantResponse from a JSON string
api_response_plant_response_instance = APIResponsePlantResponse.from_json(json)
# print the JSON string representation of the object
print(APIResponsePlantResponse.to_json())

# convert the object into a dict
api_response_plant_response_dict = api_response_plant_response_instance.to_dict()
# create an instance of APIResponsePlantResponse from a dict
api_response_plant_response_from_dict = APIResponsePlantResponse.from_dict(api_response_plant_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


