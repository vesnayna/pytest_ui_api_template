import pytest
import requests
from pytest_ui_api_template.page.ApiPage import ApiClient
from pytest_ui_api_template.config import *

@pytest.fixture
def client():
    return ApiClient()

def test_name_cyrillic(client):
    api_page = ApiClient()
    api_page.test_name_cyrillic()

def test_name_register(client):
    api_page = ApiClient()
    api_page.test_name_register()

def test_zero(client):
    api_page = ApiClient()
    api_page.test_zero()

def test_metod_post(client):
    api_page = ApiClient()
    api_page.test_metod_post()

def test_element(client):
    api_page = ApiClient()
    api_page.test_element()












