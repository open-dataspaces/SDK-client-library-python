# FeeModelCreateRequest

利用料モデル作成リクエスト  クライアントから送信するフィールド： - コアフィールド（必須） - 識別子フィールド（必須） - オプションフィールド - クライアント管理フィールド（valid_from, is_active, version）  サーバー側で自動生成されるフィールド： - created_at, updated_at（現在時刻）

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
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
**price** | [**Price**](Price.md) |  | 
**tax_classification** | [**TaxClassification**](TaxClassification.md) | 税区分 (taxable: 課税, non_taxable: 非課税) | 
**tax_rate** | [**TaxRate**](TaxRate.md) |  | 

## Example

```python
from ods_sdk_payment.models.fee_model_create_request import FeeModelCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FeeModelCreateRequest from a JSON string
fee_model_create_request_instance = FeeModelCreateRequest.from_json(json)
# print the JSON string representation of the object
print(FeeModelCreateRequest.to_json())

# convert the object into a dict
fee_model_create_request_dict = fee_model_create_request_instance.to_dict()
# create an instance of FeeModelCreateRequest from a dict
fee_model_create_request_from_dict = FeeModelCreateRequest.from_dict(fee_model_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


