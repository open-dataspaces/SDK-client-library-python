# ods_sdk_L3.ApiKeyControllerApi

All URIs are relative to *http://localhost:8090*

Method | HTTP request | Description
------------- | ------------- | -------------
[**verify_api_key**](ApiKeyControllerApi.md#verify_api_key) | **POST** /auth/apikey/verify | 


# **verify_api_key**
> APIResponseAPIKeyVerifyResponse verify_api_key(api_key_verify_request)

### Example


```python
import ods_sdk_L3
from ods_sdk_L3.models.api_key_verify_request import APIKeyVerifyRequest
from ods_sdk_L3.models.api_response_api_key_verify_response import APIResponseAPIKeyVerifyResponse
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
    api_instance = ods_sdk_L3.ApiKeyControllerApi(api_client)
    api_key_verify_request = ods_sdk_L3.APIKeyVerifyRequest() # APIKeyVerifyRequest | 

    try:
        api_response = api_instance.verify_api_key(api_key_verify_request)
        print("The response of ApiKeyControllerApi->verify_api_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiKeyControllerApi->verify_api_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key_verify_request** | [**APIKeyVerifyRequest**](APIKeyVerifyRequest.md)|  | 

### Return type

[**APIResponseAPIKeyVerifyResponse**](APIResponseAPIKeyVerifyResponse.md)

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

