# Configuration設定
def get_l3_configuration():
    import ods_sdk_L3
    return ods_sdk_L3.Configuration(
        host="http://localhost:8090"
    )

def get_payment_configuration():
    import ods_sdk_payment
    return ods_sdk_payment.Configuration(
        host="http://localhost:8080"
    )
