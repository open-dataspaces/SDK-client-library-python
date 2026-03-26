# BillingScheduleRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**consumer_id** | **str** | データ利用者ID | 
**start_date** | **date** | 開始年月日（YYYY-MM-DD） | 
**end_date** | **date** | 終了年月日（YYYY-MM-DD） | 

## Example

```python
from ods_sdk_payment.models.billing_schedule_request import BillingScheduleRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BillingScheduleRequest from a JSON string
billing_schedule_request_instance = BillingScheduleRequest.from_json(json)
# print the JSON string representation of the object
print(BillingScheduleRequest.to_json())

# convert the object into a dict
billing_schedule_request_dict = billing_schedule_request_instance.to_dict()
# create an instance of BillingScheduleRequest from a dict
billing_schedule_request_from_dict = BillingScheduleRequest.from_dict(billing_schedule_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


