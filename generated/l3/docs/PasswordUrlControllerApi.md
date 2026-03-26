# ods_sdk_L3.PasswordUrlControllerApi

All URIs are relative to *http://localhost:8090*

Method | HTTP request | Description
------------- | ------------- | -------------
[**url1**](PasswordUrlControllerApi.md#url1) | **POST** /auth/password/url | 


# **url1**
> APIResponsePasswordUrlResponse url1(password_url_request)

### Example


```python
import ods_sdk_L3
from ods_sdk_L3.models.api_response_password_url_response import APIResponsePasswordUrlResponse
from ods_sdk_L3.models.password_url_request import PasswordUrlRequest
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
    api_instance = ods_sdk_L3.PasswordUrlControllerApi(api_client)
    password_url_request = ods_sdk_L3.PasswordUrlRequest() # PasswordUrlRequest | 

    try:
        api_response = api_instance.url1(password_url_request)
        print("The response of PasswordUrlControllerApi->url1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PasswordUrlControllerApi->url1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **password_url_request** | [**PasswordUrlRequest**](PasswordUrlRequest.md)|  | 

### Return type

[**APIResponsePasswordUrlResponse**](APIResponsePasswordUrlResponse.md)

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

