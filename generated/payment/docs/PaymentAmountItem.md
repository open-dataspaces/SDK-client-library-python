# PaymentAmountItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tracking_id** | **str** | トラッキングID | 
**fee_model_id** | **str** | 利用料モデルID | 
**payment_service_id** | **str** | 決済サービスID | 
**provider_id** | **str** | データ提供者ID | 
**consumer_id** | **str** | データ利用者ID | 
**data_id_list** | **List[str]** | データIDのリスト | 
**completed_at** | **datetime** | データ交換処理完了日時 | 
**amount** | **float** | 支払い予定額 | 
**tax_rate** | **float** | 税率 | 

## Example

```python
from ods_sdk_payment.models.payment_amount_item import PaymentAmountItem

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentAmountItem from a JSON string
payment_amount_item_instance = PaymentAmountItem.from_json(json)
# print the JSON string representation of the object
print(PaymentAmountItem.to_json())

# convert the object into a dict
payment_amount_item_dict = payment_amount_item_instance.to_dict()
# create an instance of PaymentAmountItem from a dict
payment_amount_item_from_dict = PaymentAmountItem.from_dict(payment_amount_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


