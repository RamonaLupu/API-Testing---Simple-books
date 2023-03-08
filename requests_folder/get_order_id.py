import requests
from requests_folder.get_token import *


def get_order_id():
    request_body = {
            "bookId": 3,
            "customerName": 'Jhon'
        }
    token = generate_token()
    header_params = {'Authorization': token}
    r = requests.post('https://simple-books-api.glitch.me/orders', json=request_body, headers=header_params)
    order_id = r.json()["orderId"]
    return order_id