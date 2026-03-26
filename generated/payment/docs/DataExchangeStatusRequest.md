# DataExchangeStatusRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tracking_id** | **str** | トラッキングID  | 
**status** | [**DataExchangeStatus**](DataExchangeStatus.md) | データ交換ステータス (completed: 交換完了, failed: 交換失敗) | 

## Example

```python
from ods_sdk_payment.models.data_exchange_status_request import DataExchangeStatusRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DataExchangeStatusRequest from a JSON string
data_exchange_status_request_instance = DataExchangeStatusRequest.from_json(json)
# print the JSON string representation of the object
print(DataExchangeStatusRequest.to_json())

# convert the object into a dict
data_exchange_status_request_dict = data_exchange_status_request_instance.to_dict()
# create an instance of DataExchangeStatusRequest from a dict
data_exchange_status_request_from_dict = DataExchangeStatusRequest.from_dict(data_exchange_status_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


