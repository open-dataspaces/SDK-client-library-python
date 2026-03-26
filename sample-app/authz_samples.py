import ods_sdk_L3
from ods_sdk_L3.rest import ApiException
from pprint import pprint
from config import get_l3_configuration

def sample_authorization():
    configuration = get_l3_configuration()
    with ods_sdk_L3.ApiClient(configuration) as api_client:
        api_instance = ods_sdk_L3.AuthorizationControllerApi(api_client)
        store_id = "sample_store_id"
        try:
            print("--- AuthorizationControllerApi.get_api ---")
            # api_response = api_instance.get_api(store_id)
            # pprint(api_response)
            print("Sample call defined.")
        except ApiException as e:
            print("Exception: %s\n" % e)

def sample_api_key():
    configuration = get_l3_configuration()
    with ods_sdk_L3.ApiClient(configuration) as api_client:
        api_instance = ods_sdk_L3.ApiKeyControllerApi(api_client)
        try:
            print("--- ApiKeyControllerApi.verify_api_key ---")
            # api_response = api_instance.verify_api_key(...)
            print("Sample call defined.")
        except ApiException as e:
            print("Exception: %s\n" % e)

if __name__ == "__main__":
    sample_authorization()
    sample_api_key()
