# ods_sdk_L3.ClientsControllerApi

All URIs are relative to *http://localhost:8090*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_client_secret**](ClientsControllerApi.md#get_client_secret) | **POST** /auth/clients/secret/{client_uuid} | 
[**post_clients**](ClientsControllerApi.md#post_clients) | **POST** /auth/clients | 


# **get_client_secret**
> APIResponsePostClientSecretResponse get_client_secret(client_uuid)

### Example


```python
import ods_sdk_L3
from ods_sdk_L3.models.api_response_post_client_secret_response import APIResponsePostClientSecretResponse
from ods_sdk_L3.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8090
# See configuration.py for a list of all supported configuration parameters.
configuration = ods_sdk_L3.Configuration(
    host = "http://localhost:8090"
)


# Enter a context with an instance of the API client
with ods_sdk_L3.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ods_sdk_L3.ClientsControllerApi(api_client)
    client_uuid = 'client_uuid_example' # str | 

    try:
        api_response = api_instance.get_client_secret(client_uuid)
        print("The response of ClientsControllerApi->get_client_secret:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClientsControllerApi->get_client_secret: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_uuid** | **str**|  | 

### Return type

[**APIResponsePostClientSecretResponse**](APIResponsePostClientSecretResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_clients**
> APIResponsePostClientsResponse post_clients(post_clients_request)

### Example


```python
import ods_sdk_L3
from ods_sdk_L3.models.api_response_post_clients_response import APIResponsePostClientsResponse
from ods_sdk_L3.models.post_clients_request import PostClientsRequest
from ods_sdk_L3.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8090
# See configuration.py for a list of all supported configuration parameters.
configuration = ods_sdk_L3.Configuration(
    host = "http://localhost:8090"
)


# Enter a context with an instance of the API client
with ods_sdk_L3.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ods_sdk_L3.ClientsControllerApi(api_client)
    post_clients_request = ods_sdk_L3.PostClientsRequest() # PostClientsRequest | 

    try:
        api_response = api_instance.post_clients(post_clients_request)
        print("The response of ClientsControllerApi->post_clients:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClientsControllerApi->post_clients: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_clients_request** | [**PostClientsRequest**](PostClientsRequest.md)|  | 

### Return type

[**APIResponsePostClientsResponse**](APIResponsePostClientsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

