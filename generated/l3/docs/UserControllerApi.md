# ods_sdk_L3.UserControllerApi

All URIs are relative to *http://localhost:8090*

Method | HTTP request | Description
------------- | ------------- | -------------
[**post_user**](UserControllerApi.md#post_user) | **POST** /account/user | 


# **post_user**
> APIResponsePostUserResponse post_user(body)

### Example


```python
import ods_sdk_L3
from ods_sdk_L3.models.api_response_post_user_response import APIResponsePostUserResponse
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
    api_instance = ods_sdk_L3.UserControllerApi(api_client)
    body = 'body_example' # str | 

    try:
        api_response = api_instance.post_user(body)
        print("The response of UserControllerApi->post_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserControllerApi->post_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **str**|  | 

### Return type

[**APIResponsePostUserResponse**](APIResponsePostUserResponse.md)

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

