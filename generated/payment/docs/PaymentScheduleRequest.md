# PaymentScheduleRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider_id** | **str** | データ提供者ID | 
**start_date** | **date** | 開始年月日（YYYY-MM-DD） | 
**end_date** | **date** | 終了年月日（YYYY-MM-DD） | 

## Example

```python
from ods_sdk_payment.models.payment_schedule_request import PaymentScheduleRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentScheduleRequest from a JSON string
payment_schedule_request_instance = PaymentScheduleRequest.from_json(json)
# print the JSON string representation of the object
print(PaymentScheduleRequest.to_json())

# convert the object into a dict
payment_schedule_request_dict = payment_schedule_request_instance.to_dict()
# create an instance of PaymentScheduleRequest from a dict
payment_schedule_request_from_dict = PaymentScheduleRequest.from_dict(payment_schedule_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


