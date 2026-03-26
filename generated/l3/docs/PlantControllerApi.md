# ods_sdk_L3.PlantControllerApi

All URIs are relative to *http://localhost:8090*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_plant**](PlantControllerApi.md#get_plant) | **GET** /account/operator/plant/{plant_id} | 
[**list_plant**](PlantControllerApi.md#list_plant) | **POST** /account/operator/plant/list | 
[**post_plant**](PlantControllerApi.md#post_plant) | **POST** /account/operator/plant | 
[**put_plant**](PlantControllerApi.md#put_plant) | **PUT** /account/operator/plant/{plant_id} | 
[**put_plant_status**](PlantControllerApi.md#put_plant_status) | **PUT** /account/operator/plant/status/{plant_id} | 


# **get_plant**
> object get_plant(plant_id)

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
    api_instance = ods_sdk_L3.PlantControllerApi(api_client)
    plant_id = 'plant_id_example' # str | 

    try:
        api_response = api_instance.get_plant(plant_id)
        print("The response of PlantControllerApi->get_plant:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlantControllerApi->get_plant: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plant_id** | **str**|  | 

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

# **list_plant**
> APIResponseListGetPlantResponse list_plant(body)

### Example


```python
import ods_sdk_L3
from ods_sdk_L3.models.api_response_list_get_plant_response import APIResponseListGetPlantResponse
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
    api_instance = ods_sdk_L3.PlantControllerApi(api_client)
    body = 'body_example' # str | 

    try:
        api_response = api_instance.list_plant(body)
        print("The response of PlantControllerApi->list_plant:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlantControllerApi->list_plant: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **str**|  | 

### Return type

[**APIResponseListGetPlantResponse**](APIResponseListGetPlantResponse.md)

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

# **post_plant**
> APIResponsePlantResponse post_plant(post_plant_request)

### Example


```python
import ods_sdk_L3
from ods_sdk_L3.models.api_response_plant_response import APIResponsePlantResponse
from ods_sdk_L3.models.post_plant_request import PostPlantRequest
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
    api_instance = ods_sdk_L3.PlantControllerApi(api_client)
    post_plant_request = ods_sdk_L3.PostPlantRequest() # PostPlantRequest | 

    try:
        api_response = api_instance.post_plant(post_plant_request)
        print("The response of PlantControllerApi->post_plant:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlantControllerApi->post_plant: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_plant_request** | [**PostPlantRequest**](PostPlantRequest.md)|  | 

### Return type

[**APIResponsePlantResponse**](APIResponsePlantResponse.md)

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

# **put_plant**
> APIResponseObject put_plant(plant_id, body)

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
    api_instance = ods_sdk_L3.PlantControllerApi(api_client)
    plant_id = 'plant_id_example' # str | 
    body = 'body_example' # str | 

    try:
        api_response = api_instance.put_plant(plant_id, body)
        print("The response of PlantControllerApi->put_plant:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlantControllerApi->put_plant: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plant_id** | **str**|  | 
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

# **put_plant_status**
> APIResponseObject put_plant_status(plant_id, put_plant_status_request)

### Example


```python
import ods_sdk_L3
from ods_sdk_L3.models.api_response_object import APIResponseObject
from ods_sdk_L3.models.put_plant_status_request import PutPlantStatusRequest
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
    api_instance = ods_sdk_L3.PlantControllerApi(api_client)
    plant_id = 'plant_id_example' # str | 
    put_plant_status_request = ods_sdk_L3.PutPlantStatusRequest() # PutPlantStatusRequest | 

    try:
        api_response = api_instance.put_plant_status(plant_id, put_plant_status_request)
        print("The response of PlantControllerApi->put_plant_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlantControllerApi->put_plant_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plant_id** | **str**|  | 
 **put_plant_status_request** | [**PutPlantStatusRequest**](PutPlantStatusRequest.md)|  | 

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

