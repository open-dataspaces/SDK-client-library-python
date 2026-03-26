# TransactionEligibilityNonFeeModelResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**TransactionEligibility**](TransactionEligibility.md) | 取引可否(allowed:取引可, denied:取引不可) | 
**detail** | **str** | 処理成否詳細 | 

## Example

```python
from ods_sdk_payment.models.transaction_eligibility_non_fee_model_response import TransactionEligibilityNonFeeModelResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionEligibilityNonFeeModelResponse from a JSON string
transaction_eligibility_non_fee_model_response_instance = TransactionEligibilityNonFeeModelResponse.from_json(json)
# print the JSON string representation of the object
print(TransactionEligibilityNonFeeModelResponse.to_json())

# convert the object into a dict
transaction_eligibility_non_fee_model_response_dict = transaction_eligibility_non_fee_model_response_instance.to_dict()
# create an instance of TransactionEligibilityNonFeeModelResponse from a dict
transaction_eligibility_non_fee_model_response_from_dict = TransactionEligibilityNonFeeModelResponse.from_dict(transaction_eligibility_non_fee_model_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


