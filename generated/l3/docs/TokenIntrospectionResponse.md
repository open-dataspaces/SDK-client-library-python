# TokenIntrospectionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** |  | [optional] 
**token_info** | **object** |  | [optional] 

## Example

```python
from ods_sdk_L3.models.token_introspection_response import TokenIntrospectionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TokenIntrospectionResponse from a JSON string
token_introspection_response_instance = TokenIntrospectionResponse.from_json(json)
# print the JSON string representation of the object
print(TokenIntrospectionResponse.to_json())

# convert the object into a dict
token_introspection_response_dict = token_introspection_response_instance.to_dict()
# create an instance of TokenIntrospectionResponse from a dict
token_introspection_response_from_dict = TokenIntrospectionResponse.from_dict(token_introspection_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


