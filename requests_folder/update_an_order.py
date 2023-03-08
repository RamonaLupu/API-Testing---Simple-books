import requests
from requests_folder.get_token import generate_token
from requests_folder.get_order_id import get_order_id

def update_an_order(customer_name):
    request_body = {"customerName": customer_name}
    orderId = get_order_id()
    token = generate_token()
    header_params = {'Authorization': token}
    r = requests.patch(f'https://simple-books-api.glitch.me/orders/?orderId={orderId}',json=request_body, headers=header_params)
    return r