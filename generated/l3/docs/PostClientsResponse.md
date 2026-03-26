# PostClientsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_uuid** | **str** |  | [optional] 
**client_id** | **str** |  | [optional] 
**enabled** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**flow_type** | **str** |  | [optional] 
**open_system_id** | **str** |  | [optional] 
**operator_id** | **str** |  | [optional] 
**redirect_uris** | **List[str]** |  | [optional] 

## Example

```python
from ods_sdk_L3.models.post_clients_response import PostClientsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PostClientsResponse from a JSON string
post_clients_response_instance = PostClientsResponse.from_json(json)
# print the JSON string representation of the object
print(PostClientsResponse.to_json())

# convert the object into a dict
post_clients_response_dict = post_clients_response_instance.to_dict()
# create an instance of PostClientsResponse from a dict
post_clients_response_from_dict = PostClientsResponse.from_dict(post_clients_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


