# open-data-spaces-sdk-client-library-python

ODS SDK for Onboarding - Python client library

## Overview

This repository contains procedures and deliverables for generating Python SDKs from OpenAPI specifications located in the `apidoc` directory.
Currently, the SDKs are generated separately from two specifications: L3 (Identity Component) and Payment (Clearing and Payment).

## Prerequisites

- Python 3.9 or later is installed.
- `npm` is available (used to run the OpenAPI Generator CLI).
- The following OpenAPI specifications exist in the repository.

  - `apidoc/L3/api-docs.yaml`
  - `apidoc/L3/config.yaml` (generation configuration)
  - `apidoc/payment/openapi.json`
  - `apidoc/payment/config.yaml` (generation configuration)

## SDK Generation Procedure

### Step 1 — Obtain OpenAPI Generator CLI

OpenAPI Generator is assumed to be installed via `npm`. You can check the version with the following command.

```bash
npx @openapitools/openapi-generator-cli version
```

If it is not installed, you can install it using the following command.

```bash
npm install -g @openapitools/openapi-generator-cli
```

### Step 2 — Specification Validation

```bash
npx @openapitools/openapi-generator-cli validate -i apidoc/L3/api-docs.yaml
npx @openapitools/openapi-generator-cli validate -i apidoc/payment/openapi.json
```

If validation errors occur, please fix them before proceeding with generation.

### Step 3 — Generate Python SDKs

Run the following commands to generate each Python client.

**Note:** If a certificate error such as (`unable to get local issuer certificate`) occurs (for example, in a proxy environment), please run the command with the environment variable `NODE_TLS_REJECT_UNAUTHORIZED=0` set to `0`.

#### Generate L3 SDK

```bash
npx @openapitools/openapi-generator-cli generate -i apidoc/L3/api-docs.yaml -g python -o generated/l3 -c apidoc/L3/config.yaml
```

#### Generate Payment SDK

```bash
npx @openapitools/openapi-generator-cli generate -i apidoc/payment/openapi.json -g python -o generated/payment -c apidoc/payment/config.yaml
```

### Step 4 — Install the Generated SDKs

Install the generated SDKs into a virtual environment (venv).

#### Create and Activate a Virtual Environment

```bash
# Create a virtual environment
python -m venv .venv

# Activate the virtual environment (Windows)
.venv\Scripts\activate

# Activate the virtual environment (Linux/macOS)
source .venv/bin/activate
```

#### Install the SDKs

```bash
# Install L3 SDK
cd generated/l3
pip install .
cd ../..

# Install Payment SDK
cd generated/payment
pip install .
cd ../..
```

### Step 5 — Usage Example

This is an example of using the generated client (it is assumed that the virtual environment is active).

#### Using the L3 SDK

```python
import ods_sdk_L3
from ods_sdk_L3.rest import ApiException
from pprint import pprint

configuration = ods_sdk_L3.Configuration(
    host = "http://localhost:8090"
)

with ods_sdk_L3.ApiClient(configuration) as api_client:
    auth_api = ods_sdk_L3.AuthTokenControllerApi(api_client)
    # ...
```

#### Using the Payment SDK

```python
import ods_sdk_payment
from ods_sdk_payment.rest import ApiException
from pprint import pprint

configuration = ods_sdk_payment.Configuration(
    host = "http://localhost:8080"
)

with ods_sdk_payment.ApiClient(configuration) as api_client:
    payment_api = ods_sdk_payment.DefaultApi(api_client)
    # ...
```


#### L3 SDK List

