import ods_sdk_L3
from ods_sdk_L3.rest import ApiException
from pprint import pprint
from config import get_l3_configuration

def sample_misc():
    configuration = get_l3_configuration()
    with ods_sdk_L3.ApiClient(configuration) as api_client:
        # Clients
        clients_api = ods_sdk_L3.ClientsControllerApi(api_client)
        # Password
        pass_api = ods_sdk_L3.PasswordControllerApi(api_client)
        # Password URL
        pass_url_api = ods_sdk_L3.PasswordUrlControllerApi(api_client)
        
        try:
            print("--- ClientsControllerApi.post_clients ---")
            # api_response = clients_api.post_clients(...)
            print("Sample call defined.")

            print("--- PasswordControllerApi.change_password ---")
            # api_response = pass_api.change_password(...)
            print("Sample call defined.")

            print("--- PasswordUrlControllerApi.auth_password_url ---")
            # api_response = pass_url_api.auth_password_url(...)
            print("Sample call defined.")
            
        except ApiException as e:
            print("Exception: %s\n" % e)

if __name__ == "__main__":
    sample_misc()
