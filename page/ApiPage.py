import requests
from pytest_ui_api_template.config import baseUrl, api_key, HEADERS

class ApiClient:
    def __init__(self):
        self.base_url = baseUrl
        self.headers = {"X-API-KEY": api_key} if api_key else {}

    def test_name_cyrillic(self):
        self.response = requests.get(baseUrl + '?page=1&limit=10&query=%D1%82%D1%80%D0%B8%D0%B3%D0%B3%D0%B5%D1%80', headers=HEADERS)
        assert self.response.status_code == 200
        assert self.response.json()["docs"][0]["name"] == "Триггер"

    def test_name_register(self):
        self.response = requests.get(baseUrl + '?page=1&limit=10&query=%D0%A2%D0%A0%D0%98%D0%93%D0%93%D0%95%D0%A0', headers=HEADERS)
        assert self.response.status_code == 200
        assert self.response.json()["docs"][0]["name"] == "Триггер"

    def test_zero(self):
        self.response = requests.get(baseUrl + 'page=0&limit=250&query=%D1%82%D1%80%D0%B8%D0%B3%D0%B3%D0%B5%D1%80', headers=HEADERS)
        assert self.response.status_code == 400

    def test_metod_post(self):
        self.body = {
            "collection": {
                "info": {
                    "name": "{{collectionName}}",
                    "schema": "{{collectionSchemaUrl}}"
                },
                "item": [
                    {
                        "request": {}
                    }
                ]
            }
        }
        self.response = requests.post(baseUrl + '?page=1&limit=10&query=%D1%82%D1%80%D0%B8%D0%B3%D0%B3%D0%B5%D1%80', headers=HEADERS)
        assert self.response.status_code == 200
        assert self.response.json()["docs"][0]["name"] == "Триггер"

    def test_element(self):
        self.response = requests.get(baseUrl + 'page=0&limit=251&query=%D1%82%D1%80%D0%B8%D0%B3%D0%B3%D0%B5%D1%80', headers=HEADERS)
        assert self.response.status_code == 400

