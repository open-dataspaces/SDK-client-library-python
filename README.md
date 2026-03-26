# open-data-spaces-sdk-client-library-python

ODS SDK for Onboarding - Python client library

## 概要

このリポジトリには、`apidoc` フォルダにある OpenAPI 仕様書から Python SDK を生成するための手順と成果物が含まれています。
現在は、L3（アイデンティティコンポーネント）と Payment（精算・決済サービス）の2つの仕様書から個別の SDK を生成する構成になっています。

## 前提条件

- Python 3.9 以上がインストールされていること。
- `npm` が利用可能であること（OpenAPI Generator CLI の実行に使用）。
- リポジトリ内に以下の OpenAPI 仕様書が存在すること。

  - `apidoc/L3/api-docs.yaml`
  - `apidoc/L3/config.yaml` (生成設定)
  - `apidoc/payment/openapi.json`
  - `apidoc/payment/config.yaml` (生成設定)

## SDK 生成手順

### Step 1 — OpenAPI Generator CLI を入手

OpenAPI Generator は `npm` でインストールされていることを前提としています。以下のコマンドでバージョンを確認できます。

```bash
npx @openapitools/openapi-generator-cli version
```

もしインストールされていない場合は、以下のコマンドでインストールできます。

```bash
npm install -g @openapitools/openapi-generator-cli
```

### Step 2 — 仕様の検証

```bash
npx @openapitools/openapi-generator-cli validate -i apidoc/L3/api-docs.yaml
npx @openapitools/openapi-generator-cli validate -i apidoc/payment/openapi.json
```

検証でエラーが出た場合は生成前に修正してください。

### Step 3 — Python SDK の生成

以下のコマンドを実行して、それぞれの Python クライアントを生成します。

**注意:** プロキシ環境下などで証明書エラー（`unable to get local issuer certificate`）が発生する場合は、環境変数 `NODE_TLS_REJECT_UNAUTHORIZED=0` を設定して実行してください。

#### L3 SDK の生成

```bash
npx @openapitools/openapi-generator-cli generate -i apidoc/L3/api-docs.yaml -g python -o generated/l3 -c apidoc/L3/config.yaml
```

#### Payment SDK の生成

```bash
npx @openapitools/openapi-generator-cli generate -i apidoc/payment/openapi.json -g python -o generated/payment -c apidoc/payment/config.yaml
```

### Step 4 — 生成した SDK のインストール

生成された SDK を仮想環境（venv）にインストールします。

#### 仮想環境の作成と有効化

```bash
# 仮想環境の作成
python3 -m venv .venv

# 仮想環境の有効化 (Windows)
.venv\Scripts\activate

# 仮想環境の有効化 (Linux/macOS)
source .venv/bin/activate
```

#### SDK のインストール

```bash
# L3 SDK のインストール
cd generated/l3
pip install .
cd -

# Payment SDK のインストール
cd generated/payment
pip install .
cd -
```

### Step 5 — 利用例

生成されたクライアントの使用例です（仮想環境が有効であることを前提としています）。

#### L3 SDK の利用

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

#### Payment SDK の利用

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

#### L3 SDK 一覧

