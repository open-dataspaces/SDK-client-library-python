# DataExchangeStatusNonFeeModelResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**ProcessStatus**](ProcessStatus.md) | 処理成否状態(success:成功、error:失敗) | 
**detail** | **str** | 処理成否詳細 | 

## Example

```python
from ods_sdk_payment.models.data_exchange_status_non_fee_model_response import DataExchangeStatusNonFeeModelResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DataExchangeStatusNonFeeModelResponse from a JSON string
data_exchange_status_non_fee_model_response_instance = DataExchangeStatusNonFeeModelResponse.from_json(json)
# print the JSON string representation of the object
print(DataExchangeStatusNonFeeModelResponse.to_json())

# convert the object into a dict
data_exchange_status_non_fee_model_response_dict = data_exchange_status_non_fee_model_response_instance.to_dict()
# create an instance of DataExchangeStatusNonFeeModelResponse from a dict
data_exchange_status_non_fee_model_response_from_dict = DataExchangeStatusNonFeeModelResponse.from_dict(data_exchange_status_non_fee_model_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


