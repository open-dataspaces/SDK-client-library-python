# FeeModelUpdateRequest

利用料モデル更新リクエスト  更新可能なフィールドのみ含む（すべて任意 = 部分更新対応）  更新不可能なフィールド： - provider_id, consumer_id, data_id, payment_service_id（識別子） - created_at, updated_at（システム管理）  更新可能なフィールド： - fee_model_name, price, tax_classification, tax_rate（コア情報） - storage_type, storage_key, valid_from, valid_to（オプション情報） - is_active, version（クライアント管理フィールド）

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fee_model_name** | **str** |  | [optional] 
**price** | [**Price1**](Price1.md) |  | [optional] 
**tax_classification** | [**TaxClassification**](TaxClassification.md) |  | [optional] 
**tax_rate** | [**TaxRate1**](TaxRate1.md) |  | [optional] 
**storage_type** | [**StorageType**](StorageType.md) |  | [optional] 
**storage_key** | **str** |  | [optional] 
**valid_from** | **datetime** |  | [optional] 
**valid_to** | **datetime** |  | [optional] 
**is_active** | **bool** |  | [optional] 
**version** | **int** |  | [optional] 

## Example

```python
from ods_sdk_payment.models.fee_model_update_request import FeeModelUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FeeModelUpdateRequest from a JSON string
fee_model_update_request_instance = FeeModelUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(FeeModelUpdateRequest.to_json())

# convert the object into a dict
fee_model_update_request_dict = fee_model_update_request_instance.to_dict()
# create an instance of FeeModelUpdateRequest from a dict
fee_model_update_request_from_dict = FeeModelUpdateRequest.from_dict(fee_model_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


