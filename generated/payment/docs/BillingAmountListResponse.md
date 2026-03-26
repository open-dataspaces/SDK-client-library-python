# BillingAmountListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**billing_details** | [**List[BillingAmountItem]**](BillingAmountItem.md) | 請求リスト | 
**total_amount** | **float** | 請求総額 | 

## Example

```python
from ods_sdk_payment.models.billing_amount_list_response import BillingAmountListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BillingAmountListResponse from a JSON string
billing_amount_list_response_instance = BillingAmountListResponse.from_json(json)
# print the JSON string representation of the object
print(BillingAmountListResponse.to_json())

# convert the object into a dict
billing_amount_list_response_dict = billing_amount_list_response_instance.to_dict()
# create an instance of BillingAmountListResponse from a dict
billing_amount_list_response_from_dict = BillingAmountListResponse.from_dict(billing_amount_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


