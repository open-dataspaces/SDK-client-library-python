# FeeModelListResponse

利用料モデル一覧レスポンス

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**models** | [**List[FeeModelResponse]**](FeeModelResponse.md) | 利用料モデル一覧 | 

## Example

```python
from ods_sdk_payment.models.fee_model_list_response import FeeModelListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FeeModelListResponse from a JSON string
fee_model_list_response_instance = FeeModelListResponse.from_json(json)
# print the JSON string representation of the object
print(FeeModelListResponse.to_json())

# convert the object into a dict
fee_model_list_response_dict = fee_model_list_response_instance.to_dict()
# create an instance of FeeModelListResponse from a dict
fee_model_list_response_from_dict = FeeModelListResponse.from_dict(fee_model_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


