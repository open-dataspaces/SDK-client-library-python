# PostClientSecretResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_secret** | **str** |  | [optional] 

## Example

```python
from ods_sdk_L3.models.post_client_secret_response import PostClientSecretResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PostClientSecretResponse from a JSON string
post_client_secret_response_instance = PostClientSecretResponse.from_json(json)
# print the JSON string representation of the object
print(PostClientSecretResponse.to_json())

# convert the object into a dict
post_client_secret_response_dict = post_client_secret_response_instance.to_dict()
# create an instance of PostClientSecretResponse from a dict
post_client_secret_response_from_dict = PostClientSecretResponse.from_dict(post_client_secret_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


