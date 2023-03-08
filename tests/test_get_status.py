from requests_folder.get_status import get_status

class TestGetStatus:
    def test_get_status_books(self):
        r = get_status()
        assert r.status_code == 200, f'Status is NOK'
        assert r.json()["status"] == "OK", f'Error'
