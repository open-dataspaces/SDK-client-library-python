import ods_sdk_L3
from ods_sdk_L3.rest import ApiException
from pprint import pprint
from config import get_l3_configuration

def sample_auth_token():
    configuration = get_l3_configuration()

    with ods_sdk_L3.ApiClient(configuration) as api_client:
        api_instance = ods_sdk_L3.AuthTokenControllerApi(api_client)
        
        # リクエストモデルの作成
        auth_token_request = ods_sdk_L3.AuthTokenRequest(
            code="sample_code",
            client_id="sample_client_id",
            client_secret="sample_client_secret",
            redirect_uri="http://localhost/callback",
            code_verifier="sample_verifier"
        )

        try:
            print("--- AuthTokenControllerApi.access_token ---")
            # api_response = api_instance.access_token(auth_token_request)
            # pprint(api_response)
            print("Sample call defined. Uncomment the execution lines to run against a real server.")
        except ApiException as e:
            print("Exception when calling AuthTokenControllerApi->access_token: %s\n" % e)

def sample_auth_url():
    configuration = get_l3_configuration()
    with ods_sdk_L3.ApiClient(configuration) as api_client:
        api_instance = ods_sdk_L3.AuthUrlControllerApi(api_client)
        auth_url_request = ods_sdk_L3.AuthUrlRequest(
            client_id="sample_id",
            redirect_uri="http://localhost/callback",
            scope="openid",
            state="sample_state",
            code_challenge="sample_challenge",
            code_challenge_method="S256"
        )
        try:
            print("--- AuthUrlControllerApi.url ---")
            # api_response = api_instance.url(auth_url_request)
            # pprint(api_response)
            print("Sample call defined.")
        except ApiException as e:
            print("Exception: %s\n" % e)

if __name__ == "__main__":
    sample_auth_token()
    sample_auth_url()
