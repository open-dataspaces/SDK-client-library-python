# PaymentAmountListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_details** | [**List[PaymentAmountItem]**](PaymentAmountItem.md) | 支払いリスト | 
**total_amount** | **float** | 支払い総額 | 

## Example

```python
from ods_sdk_payment.models.payment_amount_list_response import PaymentAmountListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentAmountListResponse from a JSON string
payment_amount_list_response_instance = PaymentAmountListResponse.from_json(json)
# print the JSON string representation of the object
print(PaymentAmountListResponse.to_json())

# convert the object into a dict
payment_amount_list_response_dict = payment_amount_list_response_instance.to_dict()
# create an instance of PaymentAmountListResponse from a dict
payment_amount_list_response_from_dict = PaymentAmountListResponse.from_dict(payment_amount_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


