import requests
from requests_folder.get_token import generate_token
from requests_folder.get_order_id import get_order_id

def get_an_order():
    orderId = get_order_id()
    token = generate_token()
    header_params = {'Authorization': token}
    r = requests.get(f'https://simple-books-api.glitch.me/orders/?orderId={orderId}', headers=header_params)
    return r