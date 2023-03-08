from requests_folder.get_an_order import get_an_order

class TestAnOrder:
    def test_get_an_order(self):
        r=get_an_order()
        assert r.status_code == 200, f'Error: status code is not correct. Expected: 200, Actual: {r.status_code}'
