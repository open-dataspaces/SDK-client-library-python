# PostClientsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**flow_type** | **str** |  | 
**client_id** | **str** |  | 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**operator_id** | **str** |  | [optional] 
**open_system_id** | **str** |  | [optional] 
**redirect_uris** | **List[str]** |  | [optional] 

## Example

```python
from ods_sdk_L3.models.post_clients_request import PostClientsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostClientsRequest from a JSON string
post_clients_request_instance = PostClientsRequest.from_json(json)
# print the JSON string representation of the object
print(PostClientsRequest.to_json())

# convert the object into a dict
post_clients_request_dict = post_clients_request_instance.to_dict()
# create an instance of PostClientsRequest from a dict
post_clients_request_from_dict = PostClientsRequest.from_dict(post_clients_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


