import ods_sdk_payment
from ods_sdk_payment.rest import ApiException
from pprint import pprint
from config import get_payment_configuration

def sample_data_exchange():
    configuration = get_payment_configuration()
    with ods_sdk_payment.ApiClient(configuration) as api_client:
        api_instance = ods_sdk_payment.DefaultApi(api_client)
        
        try:
            print("--- 精算決済Api.list_fee_models ---")
            # api_response = api_instance.list_fee_models_api_v1_fee_model_get()
            # pprint(api_response)
            print("Sample call defined.")
            
            print("--- 精算決済Api.check_transaction_eligibility ---")
            # req = ods_payment_sdk.TransactionEligibilityRequest(...)
            # api_response = api_instance.check_transaction_eligibility_api_v1_data_exchange_transaction_eligibility_post(...)
            print("Sample call defined.")
        except ApiException as e:
            print("Exception: %s\n" % e)

if __name__ == "__main__":
    sample_data_exchange()
