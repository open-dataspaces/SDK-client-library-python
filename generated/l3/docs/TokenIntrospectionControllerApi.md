# ods_sdk_L3.TokenIntrospectionControllerApi

All URIs are relative to *http://localhost:8090*

Method | HTTP request | Description
------------- | ------------- | -------------
[**token_introspection**](TokenIntrospectionControllerApi.md#token_introspection) | **POST** /auth/token/introspect | 


# **token_introspection**
> APIResponseTokenIntrospectionResponse token_introspection(token_introspection_request)

### Example


```python
import ods_sdk_L3
from ods_sdk_L3.models.api_response_token_introspection_response import APIResponseTokenIntrospectionResponse
from ods_sdk_L3.models.token_introspection_request import TokenIntrospectionRequest
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
    api_instance = ods_sdk_L3.TokenIntrospectionControllerApi(api_client)
    token_introspection_request = ods_sdk_L3.TokenIntrospectionRequest() # TokenIntrospectionRequest | 

    try:
        api_response = api_instance.token_introspection(token_introspection_request)
        print("The response of TokenIntrospectionControllerApi->token_introspection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TokenIntrospectionControllerApi->token_introspection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_introspection_request** | [**TokenIntrospectionRequest**](TokenIntrospectionRequest.md)|  | 

### Return type

[**APIResponseTokenIntrospectionResponse**](APIResponseTokenIntrospectionResponse.md)

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

