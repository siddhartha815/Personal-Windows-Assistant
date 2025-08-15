import requests

def cryptocurrency(crypto_api):
    response = requests.get(crypto_api)
    crypto_json = response.json()
    print(">",crypto_json["USD"],"USD")
    return crypto_json