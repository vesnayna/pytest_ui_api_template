import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MainPage:
    """
    Конструкция класса MainePage.

    :param driver: Webdriver - объект драйвера Selenium.
    """

    def __init__(self, driver: WebDriver):
        self.url = "https://www.kinopoisk.ru/"
        self.driver = driver
        self.driver.get(self.url)

    @allure.step("Поиск фильма на кириллице")
    def test_name_cyrillic(self):
        """
        Поиск фильма по названию на кириллице (к примеру "Триггер")
        """

        search_input = WebDriverWait(self.driver, 50).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[name='kp_query']")))
        search_input.send_keys('Триггер')
        self.driver.find_element(By.CSS_SELECTOR, "[type='submit']").send_keys()
        print('Триггер')


    @allure.step("Ввод в поле поиска спецсимволов (! ?)")
    def test_symbol(self):
        """
        Ввод в поле поиска спецсимволов (! ?)
        """

        search_input = WebDriverWait(self.driver, 50).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "[name='kp_query']")))
        search_input.send_keys('!?')
        self.driver.find_element(By.CSS_SELECTOR, "[type='submit']").send_keys()
        print('! ?')

    @allure.step("Ввод в поле поиска только цифр")
    def test_number(self):
        """
        Ввод в поле поиска только цифр
        """

        search_input = WebDriverWait(self.driver, 50).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "[name='kp_query']")))
        search_input.send_keys('123')
        self.driver.find_element(By.CSS_SELECTOR, "[type='submit']").send_keys()
        print('123')

    @allure.step("Поиск фильма на латинице")
    def test_name_latin(self):
        """
        Поиск фильма по названию на латинице (к примеру "Fair Game")
        """

        search_input = WebDriverWait(self.driver, 50).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "[name='kp_query']")))
        search_input.send_keys('Fair Game')
        self.driver.find_element(By.CSS_SELECTOR, "[type='submit']").send_keys()
        print('Fair Game')

    @allure.step("Поиск фильма с дефисом между словами")
    def test_name_dash(self):
        """
        Поиск фильма с дефисом между словами (к примеру "Сынуля-чистюля")
        """

        self.driver.find_element(By.CSS_SELECTOR, "[class='sign-in__close']").send_keys()
        search_input = WebDriverWait(self.driver, 50).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "[name='kp_query']")))
        search_input.send_keys('Сынуля-чистюля')
        self.driver.find_element(By.CSS_SELECTOR, "[type='submit']").send_keys()
        print('Сынуля-чистюля')

    def close_driver(self):
        """
        Функция закрытия браузера
        """

        self.driver.quit()