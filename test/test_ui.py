import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pytest_ui_api_template.page.MainPage import MainPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pytest_ui_api_template.config import ui_url

@pytest.fixture
def driver():
    """
    Фикстура для инициализации и завершения работы драйвера
    """

    with allure.step("Инициализация браузера Chrome"):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    with allure.step("Увеличить окно браузера"):
        driver.maximize_window()
    with allure.step("Зайти на сайт"):
        driver.get("https://www.kinopoisk.ru/")
    with allure.step("Ожидание"):
        driver.implicitly_wait(10)
    with allure.step("Передача драйвера тесту"):
        yield driver
        driver.quit()


@allure.feature("Smoke")
@allure.story("UI")
@allure.title("Поиск фильма по названию на кириллице")
@allure.severity("CRITICAL")

def test_name_cyrillic(driver):
    main_page = MainPage(driver)
    main_page.test_name_cyrillic()
    main_page.close_driver()

@allure.feature("functional")
@allure.story("UI")
@allure.title("Ввод в поле поиска спецсимволов (! ?)")
@allure.severity("CRITICAL")

def test_symbol(driver):
        main_page = MainPage(driver)
        main_page.test_symbol()
        main_page.close_driver()

@allure.feature("functional")
@allure.story("UI")
@allure.title("Ввод в поле поиска только цифр")
@allure.severity("CRITICAL")

def test_number(driver):
    main_page = MainPage(driver)
    main_page.test_number()
    main_page.close_driver()

@allure.feature("Smoke")
@allure.story("UI")
@allure.title("Поиск фильмов по названию на латинице")
@allure.severity("CRITICAL")

def test_name_latin(driver):
    main_page = MainPage(driver)
    main_page.test_name_latin()
    main_page.close_driver()

@allure.feature("Smoke")
@allure.story("UI")
@allure.title("Поиск фильма с дефисом между словами")
@allure.severity("CRITICAL")

def test_name_dash(driver):
    main_page = MainPage(driver)
    main_page.test_name_dash()
    main_page.close_driver()


