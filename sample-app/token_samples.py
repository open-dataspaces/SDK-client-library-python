import ods_sdk_L3
from ods_sdk_L3.rest import ApiException
from pprint import pprint
from config import get_l3_configuration

def sample_token_management():
    configuration = get_l3_configuration()
    with ods_sdk_L3.ApiClient(configuration) as api_client:
        # Client Token
        token_client_api = ods_sdk_L3.TokenClientControllerApi(api_client)
        # Token Introspection
        token_intro_api = ods_sdk_L3.TokenIntrospectionControllerApi(api_client)
        # Token Password (Login)
        token_pass_api = ods_sdk_L3.TokenPasswordControllerApi(api_client)
        # Token Refresh
        token_refresh_api = ods_sdk_L3.TokenRefreshControllerApi(api_client)
        
        try:
            print("--- TokenClientControllerApi.client ---")
            # api_response = token_client_api.client(...)
            print("Sample call defined.")

            print("--- TokenIntrospectionControllerApi.token_introspection ---")
            # api_response = token_intro_api.token_introspection(...)
            print("Sample call defined.")

            print("--- TokenPasswordControllerApi.login ---")
            # api_response = token_pass_api.login(...)
            print("Sample call defined.")

            print("--- TokenRefreshControllerApi.refresh ---")
            # api_response = token_refresh_api.refresh(...)
            print("Sample call defined.")
            
        except ApiException as e:
            print("Exception: %s\n" % e)

if __name__ == "__main__":
    sample_token_management()
