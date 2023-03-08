from requests_folder.delete_an_order import delete_an_order

class TestDeleteAnOrder:
    def test_delete_an_order(self):
        r=delete_an_order()
        assert r.status_code == 204, f'Error: status code is not correct. Expected: 204, Actual: {r.status_code}'
        assert r.json()["error"] == "No order with id :orderId.", f"Error: is incorrect. Actual {r.json()['error']}"