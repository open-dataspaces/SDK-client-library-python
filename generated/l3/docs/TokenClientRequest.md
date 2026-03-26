# TokenClientRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_id** | **str** |  | 
**client_secret** | **str** |  | 

## Example

```python
from ods_sdk_L3.models.token_client_request import TokenClientRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TokenClientRequest from a JSON string
token_client_request_instance = TokenClientRequest.from_json(json)
# print the JSON string representation of the object
print(TokenClientRequest.to_json())

# convert the object into a dict
token_client_request_dict = token_client_request_instance.to_dict()
# create an instance of TokenClientRequest from a dict
token_client_request_from_dict = TokenClientRequest.from_dict(token_client_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


