# ods_sdk_L3.TokenRefreshControllerApi

All URIs are relative to *http://localhost:8090*

Method | HTTP request | Description
------------- | ------------- | -------------
[**refresh**](TokenRefreshControllerApi.md#refresh) | **POST** /auth/token/refresh | 


# **refresh**
> APIResponseTokenRefreshResponse refresh(token_refresh_request)

### Example


```python
import ods_sdk_L3
from ods_sdk_L3.models.api_response_token_refresh_response import APIResponseTokenRefreshResponse
from ods_sdk_L3.models.token_refresh_request import TokenRefreshRequest
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
    api_instance = ods_sdk_L3.TokenRefreshControllerApi(api_client)
    token_refresh_request = ods_sdk_L3.TokenRefreshRequest() # TokenRefreshRequest | 

    try:
        api_response = api_instance.refresh(token_refresh_request)
        print("The response of TokenRefreshControllerApi->refresh:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TokenRefreshControllerApi->refresh: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_refresh_request** | [**TokenRefreshRequest**](TokenRefreshRequest.md)|  | 

### Return type

[**APIResponseTokenRefreshResponse**](APIResponseTokenRefreshResponse.md)

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

