# TokenIntrospectionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_id** | **str** |  | 
**client_secret** | **str** |  | 
**access_token** | **str** |  | 

## Example

```python
from ods_sdk_L3.models.token_introspection_request import TokenIntrospectionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TokenIntrospectionRequest from a JSON string
token_introspection_request_instance = TokenIntrospectionRequest.from_json(json)
# print the JSON string representation of the object
print(TokenIntrospectionRequest.to_json())

# convert the object into a dict
token_introspection_request_dict = token_introspection_request_instance.to_dict()
# create an instance of TokenIntrospectionRequest from a dict
token_introspection_request_from_dict = TokenIntrospectionRequest.from_dict(token_introspection_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


