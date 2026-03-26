# ods_sdk_payment.DefaultApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**check_transaction_eligibility_api_v1_data_exchange_transaction_eligibility_post**](DefaultApi.md#check_transaction_eligibility_api_v1_data_exchange_transaction_eligibility_post) | **POST** /api/v1/data-exchange/transaction/eligibility | 取引可否確認API
[**check_transaction_eligibility_non_fee_model_api_v1_data_exchange_non_fee_model_transaction_eligibility_post**](DefaultApi.md#check_transaction_eligibility_non_fee_model_api_v1_data_exchange_non_fee_model_transaction_eligibility_post) | **POST** /api/v1/data-exchange/non-fee-model/transaction/eligibility | 取引可否確認API(利用料モデル無)
[**confirm_data_exchange_api_v1_data_exchange_non_fee_model_confirm_post**](DefaultApi.md#confirm_data_exchange_api_v1_data_exchange_non_fee_model_confirm_post) | **POST** /api/v1/data-exchange/non-fee-model/confirm | データ交換取引金額確定用API(利用料モデル無)
[**create_fee_model_api_v1_fee_model_post**](DefaultApi.md#create_fee_model_api_v1_fee_model_post) | **POST** /api/v1/fee-model | 利用料モデル登録API
[**delete_fee_model_api_v1_fee_model_fee_model_id_delete**](DefaultApi.md#delete_fee_model_api_v1_fee_model_fee_model_id_delete) | **DELETE** /api/v1/fee-model/{fee_model_id} | 利用料モデル削除API
[**get_billing_schedule_api_v1_billing_post**](DefaultApi.md#get_billing_schedule_api_v1_billing_post) | **POST** /api/v1/billing | 請求予定額取得API
[**get_payment_schedule_api_v1_payment_post**](DefaultApi.md#get_payment_schedule_api_v1_payment_post) | **POST** /api/v1/payment | 支払予定額取得API
[**list_fee_models_api_v1_fee_model_get**](DefaultApi.md#list_fee_models_api_v1_fee_model_get) | **GET** /api/v1/fee-model | 利用料モデル一覧取得API
[**register_data_exchange_status_api_v1_data_exchange_status_post**](DefaultApi.md#register_data_exchange_status_api_v1_data_exchange_status_post) | **POST** /api/v1/data-exchange/status | データ交換状態登録API
[**update_data_exchange_status_api_v1_data_exchange_status_put**](DefaultApi.md#update_data_exchange_status_api_v1_data_exchange_status_put) | **PUT** /api/v1/data-exchange/status | データ交換状態更新API
[**update_fee_model_api_v1_fee_model_fee_model_id_put**](DefaultApi.md#update_fee_model_api_v1_fee_model_fee_model_id_put) | **PUT** /api/v1/fee-model/{fee_model_id} | 利用料モデル変更API


# **check_transaction_eligibility_api_v1_data_exchange_transaction_eligibility_post**
> TransactionEligibilityResponse check_transaction_eligibility_api_v1_data_exchange_transaction_eligibility_post(user_agent, x_tracking_id, content_type, x_payment_api_key, transaction_eligibility_request, accept_language=accept_language)

取引可否確認API

取引可否確認API

### Example

* Bearer Authentication (HTTPBearer):

```python
import ods_sdk_payment
from ods_sdk_payment.models.transaction_eligibility_request import TransactionEligibilityRequest
from ods_sdk_payment.models.transaction_eligibility_response import TransactionEligibilityResponse
from ods_sdk_payment.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ods_sdk_payment.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: HTTPBearer
configuration = ods_sdk_payment.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with ods_sdk_payment.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ods_sdk_payment.DefaultApi(api_client)
    user_agent = 'user_agent_example' # str | 
    x_tracking_id = 'x_tracking_id_example' # str | 
    content_type = None # object | 
    x_payment_api_key = 'x_payment_api_key_example' # str | 
    transaction_eligibility_request = ods_sdk_payment.TransactionEligibilityRequest() # TransactionEligibilityRequest | 
    accept_language = 'ja-JP' # str |  (optional) (default to 'ja-JP')

    try:
        # 取引可否確認API
        api_response = api_instance.check_transaction_eligibility_api_v1_data_exchange_transaction_eligibility_post(user_agent, x_tracking_id, content_type, x_payment_api_key, transaction_eligibility_request, accept_language=accept_language)
        print("The response of DefaultApi->check_transaction_eligibility_api_v1_data_exchange_transaction_eligibility_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->check_transaction_eligibility_api_v1_data_exchange_transaction_eligibility_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_agent** | **str**|  | 
 **x_tracking_id** | **str**|  | 
 **content_type** | [**object**](.md)|  | 
 **x_payment_api_key** | **str**|  | 
 **transaction_eligibility_request** | [**TransactionEligibilityRequest**](TransactionEligibilityRequest.md)|  | 
 **accept_language** | **str**|  | [optional] [default to &#39;ja-JP&#39;]

### Return type

[**TransactionEligibilityResponse**](TransactionEligibilityResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 成功 |  * Cache-Control - キャッシュ制御指示 <br>  * X-TrackingId - リクエストトラッキング用UUID <br>  * Content-Security-Policy - XSS対策 <br>  * X-Content-Type-Options - MIMEスニッフィング防止 <br>  * Strict-Transport-Security - HTTPS強制 <br>  |
**400** | リクエストエラー |  * Cache-Control - キャッシュ制御指示 <br>  * X-TrackingId - リクエストトラッキング用UUID <br>  * Content-Security-Policy - XSS対策 <br>  * X-Content-Type-Options - MIMEスニッフィング防止 <br>  * Strict-Transport-Security - HTTPS強制 <br>  |
**401** | 認証エラー |  * Cache-Control - キャッシュ制御指示 <br>  * X-TrackingId - リクエストトラッキング用UUID <br>  * Content-Security-Policy - XSS対策 <br>  * X-Content-Type-Options - MIMEスニッフィング防止 <br>  * Strict-Transport-Security - HTTPS強制 <br>  |
**403** | 認可エラー |  * Cache-Control - キャッシュ制御指示 <br>  * X-TrackingId - リクエストトラッキング用UUID <br>  * Content-Security-Policy - XSS対策 <br>  * X-Content-Type-Options - MIMEスニッフィング防止 <br>  * Strict-Transport-Security - HTTPS強制 <br>  |
**404** | データなし |  * Cache-Control - キャッシュ制御指示 <br>  * X-TrackingId - リクエストトラッキング用UUID <br>  * Content-Security-Policy - XSS対策 <br>  * X-Content-Type-Options - MIMEスニッフィング防止 <br>  * Strict-Transport-Security - HTTPS強制 <br>  |
**409** | リソース競合エラー |  * Cache-Control - キャッシュ制御指示 <br>  * X-TrackingId - リクエストトラッキング用UUID <br>  * Content-Security-Policy - XSS対策 <br>  * X-Content-Type-Options - MIMEスニッフィング防止 <br>  * Strict-Transport-Security - HTTPS強制 <br>  |
**500** | サーバエラー |  * Cache-Control - キャッシュ制御指示 <br>  * X-TrackingId - リクエストトラッキング用UUID <br>  * Content-Security-Policy - XSS対策 <br>  * X-Content-Type-Options - MIMEスニッフィング防止 <br>  * Strict-Transport-Security - HTTPS強制 <br>  |
**422** | Validation Error |  * Cache-Control - キャッシュ制御指示 <br>  * X-TrackingId - リクエストトラッキング用UUID <br>  * Content-Security-Policy - XSS対策 <br>  * X-Content-Type-Options - MIMEスニッフィング防止 <br>  * Strict-Transport-Security - HTTPS強制 <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **check_transaction_eligibility_non_fee_model_api_v1_data_exchange_non_fee_model_transaction_eligibility_post**
> TransactionEligibilityNonFeeModelResponse check_transaction_eligibility_non_fee_model_api_v1_data_exchange_non_fee_model_transaction_eligibility_post(user_agent, x_tracking_id, content_type, x_payment_api_key, transaction_eligibility_non_fee_model_request, accept_language=accept_language)

取引可否確認API(利用料モデル無)

取引可否確認API(データID、利用料モデルが無い場合に使用)

### Example

* Bearer Authentication (HTTPBearer):

```python
import ods_sdk_payment
from ods_sdk_payment.models.transaction_eligibility_non_fee_model_request import TransactionEligibilityNonFeeModelRequest
from ods_sdk_payment.models.transaction_eligibility_non_fee_model_response import TransactionEligibilityNonFeeModelResponse
from ods_sdk_payment.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ods_sdk_payment.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: HTTPBearer
configuration = ods_sdk_payment.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with ods_sdk_payment.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ods_sdk_payment.DefaultApi(api_client)
    user_agent = 'user_agent_example' # str | 
    x_tracking_id = 'x_tracking_id_example' # str | 
    content_type = None # object | 
    x_payment_api_key = 'x_payment_api_key_example' # str | 
    transaction_eligibility_non_fee_model_request = ods_sdk_payment.TransactionEligibilityNonFeeModelRequest() # TransactionEligibilityNonFeeModelRequest | 
    accept_language = 'ja-JP' # str |  (optional) (default to 'ja-JP')

    try:
        # 取引可否確認API(利用料モデル無)
        api_response = api_instance.check_transaction_eligibility_non_fee_model_api_v1_data_exchange_non_fee_model_transaction_eligibility_post(user_agent, x_tracking_id, content_type, x_payment_api_key, transaction_eligibility_non_fee_model_request, accept_language=accept_language)
        print("The response of DefaultApi->check_transaction_eligibility_non_fee_model_api_v1_data_exchange_non_fee_model_transaction_eligibility_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->check_transaction_eligibility_non_fee_model_api_v1_data_exchange_non_fee_model_transaction_eligibility_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_agent** | **str**|  | 
 **x_tracking_id** | **str**|  | 
 **content_type** | [**object**](.md)|  | 
 **x_payment_api_key** | **str**|  | 
 **transaction_eligibility_non_fee_model_request** | [**TransactionEligibilityNonFeeModelRequest**](TransactionEligibilityNonFeeModelRequest.md)|  | 
 **accept_language** | **str**|  | [optional] [default to &#39;ja-JP&#39;]

### Return type

[**TransactionEligibilityNonFeeModelResponse**](TransactionEligibilityNonFeeModelResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 成功 |  * Cache-Control - キャッシュ制御指示 <br>  * X-TrackingId - リクエストトラッキング用UUID <br>  * Content-Security-Policy - XSS対策 <br>  * X-Content-Type-Options - MIMEスニッフィング防止 <br>  * Strict-Transport-Security - HTTPS強制 <br>  |
**400** | リクエストエラー |  * Cache-Control - キャッシュ制御指示 <br>  * X-TrackingId - リクエストトラッキング用UUID <br>  * Content-Security-Policy - XSS対策 <br>  * X-Content-Type-Options - MIMEスニッフィング防止 <br>  * Strict-Transport-Security - HTTPS強制 <br>  |
**401** | 認証エラー |  * Cache-Control - キャッシュ制御指示 <br>  * X-TrackingId - リクエストトラッキング用UUID <br>  * Content-Security-Policy - XSS対策 <br>  * X-Content-Type-Options - MIMEスニッフィング防止 <br>  * Strict-Transport-Security - HTTPS強制 <br>  |
**403** | 認可エラー |  * Cache-Control - キャッシュ制御指示 <br>  * X-TrackingId - リクエストトラッキング用UUID <br>  * Content-Security-Policy - XSS対策 <br>  * X-Content-Type-Options - MIMEスニッフィング防止 <br>  * Strict-Transport-Security - HTTPS強制 <br>  |
**404** | データなし |  * Cache-Control - キャッシュ制御指示 <br>  * X-TrackingId - リクエストトラッキング用UUID <br>  * Content-Security-Policy - XSS対策 <br>  * X-Content-Type-Options - MIMEスニッフィング防止 <br>  * Strict-Transport-Security - HTTPS強制 <br>  |
**409** | リソース競合エラー |  * Cache-Control - キャッシュ制御指示 <br>  * X-TrackingId - リクエストトラッキング用UUID <br>  * Content-Security-Policy - XSS対策 <br>  * X-Content-Type-Options - MIMEスニッフィング防止 <br>  * Strict-Transport-Security - HTTPS強制 <br>  |
**500** | サーバエラー |  * Cache-Control - キャッシュ制御指示 <br>  * X-TrackingId - リクエストトラッキング用UUID <br>  * Content-Security-Policy - XSS対策 <br>  * X-Content-Type-Options - MIMEスニッフィング防止 <br>  * Strict-Transport-Security - HTTPS強制 <br>  |
**422** | Validation Error |  * Cache-Control - キャッシュ制御指示 <br>  * X-TrackingId - リクエストトラッキング用UUID <br>  * Content-Security-Policy - XSS対策 <br>  * X-Content-Type-Options - MIMEスニッフィング防止 <br>  * Strict-Transport-Security - HTTPS強制 <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **confirm_data_exchange_api_v1_data_exchange_non_fee_model_confirm_post**
> DataExchangeStatusNonFeeModelResponse confirm_data_exchange_api_v1_data_exchange_non_fee_model_confirm_post(user_agent, x_tracking_id, content_type, x_payment_api_key, data_exchange_non_fee_model_request, accept_language=accept_language)

データ交換取引金額確定用API(利用料モデル無)

データ交換取引金額確定用API(データID、利用料モデルが無い場合に使用)

### Example

* Bearer Authentication (HTTPBearer):

```python
import ods_sdk_payment
from ods_sdk_payment.models.data_exchange_non_fee_model_request import DataExchangeNonFeeModelRequest
from ods_sdk_payment.models.data_exchange_status_non_fee_model_response import DataExchangeStatusNonFeeModelResponse
from ods_sdk_payment.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ods_sdk_payment.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: HTTPBearer
configuration = ods_sdk_payment.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with ods_sdk_payment.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ods_sdk_payment.DefaultApi(api_client)
    user_agent = 'user_agent_example' # str | 
    x_tracking_id = 'x_tracking_id_example' # str | 
    content_type = None # object | 
    x_payment_api_key = 'x_payment_api_key_example' # str | 
    data_exchange_non_fee_model_request = ods_sdk_payment.DataExchangeNonFeeModelRequest() # DataExchangeNonFeeModelRequest | 
    accept_language = 'ja-JP' # str |  (optional) (default to 'ja-JP')

    try:
        # データ交換取引金額確定用API(利用料モデル無)
        api_response = api_instance.confirm_data_exchange_api_v1_data_exchange_non_fee_model_confirm_post(user_agent, x_tracking_id, content_type, x_payment_api_key, data_exchange_non_fee_model_request, accept_language=accept_language)
        print("The response of DefaultApi->confirm_data_exchange_api_v1_data_exchange_non_fee_model_confirm_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->confirm_data_exchange_api_v1_data_exchange_non_fee_model_confirm_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_agent** | **str**|  | 
 **x_tracking_id** | **str**|  | 
 **content_type** | [**object**](.md)|  | 
 **x_payment_api_key** | **str**|  | 
 **data_exchange_non_fee_model_request** | [**DataExchangeNonFeeModelRequest**](DataExchangeNonFeeModelRequest.md)|  | 
 **accept_language** | **str**|  | [optional] [default to &#39;ja-JP&#39;]

### Return type

[**DataExchangeStatusNonFeeModelResponse**](DataExchangeStatusNonFeeModelResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 成功 |  * Cache-Control - キャッシュ制御指示 <br>  * X-TrackingId - リクエストトラッキング用UUID <br>  * Content-Security-Policy - XSS対策 <br>  * X-Content-Type-Options - MIMEスニッフィング防止 <br>  * Strict-Transport-Security - HTTPS強制 <br>  |
**400** | リクエストエラー |  * Cache-Control - キャッシュ制御指示 <br>  * X-TrackingId - リクエストトラッキング用UUID <br>  * Content-Security-Policy - XSS対策 <br>  * X-Content-Type-Options - MIMEスニッフィング防止 <br>  * Strict-Transport-Security - HTTPS強制 <br>  |
**401** | 認証エラー |  * Cache-Control - キャッシュ制御指示 <br>  * X-TrackingId - リクエストトラッキング用UUID <br>  * Content-Security-Policy - XSS対策 <br>  * X-Content-Type-Options - MIMEスニッフィング防止 <br>  * Strict-Transport-Security - HTTPS強制 <br>  |
**403** | 認可エラー |  * Cache-Control - キャッシュ制御指示 <br>  * X-TrackingId - リクエストトラッキング用UUID <br>  * Content-Security-Policy - XSS対策 <br>  * X-Content-Type-Options - MIMEスニッフィング防止 <br>  * Strict-Transport-Security - HTTPS強制 <br>  |
**404** | データなし |  * Cache-Control - キャッシュ制御指示 <br>  * X-TrackingId - リクエストトラッキング用UUID <br>  * Content-Security-Policy - XSS対策 <br>  * X-Content-Type-Options - MIMEスニッフィング防止 <br>  * Strict-Transport-Security - HTTPS強制 <br>  |
**409** | リソース競合エラー |  * Cache-Control - キャッシュ制御指示 <br>  * X-TrackingId - リクエストトラッキング用UUID <br>  * Content-Security-Policy - XSS対策 <br>  * X-Content-Type-Options - MIMEスニッフィング防止 <br>  * Strict-Transport-Security - HTTPS強制 <br>  |
**500** | サーバエラー |  * Cache-Control - キャッシュ制御指示 <br>  * X-TrackingId - リクエストトラッキング用UUID <br>  * Content-Security-Policy - XSS対策 <br>  * X-Content-Type-Options - MIMEスニッフィング防止 <br>  * Strict-Transport-Security - HTTPS強制 <br>  |
**422** | Validation Error |  * Cache-Control - キャッシュ制御指示 <br>  * X-TrackingId - リクエストトラッキング用UUID <br>  * Content-Security-Policy - XSS対策 <br>  * X-Content-Type-Options - MIMEスニッフィング防止 <br>  * Strict-Transport-Security - HTTPS強制 <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_fee_model_api_v1_fee_model_post**
> FeeModelResponse create_fee_model_api_v1_fee_model_post(user_agent, x_tracking_id, content_type, x_payment_api_key, fee_model_create_request, accept_language=accept_language)

利用料モデル登録API

利用料モデルを新規登録します。

### Example

* Bearer Authentication (HTTPBearer):

```python
import ods_sdk_payment
from ods_sdk_payment.models.fee_model_create_request import FeeModelCreateRequest
from ods_sdk_payment.models.fee_model_response import FeeModelResponse
from ods_sdk_payment.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ods_sdk_payment.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: HTTPBearer
configuration = ods_sdk_payment.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with ods_sdk_payment.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ods_sdk_payment.DefaultApi(api_client)
    user_agent = 'user_agent_example' # str | 
    x_tracking_id = 'x_tracking_id_example' # str | 
    content_type = None # object | 
    x_payment_api_key = 'x_payment_api_key_example' # str | 
    fee_model_create_request = ods_sdk_payment.FeeModelCreateRequest() # FeeModelCreateRequest | 
    accept_language = 'ja-JP' # str |  (optional) (default to 'ja-JP')

    try:
        # 利用料モデル登録API
        api_response = api_instance.create_fee_model_api_v1_fee_model_post(user_agent, x_tracking_id, content_type, x_payment_api_key, fee_model_create_request, accept_language=accept_language)
        print("The response of DefaultApi->create_fee_model_api_v1_fee_model_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->create_fee_model_api_v1_fee_model_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_agent** | **str**|  | 
 **x_tracking_id** | **str**|  | 
 **content_type** | [**object**](.md)|  | 
 **x_payment_api_key** | **str**|  | 
 **fee_model_create_request** | [**FeeModelCreateRequest**](FeeModelCreateRequest.md)|  | 
 **accept_language** | **str**|  | [optional] [default to &#39;ja-JP&#39;]

### Return type

[**FeeModelResponse**](FeeModelResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | 成功 |  * Cache-Control - キャッシュ制御指示 <br>  * X-TrackingId - リクエストトラッキング用UUID <br>  * Content-Security-Policy - XSS対策 <br>  * X-Content-Type-Options - MIMEスニッフィング防止 <br>  * Strict-Transport-Security - HTTPS強制 <br>  |
**400** | パラメータエラー |  * Cache-Control - キャッシュ制御指示 <br>  * X-TrackingId - リクエストトラッキング用UUID <br>  * Content-Security-Policy - XSS対策 <br>  * X-Content-Type-Options - MIMEスニッフィング防止 <br>  * Strict-Transport-Security - HTTPS強制 <br>  |
**401** | 認証エラー |  * Cache-Control - キャッシュ制御指示 <br>  * X-TrackingId - リクエストトラッキング用UUID <br>  * Content-Security-Policy - XSS対策 <br>  * X-Content-Type-Options - MIMEスニッフィング防止 <br>  * Strict-Transport-Security - HTTPS強制 <br>  |
**403** | 認可エラー |  * Cache-Control - キャッシュ制御指示 <br>  * X-TrackingId - リクエストトラッキング用UUID <br>  * Content-Security-Policy - XSS対策 <br>  * X-Content-Type-Options - MIMEスニッフィング防止 <br>  * Strict-Transport-Security - HTTPS強制 <br>  |
**409** | リソース競合エラー |  * Cache-Control - キャッシュ制御指示 <br>  * X-TrackingId - リクエストトラッキング用UUID <br>  * Content-Security-Policy - XSS対策 <br>  * X-Content-Type-Options - MIMEスニッフィング防止 <br>  * Strict-Transport-Security - HTTPS強制 <br>  |
**500** | サーバエラー |  * Cache-Control - キャッシュ制御指示 <br>  * X-TrackingId - リクエストトラッキング用UUID <br>  * Content-Security-Policy - XSS対策 <br>  * X-Content-Type-Options - MIMEスニッフィング防止 <br>  * Strict-Transport-Security - HTTPS強制 <br>  |
**422** | Validation Error |  * Cache-Control - キャッシュ制御指示 <br>  * X-TrackingId - リクエストトラッキング用UUID <br>  * Content-Security-Policy - XSS対策 <br>  * X-Content-Type-Options - MIMEスニッフィング防止 <br>  * Strict-Transport-Security - HTTPS強制 <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_fee_model_api_v1_fee_model_fee_model_id_delete**
> delete_fee_model_api_v1_fee_model_fee_model_id_delete(fee_model_id, user_agent, x_tracking_id, content_type, x_payment_api_key, accept_language=accept_language)

利用料モデル削除API

指定した利用料モデルを削除します。

### Example

* Bearer Authentication (HTTPBearer):

```python
import ods_sdk_payment
from ods_sdk_payment.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ods_sdk_payment.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: HTTPBearer
configuration = ods_sdk_payment.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with ods_sdk_payment.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ods_sdk_payment.DefaultApi(api_client)
    fee_model_id = 'fee_model_id_example' # str | 
    user_agent = 'user_agent_example' # str | 
    x_tracking_id = 'x_tracking_id_example' # str | 
    content_type = None # object | 
    x_payment_api_key = 'x_payment_api_key_example' # str | 
    accept_language = 'ja-JP' # str |  (optional) (default to 'ja-JP')

    try:
        # 利用料モデル削除API
        api_instance.delete_fee_model_api_v1_fee_model_fee_model_id_delete(fee_model_id, user_agent, x_tracking_id, content_type, x_payment_api_key, accept_language=accept_language)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_fee_model_api_v1_fee_model_fee_model_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fee_model_id** | **str**|  | 
 **user_agent** | **str**|  | 
 **x_tracking_id** | **str**|  | 
 **content_type** | [**object**](.md)|  | 
 **x_payment_api_key** | **str**|  | 
 **accept_language** | **str**|  | [optional] [default to &#39;ja-JP&#39;]

### Return type

void (empty response body)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | 成功 |  * Cache-Control - キャッシュ制御指示 <br>  * X-TrackingId - リクエストトラッキング用UUID <br>  * Content-Security-Policy - XSS対策 <br>  * X-Content-Type-Options - MIMEスニッフィング防止 <br>  * Strict-Transport-Security - HTTPS強制 <br>  |
**400** | パラメータエラー |  * Cache-Control - キャッシュ制御指示 <br>  * X-TrackingId - リクエストトラッキング用UUID <br>  * Content-Security-Policy - XSS対策 <br>  * X-Content-Type-Options - MIMEスニッフィング防止 <br>  * Strict-Transport-Security - HTTPS強制 <br>  |
**401** | 認証エラー |  * Cache-Control - キャッシュ制御指示 <br>  * X-TrackingId - リクエストトラッキング用UUID <br>  * Content-Security-Policy - XSS対策 <br>  * X-Content-Type-Options - MIMEスニッフィング防止 <br>  * Strict-Transport-Security - HTTPS強制 <br>  |
**403** | 認可エラー |  * Cache-Control - キャッシュ制御指示 <br>  * X-TrackingId - リクエストトラッキング用UUID <br>  * Content-Security-Policy - XSS対策 <br>  * X-Content-Type-Options - MIMEスニッフィング防止 <br>  * Strict-Transport-Security - HTTPS強制 <br>  |
**404** | 該当データなし |  * Cache-Control - キャッシュ制御指示 <br>  * X-TrackingId - リクエストトラッキング用UUID <br>  * Content-Security-Policy - XSS対策 <br>  * X-Content-Type-Options - MIMEスニッフィング防止 <br>  * Strict-Transport-Security - HTTPS強制 <br>  |
**409** | リソース競合エラー |  * Cache-Control - キャッシュ制御指示 <br>  * X-TrackingId - リクエストトラッキング用UUID <br>  * Content-Security-Policy - XSS対策 <br>  * X-Content-Type-Options - MIMEスニッフィング防止 <br>  * Strict-Transport-Security - HTTPS強制 <br>  |
**500** | サーバエラー |  * Cache-Control - キャッシュ制御指示 <br>  * X-TrackingId - リクエストトラッキング用UUID <br>  * Content-Security-Policy - XSS対策 <br>  * X-Content-Type-Options - MIMEスニッフィング防止 <br>  * Strict-Transport-Security - HTTPS強制 <br>  |
**422** | Validation Error |  * Cache-Control - キャッシュ制御指示 <br>  * X-TrackingId - リクエストトラッキング用UUID <br>  * Content-Security-Policy - XSS対策 <br>  * X-Content-Type-Options - MIMEスニッフィング防止 <br>  * Strict-Transport-Security - HTTPS強制 <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_billing_schedule_api_v1_billing_post**
> BillingAmountListResponse get_billing_schedule_api_v1_billing_post(user_agent, x_tracking_id, content_type, x_payment_api_key, billing_schedule_request, accept_language=accept_language)

請求予定額取得API

指定期間・データ利用者IDで請求予定額リストを返却します。

### Example

* Bearer Authentication (HTTPBearer):

```python
import ods_sdk_payment
from ods_sdk_payment.models.billing_amount_list_response import BillingAmountListResponse
from ods_sdk_payment.models.billing_schedule_request import BillingScheduleRequest
from ods_sdk_payment.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ods_sdk_payment.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: HTTPBearer
configuration = ods_sdk_payment.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with ods_sdk_payment.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ods_sdk_payment.DefaultApi(api_client)
    user_agent = 'user_agent_example' # str | 
    x_tracking_id = 'x_tracking_id_example' # str | 
    content_type = None # object | 
    x_payment_api_key = 'x_payment_api_key_example' # str | 
    billing_schedule_request = ods_sdk_payment.BillingScheduleRequest() # BillingScheduleRequest | 
    accept_language = 'ja-JP' # str |  (optional) (default to 'ja-JP')

    try:
        # 請求予定額取得API
        api_response = api_instance.get_billing_schedule_api_v1_billing_post(user_agent, x_tracking_id, content_type, x_payment_api_key, billing_schedule_request, accept_language=accept_language)
        print("The response of DefaultApi->get_billing_schedule_api_v1_billing_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_billing_schedule_api_v1_billing_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_agent** | **str**|  | 
 **x_tracking_id** | **str**|  | 
 **content_type** | [**object**](.md)|  | 
 **x_payment_api_key** | **str**|  | 
 **billing_schedule_request** | [**BillingScheduleRequest**](BillingScheduleRequest.md)|  | 
 **accept_language** | **str**|  | [optional] [default to &#39;ja-JP&#39;]

### Return type

[**BillingAmountListResponse**](BillingAmountListResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 成功 |  * Cache-Control - キャッシュ制御指示 <br>  * X-TrackingId - リクエストトラッキング用UUID <br>  * Content-Security-Policy - XSS対策 <br>  * X-Content-Type-Options - MIMEスニッフィング防止 <br>  * Strict-Transport-Security - HTTPS強制 <br>  |
**400** | パラメータエラー |  * Cache-Control - キャッシュ制御指示 <br>  * X-TrackingId - リクエストトラッキング用UUID <br>  * Content-Security-Policy - XSS対策 <br>  * X-Content-Type-Options - MIMEスニッフィング防止 <br>  * Strict-Transport-Security - HTTPS強制 <br>  |
**401** | 認証エラー |  * Cache-Control - キャッシュ制御指示 <br>  * X-TrackingId - リクエストトラッキング用UUID <br>  * Content-Security-Policy - XSS対策 <br>  * X-Content-Type-Options - MIMEスニッフィング防止 <br>  * Strict-Transport-Security - HTTPS強制 <br>  |
**403** | 認可エラー |  * Cache-Control - キャッシュ制御指示 <br>  * X-TrackingId - リクエストトラッキング用UUID <br>  * Content-Security-Policy - XSS対策 <br>  * X-Content-Type-Options - MIMEスニッフィング防止 <br>  * Strict-Transport-Security - HTTPS強制 <br>  |
**500** | サーバエラー |  * Cache-Control - キャッシュ制御指示 <br>  * X-TrackingId - リクエストトラッキング用UUID <br>  * Content-Security-Policy - XSS対策 <br>  * X-Content-Type-Options - MIMEスニッフィング防止 <br>  * Strict-Transport-Security - HTTPS強制 <br>  |
**422** | Validation Error |  * Cache-Control - キャッシュ制御指示 <br>  * X-TrackingId - リクエストトラッキング用UUID <br>  * Content-Security-Policy - XSS対策 <br>  * X-Content-Type-Options - MIMEスニッフィング防止 <br>  * Strict-Transport-Security - HTTPS強制 <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_payment_schedule_api_v1_payment_post**
> PaymentAmountListResponse get_payment_schedule_api_v1_payment_post(user_agent, x_tracking_id, content_type, x_payment_api_key, payment_schedule_request, accept_language=accept_language)

支払予定額取得API

指定期間・データ提供者IDで支払（受領）予定額リストを返却します。

### Example

* Bearer Authentication (HTTPBearer):

```python
import ods_sdk_payment
from ods_sdk_payment.models.payment_amount_list_response import PaymentAmountListResponse
from ods_sdk_payment.models.payment_schedule_request import PaymentScheduleRequest
from ods_sdk_payment.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ods_sdk_payment.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: HTTPBearer
configuration = ods_sdk_payment.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with ods_sdk_payment.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ods_sdk_payment.DefaultApi(api_client)
    user_agent = 'user_agent_example' # str | 
    x_tracking_id = 'x_tracking_id_example' # str | 
    content_type = None # object | 
    x_payment_api_key = 'x_payment_api_key_example' # str | 
    payment_schedule_request = ods_sdk_payment.PaymentScheduleRequest() # PaymentScheduleRequest | 
    accept_language = 'ja-JP' # str |  (optional) (default to 'ja-JP')

    try:
        # 支払予定額取得API
        api_response = api_instance.get_payment_schedule_api_v1_payment_post(user_agent, x_tracking_id, content_type, x_payment_api_key, payment_schedule_request, accept_language=accept_language)
        print("The response of DefaultApi->get_payment_schedule_api_v1_payment_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_payment_schedule_api_v1_payment_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_agent** | **str**|  | 
 **x_tracking_id** | **str**|  | 
 **content_type** | [**object**](.md)|  | 
 **x_payment_api_key** | **str**|  | 
 **payment_schedule_request** | [**PaymentScheduleRequest**](PaymentScheduleRequest.md)|  | 
 **accept_language** | **str**|  | [optional] [default to &#39;ja-JP&#39;]

### Return type

[**PaymentAmountListResponse**](PaymentAmountListResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 成功 |  * Cache-Control - キャッシュ制御指示 <br>  * X-TrackingId - リクエストトラッキング用UUID <br>  * Content-Security-Policy - XSS対策 <br>  * X-Content-Type-Options - MIMEスニッフィング防止 <br>  * Strict-Transport-Security - HTTPS強制 <br>  |
**400** | パラメータエラー |  * Cache-Control - キャッシュ制御指示 <br>  * X-TrackingId - リクエストトラッキング用UUID <br>  * Content-Security-Policy - XSS対策 <br>  * X-Content-Type-Options - MIMEスニッフィング防止 <br>  * Strict-Transport-Security - HTTPS強制 <br>  |
**401** | 認証エラー |  * Cache-Control - キャッシュ制御指示 <br>  * X-TrackingId - リクエストトラッキング用UUID <br>  * Content-Security-Policy - XSS対策 <br>  * X-Content-Type-Options - MIMEスニッフィング防止 <br>  * Strict-Transport-Security - HTTPS強制 <br>  |
**403** | 認可エラー |  * Cache-Control - キャッシュ制御指示 <br>  * X-TrackingId - リクエストトラッキング用UUID <br>  * Content-Security-Policy - XSS対策 <br>  * X-Content-Type-Options - MIMEスニッフィング防止 <br>  * Strict-Transport-Security - HTTPS強制 <br>  |
**500** | サーバエラー |  * Cache-Control - キャッシュ制御指示 <br>  * X-TrackingId - リクエストトラッキング用UUID <br>  * Content-Security-Policy - XSS対策 <br>  * X-Content-Type-Options - MIMEスニッフィング防止 <br>  * Strict-Transport-Security - HTTPS強制 <br>  |
**422** | Validation Error |  * Cache-Control - キャッシュ制御指示 <br>  * X-TrackingId - リクエストトラッキング用UUID <br>  * Content-Security-Policy - XSS対策 <br>  * X-Content-Type-Options - MIMEスニッフィング防止 <br>  * Strict-Transport-Security - HTTPS強制 <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_fee_models_api_v1_fee_model_get**
> FeeModelListResponse list_fee_models_api_v1_fee_model_get(user_agent, x_tracking_id, content_type, x_payment_api_key, accept_language=accept_language)

利用料モデル一覧取得API

すべての利用料モデルを一覧取得します。

### Example

* Bearer Authentication (HTTPBearer):

```python
import ods_sdk_payment
from ods_sdk_payment.models.fee_model_list_response import FeeModelListResponse
from ods_sdk_payment.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ods_sdk_payment.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: HTTPBearer
configuration = ods_sdk_payment.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with ods_sdk_payment.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ods_sdk_payment.DefaultApi(api_client)
    user_agent = 'user_agent_example' # str | 
    x_tracking_id = 'x_tracking_id_example' # str | 
    content_type = None # object | 
    x_payment_api_key = 'x_payment_api_key_example' # str | 
    accept_language = 'ja-JP' # str |  (optional) (default to 'ja-JP')

    try:
        # 利用料モデル一覧取得API
        api_response = api_instance.list_fee_models_api_v1_fee_model_get(user_agent, x_tracking_id, content_type, x_payment_api_key, accept_language=accept_language)
        print("The response of DefaultApi->list_fee_models_api_v1_fee_model_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->list_fee_models_api_v1_fee_model_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_agent** | **str**|  | 
 **x_tracking_id** | **str**|  | 
 **content_type** | [**object**](.md)|  | 
 **x_payment_api_key** | **str**|  | 
 **accept_language** | **str**|  | [optional] [default to &#39;ja-JP&#39;]

### Return type

[**FeeModelListResponse**](FeeModelListResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 成功 |  * Cache-Control - キャッシュ制御指示 <br>  * X-TrackingId - リクエストトラッキング用UUID <br>  * Content-Security-Policy - XSS対策 <br>  * X-Content-Type-Options - MIMEスニッフィング防止 <br>  * Strict-Transport-Security - HTTPS強制 <br>  * ETag - リソースのバージョン識別子 <br>  * Last-Modified - リソースの最終更新日時 <br>  |
**400** | パラメータエラー |  * Cache-Control - キャッシュ制御指示 <br>  * X-TrackingId - リクエストトラッキング用UUID <br>  * Content-Security-Policy - XSS対策 <br>  * X-Content-Type-Options - MIMEスニッフィング防止 <br>  * Strict-Transport-Security - HTTPS強制 <br>  * ETag - リソースのバージョン識別子 <br>  * Last-Modified - リソースの最終更新日時 <br>  |
**401** | 認証エラー |  * Cache-Control - キャッシュ制御指示 <br>  * X-TrackingId - リクエストトラッキング用UUID <br>  * Content-Security-Policy - XSS対策 <br>  * X-Content-Type-Options - MIMEスニッフィング防止 <br>  * Strict-Transport-Security - HTTPS強制 <br>  * ETag - リソースのバージョン識別子 <br>  * Last-Modified - リソースの最終更新日時 <br>  |
**403** | 認可エラー |  * Cache-Control - キャッシュ制御指示 <br>  * X-TrackingId - リクエストトラッキング用UUID <br>  * Content-Security-Policy - XSS対策 <br>  * X-Content-Type-Options - MIMEスニッフィング防止 <br>  * Strict-Transport-Security - HTTPS強制 <br>  * ETag - リソースのバージョン識別子 <br>  * Last-Modified - リソースの最終更新日時 <br>  |
**500** | サーバエラー |  * Cache-Control - キャッシュ制御指示 <br>  * X-TrackingId - リクエストトラッキング用UUID <br>  * Content-Security-Policy - XSS対策 <br>  * X-Content-Type-Options - MIMEスニッフィング防止 <br>  * Strict-Transport-Security - HTTPS強制 <br>  * ETag - リソースのバージョン識別子 <br>  * Last-Modified - リソースの最終更新日時 <br>  |
**422** | Validation Error |  * Cache-Control - キャッシュ制御指示 <br>  * X-TrackingId - リクエストトラッキング用UUID <br>  * Content-Security-Policy - XSS対策 <br>  * X-Content-Type-Options - MIMEスニッフィング防止 <br>  * Strict-Transport-Security - HTTPS強制 <br>  * ETag - リソースのバージョン識別子 <br>  * Last-Modified - リソースの最終更新日時 <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register_data_exchange_status_api_v1_data_exchange_status_post**
> DataExchangeStatusResponse register_data_exchange_status_api_v1_data_exchange_status_post(user_agent, x_tracking_id, content_type, x_payment_api_key, data_exchange_request, accept_language=accept_language)

データ交換状態登録API

データ交換処理の完了を精算決済機能に登録します。

### Example

* Bearer Authentication (HTTPBearer):

```python
import ods_sdk_payment
from ods_sdk_payment.models.data_exchange_request import DataExchangeRequest
from ods_sdk_payment.models.data_exchange_status_response import DataExchangeStatusResponse
from ods_sdk_payment.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ods_sdk_payment.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: HTTPBearer
configuration = ods_sdk_payment.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with ods_sdk_payment.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ods_sdk_payment.DefaultApi(api_client)
    user_agent = 'user_agent_example' # str | 
    x_tracking_id = 'x_tracking_id_example' # str | 
    content_type = None # object | 
    x_payment_api_key = 'x_payment_api_key_example' # str | 
    data_exchange_request = ods_sdk_payment.DataExchangeRequest() # DataExchangeRequest | 
    accept_language = 'ja-JP' # str |  (optional) (default to 'ja-JP')

    try:
        # データ交換状態登録API
        api_response = api_instance.register_data_exchange_status_api_v1_data_exchange_status_post(user_agent, x_tracking_id, content_type, x_payment_api_key, data_exchange_request, accept_language=accept_language)
        print("The response of DefaultApi->register_data_exchange_status_api_v1_data_exchange_status_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->register_data_exchange_status_api_v1_data_exchange_status_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_agent** | **str**|  | 
 **x_tracking_id** | **str**|  | 
 **content_type** | [**object**](.md)|  | 
 **x_payment_api_key** | **str**|  | 
 **data_exchange_request** | [**DataExchangeRequest**](DataExchangeRequest.md)|  | 
 **accept_language** | **str**|  | [optional] [default to &#39;ja-JP&#39;]

### Return type

[**DataExchangeStatusResponse**](DataExchangeStatusResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 成功 |  * Cache-Control - キャッシュ制御指示 <br>  * X-TrackingId - リクエストトラッキング用UUID <br>  * Content-Security-Policy - XSS対策 <br>  * X-Content-Type-Options - MIMEスニッフィング防止 <br>  * Strict-Transport-Security - HTTPS強制 <br>  |
**400** | リクエストエラー |  * Cache-Control - キャッシュ制御指示 <br>  * X-TrackingId - リクエストトラッキング用UUID <br>  * Content-Security-Policy - XSS対策 <br>  * X-Content-Type-Options - MIMEスニッフィング防止 <br>  * Strict-Transport-Security - HTTPS強制 <br>  |
**401** | 認証エラー |  * Cache-Control - キャッシュ制御指示 <br>  * X-TrackingId - リクエストトラッキング用UUID <br>  * Content-Security-Policy - XSS対策 <br>  * X-Content-Type-Options - MIMEスニッフィング防止 <br>  * Strict-Transport-Security - HTTPS強制 <br>  |
**403** | 認可エラー |  * Cache-Control - キャッシュ制御指示 <br>  * X-TrackingId - リクエストトラッキング用UUID <br>  * Content-Security-Policy - XSS対策 <br>  * X-Content-Type-Options - MIMEスニッフィング防止 <br>  * Strict-Transport-Security - HTTPS強制 <br>  |
**404** | データなし |  * Cache-Control - キャッシュ制御指示 <br>  * X-TrackingId - リクエストトラッキング用UUID <br>  * Content-Security-Policy - XSS対策 <br>  * X-Content-Type-Options - MIMEスニッフィング防止 <br>  * Strict-Transport-Security - HTTPS強制 <br>  |
**409** | リソース競合エラー |  * Cache-Control - キャッシュ制御指示 <br>  * X-TrackingId - リクエストトラッキング用UUID <br>  * Content-Security-Policy - XSS対策 <br>  * X-Content-Type-Options - MIMEスニッフィング防止 <br>  * Strict-Transport-Security - HTTPS強制 <br>  |
**500** | サーバエラー |  * Cache-Control - キャッシュ制御指示 <br>  * X-TrackingId - リクエストトラッキング用UUID <br>  * Content-Security-Policy - XSS対策 <br>  * X-Content-Type-Options - MIMEスニッフィング防止 <br>  * Strict-Transport-Security - HTTPS強制 <br>  |
**422** | Validation Error |  * Cache-Control - キャッシュ制御指示 <br>  * X-TrackingId - リクエストトラッキング用UUID <br>  * Content-Security-Policy - XSS対策 <br>  * X-Content-Type-Options - MIMEスニッフィング防止 <br>  * Strict-Transport-Security - HTTPS強制 <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_data_exchange_status_api_v1_data_exchange_status_put**
> DataExchangeStatusResponse update_data_exchange_status_api_v1_data_exchange_status_put(user_agent, x_tracking_id, content_type, x_payment_api_key, data_exchange_status_request, accept_language=accept_language)

データ交換状態更新API

データ交換処理のステータスを変更します。

### Example

* Bearer Authentication (HTTPBearer):

```python
import ods_sdk_payment
from ods_sdk_payment.models.data_exchange_status_request import DataExchangeStatusRequest
from ods_sdk_payment.models.data_exchange_status_response import DataExchangeStatusResponse
from ods_sdk_payment.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ods_sdk_payment.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: HTTPBearer
configuration = ods_sdk_payment.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with ods_sdk_payment.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ods_sdk_payment.DefaultApi(api_client)
    user_agent = 'user_agent_example' # str | 
    x_tracking_id = 'x_tracking_id_example' # str | 
    content_type = None # object | 
    x_payment_api_key = 'x_payment_api_key_example' # str | 
    data_exchange_status_request = ods_sdk_payment.DataExchangeStatusRequest() # DataExchangeStatusRequest | 
    accept_language = 'ja-JP' # str |  (optional) (default to 'ja-JP')

    try:
        # データ交換状態更新API
        api_response = api_instance.update_data_exchange_status_api_v1_data_exchange_status_put(user_agent, x_tracking_id, content_type, x_payment_api_key, data_exchange_status_request, accept_language=accept_language)
        print("The response of DefaultApi->update_data_exchange_status_api_v1_data_exchange_status_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->update_data_exchange_status_api_v1_data_exchange_status_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_agent** | **str**|  | 
 **x_tracking_id** | **str**|  | 
 **content_type** | [**object**](.md)|  | 
 **x_payment_api_key** | **str**|  | 
 **data_exchange_status_request** | [**DataExchangeStatusRequest**](DataExchangeStatusRequest.md)|  | 
 **accept_language** | **str**|  | [optional] [default to &#39;ja-JP&#39;]

### Return type

[**DataExchangeStatusResponse**](DataExchangeStatusResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 成功 |  * Cache-Control - キャッシュ制御指示 <br>  * X-TrackingId - リクエストトラッキング用UUID <br>  * Content-Security-Policy - XSS対策 <br>  * X-Content-Type-Options - MIMEスニッフィング防止 <br>  * Strict-Transport-Security - HTTPS強制 <br>  |
**400** | リクエストエラー |  * Cache-Control - キャッシュ制御指示 <br>  * X-TrackingId - リクエストトラッキング用UUID <br>  * Content-Security-Policy - XSS対策 <br>  * X-Content-Type-Options - MIMEスニッフィング防止 <br>  * Strict-Transport-Security - HTTPS強制 <br>  |
**401** | 認証エラー |  * Cache-Control - キャッシュ制御指示 <br>  * X-TrackingId - リクエストトラッキング用UUID <br>  * Content-Security-Policy - XSS対策 <br>  * X-Content-Type-Options - MIMEスニッフィング防止 <br>  * Strict-Transport-Security - HTTPS強制 <br>  |
**403** | 認可エラー |  * Cache-Control - キャッシュ制御指示 <br>  * X-TrackingId - リクエストトラッキング用UUID <br>  * Content-Security-Policy - XSS対策 <br>  * X-Content-Type-Options - MIMEスニッフィング防止 <br>  * Strict-Transport-Security - HTTPS強制 <br>  |
**404** | データなし |  * Cache-Control - キャッシュ制御指示 <br>  * X-TrackingId - リクエストトラッキング用UUID <br>  * Content-Security-Policy - XSS対策 <br>  * X-Content-Type-Options - MIMEスニッフィング防止 <br>  * Strict-Transport-Security - HTTPS強制 <br>  |
**409** | リソース競合エラー |  * Cache-Control - キャッシュ制御指示 <br>  * X-TrackingId - リクエストトラッキング用UUID <br>  * Content-Security-Policy - XSS対策 <br>  * X-Content-Type-Options - MIMEスニッフィング防止 <br>  * Strict-Transport-Security - HTTPS強制 <br>  |
**500** | サーバエラー |  * Cache-Control - キャッシュ制御指示 <br>  * X-TrackingId - リクエストトラッキング用UUID <br>  * Content-Security-Policy - XSS対策 <br>  * X-Content-Type-Options - MIMEスニッフィング防止 <br>  * Strict-Transport-Security - HTTPS強制 <br>  |
**422** | Validation Error |  * Cache-Control - キャッシュ制御指示 <br>  * X-TrackingId - リクエストトラッキング用UUID <br>  * Content-Security-Policy - XSS対策 <br>  * X-Content-Type-Options - MIMEスニッフィング防止 <br>  * Strict-Transport-Security - HTTPS強制 <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_fee_model_api_v1_fee_model_fee_model_id_put**
> FeeModelResponse update_fee_model_api_v1_fee_model_fee_model_id_put(fee_model_id, user_agent, x_tracking_id, content_type, x_payment_api_key, fee_model_update_request, accept_language=accept_language)

利用料モデル変更API

指定した利用料モデルを更新します。

### Example

* Bearer Authentication (HTTPBearer):

```python
import ods_sdk_payment
from ods_sdk_payment.models.fee_model_response import FeeModelResponse
from ods_sdk_payment.models.fee_model_update_request import FeeModelUpdateRequest
from ods_sdk_payment.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ods_sdk_payment.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: HTTPBearer
configuration = ods_sdk_payment.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with ods_sdk_payment.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ods_sdk_payment.DefaultApi(api_client)
    fee_model_id = 'fee_model_id_example' # str | 
    user_agent = 'user_agent_example' # str | 
    x_tracking_id = 'x_tracking_id_example' # str | 
    content_type = None # object | 
    x_payment_api_key = 'x_payment_api_key_example' # str | 
    fee_model_update_request = ods_sdk_payment.FeeModelUpdateRequest() # FeeModelUpdateRequest | 
    accept_language = 'ja-JP' # str |  (optional) (default to 'ja-JP')

    try:
        # 利用料モデル変更API
        api_response = api_instance.update_fee_model_api_v1_fee_model_fee_model_id_put(fee_model_id, user_agent, x_tracking_id, content_type, x_payment_api_key, fee_model_update_request, accept_language=accept_language)
        print("The response of DefaultApi->update_fee_model_api_v1_fee_model_fee_model_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->update_fee_model_api_v1_fee_model_fee_model_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fee_model_id** | **str**|  | 
 **user_agent** | **str**|  | 
 **x_tracking_id** | **str**|  | 
 **content_type** | [**object**](.md)|  | 
 **x_payment_api_key** | **str**|  | 
 **fee_model_update_request** | [**FeeModelUpdateRequest**](FeeModelUpdateRequest.md)|  | 
 **accept_language** | **str**|  | [optional] [default to &#39;ja-JP&#39;]

### Return type

[**FeeModelResponse**](FeeModelResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 成功 |  * Cache-Control - キャッシュ制御指示 <br>  * X-TrackingId - リクエストトラッキング用UUID <br>  * Content-Security-Policy - XSS対策 <br>  * X-Content-Type-Options - MIMEスニッフィング防止 <br>  * Strict-Transport-Security - HTTPS強制 <br>  |
**400** | パラメータエラー |  * Cache-Control - キャッシュ制御指示 <br>  * X-TrackingId - リクエストトラッキング用UUID <br>  * Content-Security-Policy - XSS対策 <br>  * X-Content-Type-Options - MIMEスニッフィング防止 <br>  * Strict-Transport-Security - HTTPS強制 <br>  |
**401** | 認証エラー |  * Cache-Control - キャッシュ制御指示 <br>  * X-TrackingId - リクエストトラッキング用UUID <br>  * Content-Security-Policy - XSS対策 <br>  * X-Content-Type-Options - MIMEスニッフィング防止 <br>  * Strict-Transport-Security - HTTPS強制 <br>  |
**403** | 認可エラー |  * Cache-Control - キャッシュ制御指示 <br>  * X-TrackingId - リクエストトラッキング用UUID <br>  * Content-Security-Policy - XSS対策 <br>  * X-Content-Type-Options - MIMEスニッフィング防止 <br>  * Strict-Transport-Security - HTTPS強制 <br>  |
**404** | 該当データなし |  * Cache-Control - キャッシュ制御指示 <br>  * X-TrackingId - リクエストトラッキング用UUID <br>  * Content-Security-Policy - XSS対策 <br>  * X-Content-Type-Options - MIMEスニッフィング防止 <br>  * Strict-Transport-Security - HTTPS強制 <br>  |
**409** | リソース競合エラー |  * Cache-Control - キャッシュ制御指示 <br>  * X-TrackingId - リクエストトラッキング用UUID <br>  * Content-Security-Policy - XSS対策 <br>  * X-Content-Type-Options - MIMEスニッフィング防止 <br>  * Strict-Transport-Security - HTTPS強制 <br>  |
**500** | サーバエラー |  * Cache-Control - キャッシュ制御指示 <br>  * X-TrackingId - リクエストトラッキング用UUID <br>  * Content-Security-Policy - XSS対策 <br>  * X-Content-Type-Options - MIMEスニッフィング防止 <br>  * Strict-Transport-Security - HTTPS強制 <br>  |
**422** | Validation Error |  * Cache-Control - キャッシュ制御指示 <br>  * X-TrackingId - リクエストトラッキング用UUID <br>  * Content-Security-Policy - XSS対策 <br>  * X-Content-Type-Options - MIMEスニッフィング防止 <br>  * Strict-Transport-Security - HTTPS強制 <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

