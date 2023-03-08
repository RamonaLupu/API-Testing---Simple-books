from requests_folder.update_an_order import update_an_order

class TestUpdateAnOrder:
    def test_update_an_order(self):
        r=update_an_order('ramo')
        assert r.status_code == 204, f'Error: status code is not correct. Expected: 204, Actual: {r.status_code}'
