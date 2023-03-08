import requests
from requests_folder.get_token import *

def get_all_orders():
    token = generate_token()
    header_params = {'Authorization': token}
    r=requests.get('https://simple-books-api.glitch.me/orders', headers=header_params)
    return r