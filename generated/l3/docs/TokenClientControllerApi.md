# ods_sdk_L3.TokenClientControllerApi

All URIs are relative to *http://localhost:8090*

Method | HTTP request | Description
------------- | ------------- | -------------
[**client**](TokenClientControllerApi.md#client) | **POST** /auth/token/client | 


# **client**
> APIResponseTokenClientResponse client(token_client_request)

### Example


```python
import ods_sdk_L3
from ods_sdk_L3.models.api_response_token_client_response import APIResponseTokenClientResponse
from ods_sdk_L3.models.token_client_request import TokenClientRequest
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
    api_instance = ods_sdk_L3.TokenClientControllerApi(api_client)
    token_client_request = ods_sdk_L3.TokenClientRequest() # TokenClientRequest | 

    try:
        api_response = api_instance.client(token_client_request)
        print("The response of TokenClientControllerApi->client:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TokenClientControllerApi->client: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_client_request** | [**TokenClientRequest**](TokenClientRequest.md)|  | 

### Return type

[**APIResponseTokenClientResponse**](APIResponseTokenClientResponse.md)

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

