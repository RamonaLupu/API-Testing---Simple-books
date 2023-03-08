from requests_folder.get_all_orders import get_all_orders

class TestAllOrders:
    def test_get_all_orders(self):
        r=get_all_orders()
        assert r.status_code == 200, f'Error: status code is not correct. Expected: 200, Actual: {r.status_code}'