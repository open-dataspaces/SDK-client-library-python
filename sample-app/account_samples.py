import ods_sdk_L3
from ods_sdk_L3.rest import ApiException
from pprint import pprint
from config import get_l3_configuration

def sample_operator():
    configuration = get_l3_configuration()
    with ods_sdk_L3.ApiClient(configuration) as api_client:
        api_instance = ods_sdk_L3.OperatorControllerApi(api_client)
        operator_id = "sample_op_id"
        
        try:
            print("--- OperatorControllerApi.get_operator ---")
            api_response = api_instance.get_operator(operator_id)
            pprint(api_response)
        except ApiException as e:
            print("Exception: %s\n" % e)
        except Exception as e:
            print("General Exception: %s\n" % e)

def sample_plant():
    configuration = get_l3_configuration()
    with ods_sdk_L3.ApiClient(configuration) as api_client:
        api_instance = ods_sdk_L3.PlantControllerApi(api_client)
        plant_id = "sample_plant_id"
        try:
            print("--- PlantControllerApi.get_plant ---")
            api_response = api_instance.get_plant(plant_id)
            pprint(api_response)
        except ApiException as e:
            print("Exception: %s\n" % e)
        except Exception as e:
            print("General Exception: %s\n" % e)

def sample_user():
    configuration = get_l3_configuration()
    with ods_sdk_L3.ApiClient(configuration) as api_client:
        api_instance = ods_sdk_L3.UserControllerApi(api_client)
        try:
            print("--- UserControllerApi.post_user ---")
            body = "sample_user_id"
            api_response = api_instance.post_user(body)
            pprint(api_response)
        except ApiException as e:
            print("Exception: %s\n" % e)
        except Exception as e:
            print("General Exception: %s\n" % e)

if __name__ == "__main__":
    sample_operator()
    sample_plant()
    sample_user()
