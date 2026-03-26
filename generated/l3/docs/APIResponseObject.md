# APIResponseObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**title** | **str** |  | 
**status** | **int** |  | [optional] 
**detail** | **str** |  | 
**data** | **object** |  | 

## Example

```python
from ods_sdk_L3.models.api_response_object import APIResponseObject

# TODO update the JSON string below
json = "{}"
# create an instance of APIResponseObject from a JSON string
api_response_object_instance = APIResponseObject.from_json(json)
# print the JSON string representation of the object
print(APIResponseObject.to_json())

# convert the object into a dict
api_response_object_dict = api_response_object_instance.to_dict()
# create an instance of APIResponseObject from a dict
api_response_object_from_dict = APIResponseObject.from_dict(api_response_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


