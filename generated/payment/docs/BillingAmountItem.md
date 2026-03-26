# BillingAmountItem


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
**amount** | **float** | 請求予定額 | 
**tax_rate** | **float** | 税率 | 

## Example

```python
from ods_sdk_payment.models.billing_amount_item import BillingAmountItem

# TODO update the JSON string below
json = "{}"
# create an instance of BillingAmountItem from a JSON string
billing_amount_item_instance = BillingAmountItem.from_json(json)
# print the JSON string representation of the object
print(BillingAmountItem.to_json())

# convert the object into a dict
billing_amount_item_dict = billing_amount_item_instance.to_dict()
# create an instance of BillingAmountItem from a dict
billing_amount_item_from_dict = BillingAmountItem.from_dict(billing_amount_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


