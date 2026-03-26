# DataExchangeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tracking_id** | **str** | トラッキングID  | 
**provider_id** | **str** | データ提供者ID | 
**consumer_id** | **str** | データ利用者ID | 
**data_id_list** | **List[str]** | データIDのリスト(外部システムにて発行) | 
**completed_at** | **datetime** | データ交換処理完了日時（ISO8601） | 
**status** | [**DataExchangeStatus**](DataExchangeStatus.md) | データ交換ステータス (completed: 交換完了, failed: 交換失敗) | 

## Example

```python
from ods_sdk_payment.models.data_exchange_request import DataExchangeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DataExchangeRequest from a JSON string
data_exchange_request_instance = DataExchangeRequest.from_json(json)
# print the JSON string representation of the object
print(DataExchangeRequest.to_json())

# convert the object into a dict
data_exchange_request_dict = data_exchange_request_instance.to_dict()
# create an instance of DataExchangeRequest from a dict
data_exchange_request_from_dict = DataExchangeRequest.from_dict(data_exchange_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


