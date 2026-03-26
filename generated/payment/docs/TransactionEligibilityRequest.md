# TransactionEligibilityRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider_id** | **str** | データ提供者ID(外部システムにて発行) | 
**consumer_id** | **str** | データ利用者ID(外部システムにて発行) | 
**data_id_list** | **List[str]** | データIDのリスト | 

## Example

```python
from ods_sdk_payment.models.transaction_eligibility_request import TransactionEligibilityRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionEligibilityRequest from a JSON string
transaction_eligibility_request_instance = TransactionEligibilityRequest.from_json(json)
# print the JSON string representation of the object
print(TransactionEligibilityRequest.to_json())

# convert the object into a dict
transaction_eligibility_request_dict = transaction_eligibility_request_instance.to_dict()
# create an instance of TransactionEligibilityRequest from a dict
transaction_eligibility_request_from_dict = TransactionEligibilityRequest.from_dict(transaction_eligibility_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


