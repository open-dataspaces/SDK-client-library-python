# TransactionEligibilityNonFeeModelRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider_id** | **str** | データ提供者ID(外部システムにて発行) | 
**consumer_id** | **str** | データ利用者ID(外部システムにて発行) | 
**payment_service_id** | **UUID** | 決済サービスID | 
**tax_classification** | [**TaxClassification**](TaxClassification.md) | 税区分 (taxable: 課税, non_taxable: 非課税) | 
**tax_rate** | [**TaxRate**](TaxRate.md) |  | 
**completed_at** | **datetime** | データ交換処理完了日時（ISO8601） | 
**amount** | **float** | 支払い予定額 | 

## Example

```python
from ods_sdk_payment.models.transaction_eligibility_non_fee_model_request import TransactionEligibilityNonFeeModelRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionEligibilityNonFeeModelRequest from a JSON string
transaction_eligibility_non_fee_model_request_instance = TransactionEligibilityNonFeeModelRequest.from_json(json)
# print the JSON string representation of the object
print(TransactionEligibilityNonFeeModelRequest.to_json())

# convert the object into a dict
transaction_eligibility_non_fee_model_request_dict = transaction_eligibility_non_fee_model_request_instance.to_dict()
# create an instance of TransactionEligibilityNonFeeModelRequest from a dict
transaction_eligibility_non_fee_model_request_from_dict = TransactionEligibilityNonFeeModelRequest.from_dict(transaction_eligibility_non_fee_model_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


