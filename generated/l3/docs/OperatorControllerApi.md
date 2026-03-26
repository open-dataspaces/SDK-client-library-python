# ods_sdk_L3.OperatorControllerApi

All URIs are relative to *http://localhost:8090*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_operator**](OperatorControllerApi.md#get_operator) | **GET** /account/operator/{operator_id} | 
[**list_operator**](OperatorControllerApi.md#list_operator) | **POST** /account/operator/list | 
[**post_operator**](OperatorControllerApi.md#post_operator) | **POST** /account/operator | 
[**put_operator**](OperatorControllerApi.md#put_operator) | **PUT** /account/operator/{operator_id} | 
[**put_operator_status**](OperatorControllerApi.md#put_operator_status) | **PUT** /account/operator/status/{operator_id} | 


# **get_operator**
> object get_operator(operator_id)

### Example


```python
import ods_sdk_L3
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
    api_instance = ods_sdk_L3.OperatorControllerApi(api_client)
    operator_id = 'operator_id_example' # str | 

    try:
        api_response = api_instance.get_operator(operator_id)
        print("The response of OperatorControllerApi->get_operator:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OperatorControllerApi->get_operator: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **operator_id** | **str**|  | 

### Return type

**object**

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

# **list_operator**
> APIResponseListGetOperatorResponse list_operator(body)

### Example


```python
import ods_sdk_L3
from ods_sdk_L3.models.api_response_list_get_operator_response import APIResponseListGetOperatorResponse
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
    api_instance = ods_sdk_L3.OperatorControllerApi(api_client)
    body = 'body_example' # str | 

    try:
        api_response = api_instance.list_operator(body)
        print("The response of OperatorControllerApi->list_operator:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OperatorControllerApi->list_operator: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **str**|  | 

### Return type

[**APIResponseListGetOperatorResponse**](APIResponseListGetOperatorResponse.md)

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

# **post_operator**
> APIResponsePostOperatorResponse post_operator(post_operator_request)

### Example


```python
import ods_sdk_L3
from ods_sdk_L3.models.api_response_post_operator_response import APIResponsePostOperatorResponse
from ods_sdk_L3.models.post_operator_request import PostOperatorRequest
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
    api_instance = ods_sdk_L3.OperatorControllerApi(api_client)
    post_operator_request = ods_sdk_L3.PostOperatorRequest() # PostOperatorRequest | 

    try:
        api_response = api_instance.post_operator(post_operator_request)
        print("The response of OperatorControllerApi->post_operator:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OperatorControllerApi->post_operator: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_operator_request** | [**PostOperatorRequest**](PostOperatorRequest.md)|  | 

### Return type

[**APIResponsePostOperatorResponse**](APIResponsePostOperatorResponse.md)

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

# **put_operator**
> APIResponseObject put_operator(operator_id, body)

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
    api_instance = ods_sdk_L3.OperatorControllerApi(api_client)
    operator_id = 'operator_id_example' # str | 
    body = 'body_example' # str | 

    try:
        api_response = api_instance.put_operator(operator_id, body)
        print("The response of OperatorControllerApi->put_operator:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OperatorControllerApi->put_operator: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **operator_id** | **str**|  | 
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

# **put_operator_status**
> APIResponseObject put_operator_status(operator_id, put_operator_status_request)

### Example


```python
import ods_sdk_L3
from ods_sdk_L3.models.api_response_object import APIResponseObject
from ods_sdk_L3.models.put_operator_status_request import PutOperatorStatusRequest
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
    api_instance = ods_sdk_L3.OperatorControllerApi(api_client)
    operator_id = 'operator_id_example' # str | 
    put_operator_status_request = ods_sdk_L3.PutOperatorStatusRequest() # PutOperatorStatusRequest | 

    try:
        api_response = api_instance.put_operator_status(operator_id, put_operator_status_request)
        print("The response of OperatorControllerApi->put_operator_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OperatorControllerApi->put_operator_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **operator_id** | **str**|  | 
 **put_operator_status_request** | [**PutOperatorStatusRequest**](PutOperatorStatusRequest.md)|  | 

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

