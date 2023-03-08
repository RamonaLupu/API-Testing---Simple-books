import requests

def get_single_book_params(book_id):
    params = {'bookId': book_id}
    r = requests.get('https://simple-books-api.glitch.me/books/:bookId', params=params)
    return r