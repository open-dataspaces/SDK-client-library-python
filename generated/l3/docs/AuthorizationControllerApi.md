# ods_sdk_L3.AuthorizationControllerApi

All URIs are relative to *http://localhost:8090*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_api**](AuthorizationControllerApi.md#get_api) | **GET** /authz/stores/{store_id}/authorization-models | 
[**post_api**](AuthorizationControllerApi.md#post_api) | **POST** /authz/stores/{store_id}/access/v1/evaluation | 
[**post_api1**](AuthorizationControllerApi.md#post_api1) | **POST** /authz/stores/{store_id}/authorization-models | 
[**post_api2**](AuthorizationControllerApi.md#post_api2) | **POST** /authz/stores/{store_id}/write | 
[**post_api3**](AuthorizationControllerApi.md#post_api3) | **POST** /authz/stores/{store_id}/read | 


# **get_api**
> APIResponseObject get_api(store_id)

### Example


```python
import ods_sdk_L3
from ods_sdk_L3.models.api_response_object import APIResponseObject
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
    api_instance = ods_sdk_L3.AuthorizationControllerApi(api_client)
    store_id = 'store_id_example' # str | 

    try:
        api_response = api_instance.get_api(store_id)
        print("The response of AuthorizationControllerApi->get_api:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthorizationControllerApi->get_api: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **str**|  | 

### Return type

[**APIResponseObject**](APIResponseObject.md)

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

# **post_api**
> APIResponseObject post_api(store_id, body)

### Example


```python
import ods_sdk_L3
from ods_sdk_L3.models.api_response_object import APIResponseObject
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
    api_instance = ods_sdk_L3.AuthorizationControllerApi(api_client)
    store_id = 'store_id_example' # str | 
    body = 'body_example' # str | 

    try:
        api_response = api_instance.post_api(store_id, body)
        print("The response of AuthorizationControllerApi->post_api:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthorizationControllerApi->post_api: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **str**|  | 
 **body** | **str**|  | 

### Return type

[**APIResponseObject**](APIResponseObject.md)

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

# **post_api1**
> APIResponseObject post_api1(store_id, body)

### Example


```python
import ods_sdk_L3
from ods_sdk_L3.models.api_response_object import APIResponseObject
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
    api_instance = ods_sdk_L3.AuthorizationControllerApi(api_client)
    store_id = 'store_id_example' # str | 
    body = 'body_example' # str | 

    try:
        api_response = api_instance.post_api1(store_id, body)
        print("The response of AuthorizationControllerApi->post_api1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthorizationControllerApi->post_api1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **str**|  | 
 **body** | **str**|  | 

### Return type

[**APIResponseObject**](APIResponseObject.md)

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

# **post_api2**
> APIResponseObject post_api2(store_id, body)

### Example


```python
import ods_sdk_L3
from ods_sdk_L3.models.api_response_object import APIResponseObject
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
    api_instance = ods_sdk_L3.AuthorizationControllerApi(api_client)
    store_id = 'store_id_example' # str | 
    body = 'body_example' # str | 

    try:
        api_response = api_instance.post_api2(store_id, body)
        print("The response of AuthorizationControllerApi->post_api2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthorizationControllerApi->post_api2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **str**|  | 
 **body** | **str**|  | 

### Return type

[**APIResponseObject**](APIResponseObject.md)

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

# **post_api3**
> APIResponseObject post_api3(store_id, body)

### Example


```python
import ods_sdk_L3
from ods_sdk_L3.models.api_response_object import APIResponseObject
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
    api_instance = ods_sdk_L3.AuthorizationControllerApi(api_client)
    store_id = 'store_id_example' # str | 
    body = 'body_example' # str | 

    try:
        api_response = api_instance.post_api3(store_id, body)
        print("The response of AuthorizationControllerApi->post_api3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthorizationControllerApi->post_api3: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **str**|  | 
 **body** | **str**|  | 

### Return type

[**APIResponseObject**](APIResponseObject.md)

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