| ユースケース | クラス名 | メソッド名 | 実装例 |
| :--- | :--- | :--- | :--- |
| アクセストークンの取得 | `AuthTokenControllerApi` | `access_token` | [詳細](#l3-access-token) |
| 認証URLの取得 | `AuthUrlControllerApi` | `url` | [詳細](#l3-auth-url) |
| API キーの検証 | `ApiKeyControllerApi` | `verify_api_key` | [詳細](#l3-verify-api-key) |
| クライアントの登録 | `ClientsControllerApi` | `post_clients` | [詳細](#l3-post-clients) |
| クライアントシークレットの取得 | `ClientsControllerApi` | `get_client_secret` | [詳細](#l3-get-client-secret) |
| オペレーターの一覧取得 | `OperatorControllerApi` | `list_operator` | [詳細](#l3-list-operator) |
| オペレーターの登録 | `OperatorControllerApi` | `post_operator` | [詳細](#l3-post-operator) |
| パスワード変更 | `PasswordControllerApi` | `change_password` | [詳細](#l3-change-password) |
| パスワード変更URLの取得 | `PasswordUrlControllerApi` | `url1` | [詳細](#l3-password-url) |
| 拠点の取得 | `PlantControllerApi` | `get_plant` | [詳細](#l3-get-plant) |
| 拠点の登録 | `PlantControllerApi` | `post_plant` | [詳細](#l3-post-plant) |
| クライアント認証によるトークン取得 | `TokenClientControllerApi` | `client` | [詳細](#l3-token-client) |
| トークンのイントロスペクション | `TokenIntrospectionControllerApi` | `token_introspection` | [詳細](#l3-token-introspect) |
| パスワード認証によるトークン取得 | `TokenPasswordControllerApi` | `login` | [詳細](#l3-token-password) |
| トークンのリフレッシュ | `TokenRefreshControllerApi` | `refresh` | [詳細](#l3-token-refresh) |
| ユーザーの登録 | `UserControllerApi` | `post_user` | [詳細](#l3-post-user) |
| 認可モデルの取得 | `AuthorizationControllerApi` | `get_api` | [詳細](#l3-get-authz) |

#### Payment SDK 一覧

| ユースケース | クラス名 | メソッド名 | 実装例 |
| :--- | :--- | :--- | :--- |
| データ交換状態の登録 | `DefaultApi` | `register_data_exchange_status_api_v1_data_exchange_status_post` | [詳細](#pay-register-status) |
| データ交換状態の更新 | `DefaultApi` | `update_data_exchange_status_api_v1_data_exchange_status_put` | [詳細](#pay-update-status) |
| 手数料モデルの一覧取得 | `DefaultApi` | `list_fee_models_api_v1_fee_model_get` | [詳細](#pay-list-fee) |
| 手数料モデルの登録 | `DefaultApi` | `create_fee_model_api_v1_fee_model_post` | [詳細](#pay-create-fee) |
| 手数料モデルの変更 | `DefaultApi` | `update_fee_model_api_v1_fee_model_fee_model_id_put` | [詳細](#pay-update-fee) |
| 手数料モデルの削除 | `DefaultApi` | `delete_fee_model_api_v1_fee_model_fee_model_id_delete` | [詳細](#pay-delete-fee) |
| 取引資格の確認 | `DefaultApi` | `check_transaction_eligibility_api_v1_data_exchange_transaction_eligibility_post` | [詳細](#pay-check-eligibility) |
| 取引資格の確認 (利用料モデル無) | `DefaultApi` | `check_transaction_eligibility_non_fee_model_api_v1_data_exchange_non_fee_model_transaction_eligibility_post` | [詳細](#pay-check-eligibility-non-fee) |
| 取引金額確定 (利用料モデル無) | `DefaultApi` | `confirm_data_exchange_api_v1_data_exchange_non_fee_model_confirm_post` | [詳細](#pay-confirm-non-fee) |
| 請求予定額の取得 | `DefaultApi` | `get_billing_schedule_api_v1_billing_post` | [詳細](#pay-get-billing) |
| 支払予定額の取得 | `DefaultApi` | `get_payment_schedule_api_v1_payment_post` | [詳細](#pay-get-payment) |

---

<div id="l3-access-token"></div>

#### アクセストークンの取得 (L3)

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

#### クライアントの登録 (L3)

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

#### API キーの検証 (L3)

```python
import ods_sdk_L3

configuration = ods_sdk_L3.Configuration(host="http://localhost:8090")
with ods_sdk_L3.ApiClient(configuration) as api_client:
    api_instance = ods_sdk_L3.ApiKeyControllerApi(api_client)
    api_key = "your_api_key_here"
    api_response = api_instance.verify_api_key(api_key=api_key)
```

<div id="l3-list-operator"></div>

#### オペレーターの一覧取得 (L3)

```python
import ods_sdk_L3

configuration = ods_sdk_L3.Configuration(host="http://localhost:8090")
with ods_sdk_L3.ApiClient(configuration) as api_client:
    api_instance = ods_sdk_L3.OperatorControllerApi(api_client)
    api_response = api_instance.list_operator()
```

<div id="l3-post-user"></div>

#### ユーザーの登録 (L3)

```python
import ods_sdk_L3

configuration = ods_sdk_L3.Configuration(host="http://localhost:8090")
with ods_sdk_L3.ApiClient(configuration) as api_client:
    api_instance = ods_sdk_L3.UserControllerApi(api_client)
    user_id = "sample_user_id"
    api_response = api_instance.post_user(body=user_id)
```

<div id="l3-auth-url"></div>

#### 認証URLの取得 (L3)

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

#### クライアントシークレットの取得 (L3)

```python
import ods_sdk_L3

configuration = ods_sdk_L3.Configuration(host="http://localhost:8090")
with ods_sdk_L3.ApiClient(configuration) as api_client:
    api_instance = ods_sdk_L3.ClientsControllerApi(api_client)
    client_uuid = "client-uuid-123"
    api_response = api_instance.get_client_secret(client_uuid)
```

<div id="l3-post-operator"></div>

#### オペレーターの登録 (L3)

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

#### パスワード変更 (L3)

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

#### パスワード変更URLの取得 (L3)

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

#### 拠点の取得 (L3)

```python
import ods_sdk_L3

configuration = ods_sdk_L3.Configuration(host="http://localhost:8090")
with ods_sdk_L3.ApiClient(configuration) as api_client:
    api_instance = ods_sdk_L3.PlantControllerApi(api_client)
    api_response = api_instance.get_plant(plant_id="plant-123")
```

<div id="l3-post-plant"></div>

#### 拠点の登録 (L3)

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

#### クライアント認証によるトークン取得 (L3)

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

#### トークンのイントロスペクション (L3)

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

#### パスワード認証によるトークン取得 (L3)

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

#### トークンのリフレッシュ (L3)

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

#### 認可モデルの取得 (L3)

```python
import ods_sdk_L3

configuration = ods_sdk_L3.Configuration(host="http://localhost:8090")
with ods_sdk_L3.ApiClient(configuration) as api_client:
    api_instance = ods_sdk_L3.AuthorizationControllerApi(api_client)
    api_response = api_instance.get_api(store_id="store-123")
```

<div id="pay-register-status"></div>

#### データ交換ステータスの登録 (Payment)

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

#### 手数料モデルの一覧取得 (Payment)

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

#### 手数料モデルの登録 (Payment)

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

#### 取引資格の確認 (Payment)

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

#### 請求スケジュールの取得 (Payment)

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

#### データ交換状態の更新 (Payment)

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

#### 手数料モデルの変更 (Payment)

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

#### 手数料モデルの削除 (Payment)

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

#### 取引資格の確認 (利用料モデル無) (Payment)

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

#### 取引金額確定 (利用料モデル無) (Payment)

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

#### 支払予定額の取得 (Payment)

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

## Step 6 — サンプルアプリの実行

`sample-app` ディレクトリには、それぞれの SDK を使用したサンプルコードが格納されています。

### 実行方法

1. **仮想環境の準備**:
   Step 4 に従って仮想環境を作成し、有効化してください。

2. **SDK と依存関係のインストール**:
   ```bash
   # SDK のインストール (Step 4 と同じ)
   pip install ./generated/l3
   pip install ./generated/payment

   # 各 SDK が依存するライブラリのインストール
   pip install -r generated/l3/requirements.txt
   pip install -r generated/payment/requirements.txt
   ```

3. **サンプルの実行**:
   `sample-app` ディレクトリに移動して、目的のサンプルを実行します。
   ```bash
   cd sample-app
   python auth_samples.py
   ```

### サンプル構成

- `config.py`: API ホストや認証などの共通設定。
- `auth_samples.py`: 認証関連（トークン取得、URL 生成）。
- `account_samples.py`: アカウント管理（オペレーター、プラント、ユーザー）。
- `data_exchange_samples.py`: データ交換、利用料モデル。
- `authz_samples.py`: 認可、API キー検証。
- `token_samples.py`: トークン管理（リフレッシュ、イントロスペクト）。
- `misc_samples.py`: その他（クライアント管理、パスワード変更）。

※ 各サンプル内の API 呼び出し部分はコメントアウトされています。実際のサーバー環境に合わせて調整してください。

## エンドポイント一覧

### L3 (apidoc/L3/api-docs.yaml)

| Path | HTTP メソッド | operationId |
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

| Path | HTTP メソッド | operationId |
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

## ライセンス

- 本リポジトリはMITライセンスで提供されています。
- ソースコードおよび関連ドキュメントの著作権は株式会社NTTデータグループ、株式会社NTTデータに帰属します。

## 免責事項

- 本リポジトリの内容は予告なく変更・削除する可能性があります。
- 本リポジトリの利用により生じた損失及び損害等について、いかなる責任も負わないものとします。
