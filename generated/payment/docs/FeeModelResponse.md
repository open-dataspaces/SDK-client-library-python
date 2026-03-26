# FeeModelResponse

利用料モデルレスポンス  すべてのフィールドを含む

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** | 登録日時 | 
**updated_at** | **datetime** | 更新日時 | 
**valid_from** | **datetime** | 有効開始日時 | 
**is_active** | **bool** | 現在有効フラグ | [optional] [default to True]
**version** | **int** | バージョン番号 | [optional] [default to 1]
**storage_type** | [**StorageType**](StorageType.md) |  | [optional] 
**storage_key** | **str** |  | [optional] 
**valid_to** | **datetime** |  | [optional] 
**provider_id** | **str** | データ提供者ID(外部システムにて発行) | 
**consumer_id** | **str** | データ利用者ID(外部システムにて発行) | 
**data_id** | **str** | データID(外部システムにて発行) | 
**payment_service_id** | **UUID** | 決済サービスID | 
**fee_model_name** | **str** | 利用料モデル名 | 
**price** | **str** | 金額 | 
**tax_classification** | [**TaxClassification**](TaxClassification.md) | 税区分 (taxable: 課税, non_taxable: 非課税) | 
**tax_rate** | **str** | 税率 | 
**fee_model_id** | **UUID** | 利用料モデルID | 

## Example

```python
from ods_sdk_payment.models.fee_model_response import FeeModelResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FeeModelResponse from a JSON string
fee_model_response_instance = FeeModelResponse.from_json(json)
# print the JSON string representation of the object
print(FeeModelResponse.to_json())

# convert the object into a dict
fee_model_response_dict = fee_model_response_instance.to_dict()
# create an instance of FeeModelResponse from a dict
fee_model_response_from_dict = FeeModelResponse.from_dict(fee_model_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


