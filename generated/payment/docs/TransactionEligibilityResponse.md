# TransactionEligibilityResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**TransactionEligibility**](TransactionEligibility.md) | 取引可否(allowed:取引可, denied:取引不可) | 
**detail** | **str** | 処理成否詳細 | 

## Example

```python
from ods_sdk_payment.models.transaction_eligibility_response import TransactionEligibilityResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionEligibilityResponse from a JSON string
transaction_eligibility_response_instance = TransactionEligibilityResponse.from_json(json)
# print the JSON string representation of the object
print(TransactionEligibilityResponse.to_json())

# convert the object into a dict
transaction_eligibility_response_dict = transaction_eligibility_response_instance.to_dict()
# create an instance of TransactionEligibilityResponse from a dict
transaction_eligibility_response_from_dict = TransactionEligibilityResponse.from_dict(transaction_eligibility_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


