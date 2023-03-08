from requests_folder.get_single_book_params import get_single_book_params


class TestGetSingleBookParams:
    def test_get_single_book_params_valid_id(self):
        r=get_single_book_params(2)
        assert r.status_code == 200, f'Error: status code is not correct. Expected: 200, Actual: {r.status_code}'

    def test_get_single_book_params_invalid_id(self):
        r=get_single_book_params(21)
        assert r.status_code == 404, f'Error: status code is not correct. Expected: 404, Actual: {r.status_code}'
        assert r.json()["error"] == "No book with id 21", f"Error: is incorrect. Actual {r.json()['error']}"