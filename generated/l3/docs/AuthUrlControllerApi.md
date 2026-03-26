# ods_sdk_L3.AuthUrlControllerApi

All URIs are relative to *http://localhost:8090*

Method | HTTP request | Description
------------- | ------------- | -------------
[**url**](AuthUrlControllerApi.md#url) | **POST** /auth/url | 


# **url**
> APIResponseAuthUrlResponse url(auth_url_request)

### Example


```python
import ods_sdk_L3
from ods_sdk_L3.models.api_response_auth_url_response import APIResponseAuthUrlResponse
from ods_sdk_L3.models.auth_url_request import AuthUrlRequest
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
    api_instance = ods_sdk_L3.AuthUrlControllerApi(api_client)
    auth_url_request = ods_sdk_L3.AuthUrlRequest() # AuthUrlRequest | 

    try:
        api_response = api_instance.url(auth_url_request)
        print("The response of AuthUrlControllerApi->url:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthUrlControllerApi->url: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_url_request** | [**AuthUrlRequest**](AuthUrlRequest.md)|  | 

### Return type

[**APIResponseAuthUrlResponse**](APIResponseAuthUrlResponse.md)

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

