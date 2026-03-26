# ods_sdk_L3.PasswordControllerApi

All URIs are relative to *http://localhost:8090*

Method | HTTP request | Description
------------- | ------------- | -------------
[**change_password**](PasswordControllerApi.md#change_password) | **PUT** /auth/password/{operator_id} | 


# **change_password**
> object change_password(operator_id, password_request)

### Example


```python
import ods_sdk_L3
from ods_sdk_L3.models.password_request import PasswordRequest
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
    api_instance = ods_sdk_L3.PasswordControllerApi(api_client)
    operator_id = 'operator_id_example' # str | 
    password_request = ods_sdk_L3.PasswordRequest() # PasswordRequest | 

    try:
        api_response = api_instance.change_password(operator_id, password_request)
        print("The response of PasswordControllerApi->change_password:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PasswordControllerApi->change_password: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **operator_id** | **str**|  | 
 **password_request** | [**PasswordRequest**](PasswordRequest.md)|  | 

### Return type

**object**

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