| Use Case | Class Name | Method Name | Example |
| :--- | :--- | :--- | :--- |
| Obtain an access token | `AuthTokenControllerApi` | `access_token` | [Details](#l3-access-token) |
| Retrieve authentication URL | `AuthUrlControllerApi` | `url` | [Details](#l3-auth-url) |
| Verify API key | `ApiKeyControllerApi` | `verify_api_key` | [Details](#l3-verify-api-key) |
| Register a client | `ClientsControllerApi` | `post_clients` | [Details](#l3-post-clients) |
| Retrieve client secret | `ClientsControllerApi` | `get_client_secret` | [Details](#l3-get-client-secret) |
| Retrieve operator list | `OperatorControllerApi` | `list_operator` | [Details](#l3-list-operator) |
| Register an operator | `OperatorControllerApi` | `post_operator` | [Details](#l3-post-operator) |
| Change password | `PasswordControllerApi` | `change_password` | [Details](#l3-change-password) |
| Retrieve password change URL | `PasswordUrlControllerApi` | `url1` | [Details](#l3-password-url) |
| Retrieve a plant | `PlantControllerApi` | `get_plant` | [Details](#l3-get-plant) |
| Register a plant | `PlantControllerApi` | `post_plant` | [Details](#l3-post-plant) |
| Obtain token via client authentication | `TokenClientControllerApi` | `client` | [Details](#l3-token-client) |
| Token introspection | `TokenIntrospectionControllerApi` | `token_introspection` | [Details](#l3-token-introspect) |
| Obtain token via password authentication | `TokenPasswordControllerApi` | `login` | [Details](#l3-token-password) |
| Refresh token | `TokenRefreshControllerApi` | `refresh` | [Details](#l3-token-refresh) |
| Register a user | `UserControllerApi` | `post_user` | [Details](#l3-post-user) |
| Retrieve authorization model | `AuthorizationControllerApi` | `get_api` | [Details](#l3-get-authz) |



#### Payment SDK List

| Use Case | Class Name | Method Name | Example |
| :--- | :--- | :--- | :--- |
| Register data exchange status | `DefaultApi` | `register_data_exchange_status_api_v1_data_exchange_status_post` | [Details](#pay-register-status) |
| Update data exchange status | `DefaultApi` | `update_data_exchange_status_api_v1_data_exchange_status_put` | [Details](#pay-update-status) |
| Retrieve fee model list | `DefaultApi` | `list_fee_models_api_v1_fee_model_get` | [Details](#pay-list-fee) |
| Register a fee model | `DefaultApi` | `create_fee_model_api_v1_fee_model_post` | [Details](#pay-create-fee) |
| Update a fee model | `DefaultApi` | `update_fee_model_api_v1_fee_model_fee_model_id_put` | [Details](#pay-update-fee) |
| Delete a fee model | `DefaultApi` | `delete_fee_model_api_v1_fee_model_fee_model_id_delete` | [Details](#pay-delete-fee) |
| Check transaction eligibility | `DefaultApi` | `check_transaction_eligibility_api_v1_data_exchange_transaction_eligibility_post` | [Details](#pay-check-eligibility) |
| Check transaction eligibility (no fee model) | `DefaultApi` | `check_transaction_eligibility_non_fee_model_api_v1_data_exchange_non_fee_model_transaction_eligibility_post` | [Details](#pay-check-eligibility-non-fee) |
| Confirm transaction amount (no fee model) | `DefaultApi` | `confirm_data_exchange_api_v1_data_exchange_non_fee_model_confirm_post` | [Details](#pay-confirm-non-fee) |
| Retrieve billing schedule | `DefaultApi` | `get_billing_schedule_api_v1_billing_post` | [Details](#pay-get-billing) |
| Retrieve payment schedule | `DefaultApi` | `get_payment_schedule_api_v1_payment_post` | [Details](#pay-get-payment) |

---

<div id="l3-access-token"></div>

#### Obtain an Access Token (L3)

```python
import ods_sdk_L3
from ods_sdk_L3.models.auth_token_request import AuthTokenRequest

configuration = ods_sdk_L3.Configuration(host="http://localhost:8090")
with ods_sdk_L3.ApiClient(configuration) as api_client:
    api_instance = ods_sdk_L3.AuthTokenControllerApi(api_client)
    auth_token_request = AuthTokenRequest(
        code="sample_code",
        client_id="sample_client_id",
        client_secret="sample_client_secret",
        redirect_uri="http://localhost/callback",
        code_verifier="sample_verifier"
    )
    api_response = api_instance.access_token(auth_token_request)
```

<div id="l3-post-clients"></div>

#### Register a Client (L3)

```python
import ods_sdk_L3
from ods_sdk_L3.models.post_clients_request import PostClientsRequest

configuration = ods_sdk_L3.Configuration(host="http://localhost:8090")
with ods_sdk_L3.ApiClient(configuration) as api_client:
    api_instance = ods_sdk_L3.ClientsControllerApi(api_client)
    post_clients_request = PostClientsRequest(
        client_name="Sample Client",
        redirect_uris=["http://localhost/callback"]
    )
    api_response = api_instance.post_clients(post_clients_request)
```

<div id="l3-verify-api-key"></div>

#### Verify API Key (L3)

```python
import ods_sdk_L3

configuration = ods_sdk_L3.Configuration(host="http://localhost:8090")
with ods_sdk_L3.ApiClient(configuration) as api_client:
    api_instance = ods_sdk_L3.ApiKeyControllerApi(api_client)
    api_key = "your_api_key_here"
    api_response = api_instance.verify_api_key(api_key=api_key)
```

<div id="l3-list-operator"></div>

#### Retrieve Operator List (L3)

```python
import ods_sdk_L3

configuration = ods_sdk_L3.Configuration(host="http://localhost:8090")
with ods_sdk_L3.ApiClient(configuration) as api_client:
    api_instance = ods_sdk_L3.OperatorControllerApi(api_client)
    api_response = api_instance.list_operator()
```

<div id="l3-post-user"></div>

#### Register a User (L3)

```python
import ods_sdk_L3

configuration = ods_sdk_L3.Configuration(host="http://localhost:8090")
with ods_sdk_L3.ApiClient(configuration) as api_client:
    api_instance = ods_sdk_L3.UserControllerApi(api_client)
    user_id = "sample_user_id"
    api_response = api_instance.post_user(body=user_id)
```

<div id="l3-auth-url"></div>

#### Retrieve Authentication URL (L3)

```python
import ods_sdk_L3
from ods_sdk_L3.models.auth_url_request import AuthUrlRequest

configuration = ods_sdk_L3.Configuration(host="http://localhost:8090")
with ods_sdk_L3.ApiClient(configuration) as api_client:
    api_instance = ods_sdk_L3.AuthUrlControllerApi(api_client)
    request = AuthUrlRequest(
        client_id="sample-client",
        redirect_uri="http://localhost/callback",
        scope="openid",
        state="sample-state",
        code_challenge="challenge",
        code_challenge_method="S256"
    )
    api_response = api_instance.url(request)
```

<div id="l3-get-client-secret"></div>

#### Retrieve Client Secret (L3)

```python
import ods_sdk_L3

configuration = ods_sdk_L3.Configuration(host="http://localhost:8090")
with ods_sdk_L3.ApiClient(configuration) as api_client:
    api_instance = ods_sdk_L3.ClientsControllerApi(api_client)
    client_uuid = "client-uuid-123"
    api_response = api_instance.get_client_secret(client_uuid)
```

<div id="l3-post-operator"></div>

#### Register an Operator (L3)

```python
import ods_sdk_L3
from ods_sdk_L3.models.post_operator_request import PostOperatorRequest

configuration = ods_sdk_L3.Configuration(host="http://localhost:8090")
with ods_sdk_L3.ApiClient(configuration) as api_client:
    api_instance = ods_sdk_L3.OperatorControllerApi(api_client)
    request = PostOperatorRequest(
        operator_name="New Operator",
        email="operator@example.com"
    )
    api_response = api_instance.post_operator(request)
```

<div id="l3-change-password"></div>

#### Change Password (L3)

```python
import ods_sdk_L3
from ods_sdk_L3.models.password_request import PasswordRequest

configuration = ods_sdk_L3.Configuration(host="http://localhost:8090")
with ods_sdk_L3.ApiClient(configuration) as api_client:
    api_instance = ods_sdk_L3.PasswordControllerApi(api_client)
    request = PasswordRequest(
        old_password="old-password",
        new_password="new-password"
    )
    api_response = api_instance.change_password(operator_id="op-123", password_request=request)
```

<div id="l3-password-url"></div>

#### Retrieve Password Change URL (L3)

```python
import ods_sdk_L3
from ods_sdk_L3.models.password_url_request import PasswordUrlRequest

configuration = ods_sdk_L3.Configuration(host="http://localhost:8090")
with ods_sdk_L3.ApiClient(configuration) as api_client:
    api_instance = ods_sdk_L3.PasswordUrlControllerApi(api_client)
    request = PasswordUrlRequest(
        email="user@example.com"
    )
    api_response = api_instance.url1(request)
```

<div id="l3-get-plant"></div>

#### Retrieve a Plant (L3)

```python
import ods_sdk_L3

configuration = ods_sdk_L3.Configuration(host="http://localhost:8090")
with ods_sdk_L3.ApiClient(configuration) as api_client:
    api_instance = ods_sdk_L3.PlantControllerApi(api_client)
    api_response = api_instance.get_plant(plant_id="plant-123")
```

<div id="l3-post-plant"></div>

#### Register a Plant (L3)

```python
import ods_sdk_L3
from ods_sdk_L3.models.post_plant_request import PostPlantRequest

configuration = ods_sdk_L3.Configuration(host="http://localhost:8090")
with ods_sdk_L3.ApiClient(configuration) as api_client:
    api_instance = ods_sdk_L3.PlantControllerApi(api_client)
    request = PostPlantRequest(
        plant_name="Main Plant",
        location="Tokyo"
    )
    api_response = api_instance.post_plant(request)
```

<div id="l3-token-client"></div>

#### Obtain Token via Client Authentication (L3)

```python
import ods_sdk_L3
from ods_sdk_L3.models.token_client_request import TokenClientRequest

configuration = ods_sdk_L3.Configuration(host="http://localhost:8090")
with ods_sdk_L3.ApiClient(configuration) as api_client:
    api_instance = ods_sdk_L3.TokenClientControllerApi(api_client)
    request = TokenClientRequest(
        client_id="client-id",
        client_secret="client-secret",
        grant_type="client_credentials"
    )
    api_response = api_instance.client(request)
```

<div id="l3-token-introspect"></div>

#### Token Introspection (L3)

```python
import ods_sdk_L3
from ods_sdk_L3.models.token_introspection_request import TokenIntrospectionRequest

configuration = ods_sdk_L3.Configuration(host="http://localhost:8090")
with ods_sdk_L3.ApiClient(configuration) as api_client:
    api_instance = ods_sdk_L3.TokenIntrospectionControllerApi(api_client)
    request = TokenIntrospectionRequest(
        token="access-token-to-check"
    )
    api_response = api_instance.token_introspection(request)
```

<div id="l3-token-password"></div>

#### Obtain Token via Password Authentication (L3)

```python
import ods_sdk_L3
from ods_sdk_L3.models.token_password_request import TokenPasswordRequest

configuration = ods_sdk_L3.Configuration(host="http://localhost:8090")
with ods_sdk_L3.ApiClient(configuration) as api_client:
    api_instance = ods_sdk_L3.TokenPasswordControllerApi(api_client)
    request = TokenPasswordRequest(
        username="user@example.com",
        password="password123"
    )
    api_response = api_instance.login(request)
```

<div id="l3-token-refresh"></div>

#### Refresh Token (L3)

```python
import ods_sdk_L3
from ods_sdk_L3.models.token_refresh_request import TokenRefreshRequest

configuration = ods_sdk_L3.Configuration(host="http://localhost:8090")
with ods_sdk_L3.ApiClient(configuration) as api_client:
    api_instance = ods_sdk_L3.TokenRefreshControllerApi(api_client)
    request = TokenRefreshRequest(
        refresh_token="your-refresh-token"
    )
    api_response = api_instance.refresh(request)
```

<div id="l3-get-authz"></div>

#### Retrieve Authorization Model (L3)

```python
import ods_sdk_L3

configuration = ods_sdk_L3.Configuration(host="http://localhost:8090")
with ods_sdk_L3.ApiClient(configuration) as api_client:
    api_instance = ods_sdk_L3.AuthorizationControllerApi(api_client)
    api_response = api_instance.get_api(store_id="store-123")
```

<div id="pay-register-status"></div>

#### Register Data Exchange Status (Payment)

```python
import ods_sdk_payment
from ods_sdk_payment.models.data_exchange_status_request import DataExchangeStatusRequest

configuration = ods_sdk_payment.Configuration(host="http://localhost:8080")
with ods_sdk_payment.ApiClient(configuration) as api_client:
    api_instance = ods_sdk_payment.DefaultApi(api_client)
    request = DataExchangeStatusRequest(
        data_id_list=["data1", "data2"],
        status="COMPLETED"
    )
    api_response = api_instance.register_data_exchange_status_api_v1_data_exchange_status_post(
        user_agent="python-sdk",
        x_tracking_id="tracking-id",
        content_type="application/json",
        x_payment_api_key="your-api-key",
        data_exchange_status_request=request
    )
```

<div id="pay-list-fee"></div>

#### Retrieve Fee Model List (Payment)

```python
import ods_sdk_payment

configuration = ods_sdk_payment.Configuration(host="http://localhost:8080")
with ods_sdk_payment.ApiClient(configuration) as api_client:
    api_instance = ods_sdk_payment.DefaultApi(api_client)
    api_response = api_instance.list_fee_models_api_v1_fee_model_get(
        user_agent="python-sdk",
        x_tracking_id="tracking-id",
        x_payment_api_key="your-api-key"
    )
```

<div id="pay-create-fee"></div>

#### Register a Fee Model (Payment)

```python
import ods_sdk_payment
from ods_sdk_payment.models.fee_model_create_request import FeeModelCreateRequest

configuration = ods_sdk_payment.Configuration(host="http://localhost:8080")
with ods_sdk_payment.ApiClient(configuration) as api_client:
    api_instance = ods_sdk_payment.DefaultApi(api_client)
    request = FeeModelCreateRequest(
        fee_model_name="Standard Model",
        fee_rate=0.05
    )
    api_response = api_instance.create_fee_model_api_v1_fee_model_post(
        user_agent="python-sdk",
        x_tracking_id="tracking-id",
        content_type="application/json",
        x_payment_api_key="your-api-key",
        fee_model_create_request=request
    )
```

<div id="pay-check-eligibility"></div>

#### Check Transaction Eligibility (Payment)

```python
import ods_sdk_payment
from ods_sdk_payment.models.transaction_eligibility_request import TransactionEligibilityRequest

configuration = ods_sdk_payment.Configuration(host="http://localhost:8080")
with ods_sdk_payment.ApiClient(configuration) as api_client:
    api_instance = ods_sdk_payment.DefaultApi(api_client)
    request = TransactionEligibilityRequest(
        participant_id="participant-123",
        data_id_list=["data-001"]
    )
    api_response = api_instance.check_transaction_eligibility_api_v1_data_exchange_transaction_eligibility_post(
        user_agent="python-sdk",
        x_tracking_id="tracking-id",
        content_type="application/json",
        x_payment_api_key="your-api-key",
        transaction_eligibility_request=request
    )
```

<div id="pay-get-billing"></div>

#### Retrieve Billing Schedule (Payment)

```python
import ods_sdk_payment
from ods_sdk_payment.models.billing_schedule_request import BillingScheduleRequest

configuration = ods_sdk_payment.Configuration(host="http://localhost:8080")
with ods_sdk_payment.ApiClient(configuration) as api_client:
    api_instance = ods_sdk_payment.DefaultApi(api_client)
    request = BillingScheduleRequest(
        billing_month="2026-02"
    )
    api_response = api_instance.get_billing_schedule_api_v1_billing_post(
        user_agent="python-sdk",
        x_tracking_id="tracking-id",
        content_type="application/json",
        x_payment_api_key="your-api-key",
        billing_schedule_request=request
    )
```

<div id="pay-update-status"></div>

#### Update Data Exchange Status (Payment)

```python
import ods_sdk_payment
from ods_sdk_payment.models.data_exchange_status_request import DataExchangeStatusRequest

configuration = ods_sdk_payment.Configuration(host="http://localhost:8080")
with ods_sdk_payment.ApiClient(configuration) as api_client:
    api_instance = ods_sdk_payment.DefaultApi(api_client)
    request = DataExchangeStatusRequest(
        data_id_list=["data1"],
        status="FAILED"
    )
    api_response = api_instance.update_data_exchange_status_api_v1_data_exchange_status_put(
        user_agent="python-sdk",
        x_tracking_id="tracking-id",
        content_type="application/json",
        x_payment_api_key="your-api-key",
        data_exchange_status_request=request
    )
```

<div id="pay-update-fee"></div>

#### Update a Fee Model (Payment)

```python
import ods_sdk_payment
from ods_sdk_payment.models.fee_model_update_request import FeeModelUpdateRequest

configuration = ods_sdk_payment.Configuration(host="http://localhost:8080")
with ods_sdk_payment.ApiClient(configuration) as api_client:
    api_instance = ods_sdk_payment.DefaultApi(api_client)
    request = FeeModelUpdateRequest(
        fee_model_name="Updated Model",
        fee_rate=0.07
    )
    api_response = api_instance.update_fee_model_api_v1_fee_model_fee_model_id_put(
        fee_model_id="fee-123",
        user_agent="python-sdk",
        x_tracking_id="tracking-id",
        content_type="application/json",
        x_payment_api_key="your-api-key",
        fee_model_update_request=request
    )
```

<div id="pay-delete-fee"></div>

#### Delete a Fee Model (Payment)

```python
import ods_sdk_payment

configuration = ods_sdk_payment.Configuration(host="http://localhost:8080")
with ods_sdk_payment.ApiClient(configuration) as api_client:
    api_instance = ods_sdk_payment.DefaultApi(api_client)
    api_response = api_instance.delete_fee_model_api_v1_fee_model_fee_model_id_delete(
        fee_model_id="fee-123",
        user_agent="python-sdk",
        x_tracking_id="tracking-id",
        content_type="application/json",
        x_payment_api_key="your-api-key"
    )
```

<div id="pay-check-eligibility-non-fee"></div>

#### Check Transaction Eligibility (No Fee Model) (Payment)

```python
import ods_sdk_payment
from ods_sdk_payment.models.transaction_eligibility_non_fee_model_request import TransactionEligibilityNonFeeModelRequest

configuration = ods_sdk_payment.Configuration(host="http://localhost:8080")
with ods_sdk_payment.ApiClient(configuration) as api_client:
    api_instance = ods_sdk_payment.DefaultApi(api_client)
    request = TransactionEligibilityNonFeeModelRequest(
        participant_id="participant-123",
        data_id_list=["data-001"]
    )
    api_response = api_instance.check_transaction_eligibility_non_fee_model_api_v1_data_exchange_non_fee_model_transaction_eligibility_post(
        user_agent="python-sdk",
        x_tracking_id="tracking-id",
        content_type="application/json",
        x_payment_api_key="your-api-key",
        transaction_eligibility_non_fee_model_request=request
    )
```

<div id="pay-confirm-non-fee"></div>

#### Confirm Transaction Amount (No Fee Model) (Payment)

```python
import ods_sdk_payment
from ods_sdk_payment.models.data_exchange_non_fee_model_request import DataExchangeNonFeeModelRequest

configuration = ods_sdk_payment.Configuration(host="http://localhost:8080")
with ods_sdk_payment.ApiClient(configuration) as api_client:
    api_instance = ods_sdk_payment.DefaultApi(api_client)
    request = DataExchangeNonFeeModelRequest(
        data_id_list=["data-001"],
        price=1000
    )
    api_response = api_instance.confirm_data_exchange_api_v1_data_exchange_non_fee_model_confirm_post(
        user_agent="python-sdk",
        x_tracking_id="tracking-id",
        content_type="application/json",
        x_payment_api_key="your-api-key",
        data_exchange_non_fee_model_request=request
    )
```

<div id="pay-get-payment"></div>

#### Retrieve Payment Schedule (Payment)

```python
import ods_sdk_payment
from ods_sdk_payment.models.payment_schedule_request import PaymentScheduleRequest

configuration = ods_sdk_payment.Configuration(host="http://localhost:8080")
with ods_sdk_payment.ApiClient(configuration) as api_client:
    api_instance = ods_sdk_payment.DefaultApi(api_client)
    request = PaymentScheduleRequest(
        payment_month="2026-02"
    )
    api_response = api_instance.get_payment_schedule_api_v1_payment_post(
        user_agent="python-sdk",
        x_tracking_id="tracking-id",
        content_type="application/json",
        x_payment_api_key="your-api-key",
        payment_schedule_request=request
    )
```

## Step 6 — Run the Sample Application

The `sample-app` directory contains sample code that uses each SDK.

### How to Run

1. **Prepare a virtual environment**:
   Create and activate a virtual environment by following Step 4.

2. **Install the SDKs and dependencies**:
   ```bash
   # Install the SDKs (same as Step 4)
   pip install ./generated/l3
   pip install ./generated/payment

   # Install libraries required by each SDK
   pip install -r generated/l3/requirements.txt
   pip install -r generated/payment/requirements.txt
   ```

3. **Run the samples**:
   Move to the `sample-app` directory and run the desired sample.
   ```bash
   cd sample-app
   python auth_samples.py
   ```

### Sample Structure

- `config.py`:  Common configuration such as API host and authentication.
- `auth_samples.py`: Authentication-related samples (token acquisition, URL generation).
- `account_samples.py`: Account management (operators, plants, users).
- `data_exchange_samples.py`: Data exchange and fee models.
- `authz_samples.py`: Authorization and API key verification.
- `token_samples.py`: Token management (refresh, introspection).
- `misc_samples.py`: Miscellaneous samples (client management, password changes).

Note: API call sections within each sample are commented out. Please adjust them according to your actual server environment.

## Endpoint List

### L3 (apidoc/L3/api-docs.yaml)

| Path | HTTP Method | operationId |
|---|---:|---|
| /auth/password/{operator_id} | PUT | changePassword |
| /account/operator/{operator_id} | GET | getOperator |
| /account/operator/{operator_id} | PUT | putOperator |
| /account/operator/status/{operator_id} | PUT | putOperatorStatus |
| /account/operator/plant/{plant_id} | GET | getPlant |
| /account/operator/plant/{plant_id} | PUT | putPlant |
| /account/operator/plant/status/{plant_id} | PUT | putPlantStatus |
| /authz/stores/{store_id}/access/v1/evaluation | POST | postApi |
| /authz/stores/{store_id}/authorization-models | GET | getApi |
| /authz/stores/{store_id}/authorization-models | POST | createAuthorizationModel |
| /authz/stores/{store_id}/write | POST | writeAuthorization |
| /authz/stores/{store_id}/read | POST | readAuthorization |
| /auth/url | POST | url |
| /auth/token | POST | accessToken |
| /auth/token/refresh | POST | refresh |
| /auth/token/password | POST | login |
| /auth/token/introspect | POST | tokenIntrospection |
| /auth/token/client | POST | client |
| /auth/password/url | POST | authPasswordUrl |
| /auth/clients | POST | postClients |
| /auth/clients/secret/{client_uuid} | POST | getClientSecret |
| /auth/apikey/verify | POST | verifyAPIKey |
| /account/user | POST | postUser |
| /account/operator | POST | postOperator |
| /account/operator/plant | POST | postPlant |
| /account/operator/plant/list | POST | listPlant |
| /account/operator/list | POST | listOperator |

### Payment (apidoc/payment/openapi.json)

| Path | HTTP Method | operationId |
|---|---:|---|
| /api/v1/fee-model | POST | create_fee_model_api_v1_fee_model_post |
| /api/v1/fee-model | GET | list_fee_models_api_v1_fee_model_get |
| /api/v1/fee-model/{fee_model_id} | GET | get_fee_model_api_v1_fee_model__fee_model_id__get |
| /api/v1/fee-model/{fee_model_id} | PUT | update_fee_model_api_v1_fee_model__fee_model_id__put |
| /api/v1/fee-model/{fee_model_id} | DELETE | delete_fee_model_api_v1_fee_model__fee_model_id__delete |
| /api/v1/data-exchange/transaction/eligibility | POST | check_transaction_eligibility_api_v1_data_exchange_transaction_eligibility_post |
| /api/v1/data-exchange/status | POST | register_data_exchange_status_api_v1_data_exchange_status_post |
| /api/v1/data-exchange/status | PUT | update_data_exchange_status_api_v1_data_exchange_status_put |
| /api/v1/data-exchange/non-fee-model/transaction/eligibility | POST | check_transaction_eligibility_non_fee_model_api_v1_data_exchange_non_fee_model_transaction_eligibility_post |
| /api/v1/data-exchange/non-fee-model/confirm | POST | confirm_data_exchange_api_v1_data_exchange_non_fee_model_confirm_post |
| /api/v1/payment | POST | get_payment_schedule_api_v1_payment_post |
| /api/v1/billing | POST | get_billing_schedule_api_v1_billing_post |

## License

- This repository is provided under the MIT License.
- The copyright of the source code and related documentation belongs to NTT DATA Group Corporation and NTT DATA Corporation.

## Disclaimer

- The contents of this repository may be changed or removed without prior notice.
- The authors and maintainers assume no responsibility whatsoever for any losses or damages arising from the use of this repository.
