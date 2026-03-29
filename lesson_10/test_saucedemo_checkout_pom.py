"""
Тесты для проверки оформления заказа в интернет-магазине SauceDemo.
"""
import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from pages.saucedemo_pages import (
    LoginPage,
    ProductsPage,
    CartPage,
    CheckoutStepOnePage,
    CheckoutStepTwoPage
)
import allure

BASE_URL = "https://www.saucedemo.com/"
USERNAME = "standard_user"
PASSWORD = "secret_sauce"
FIRST_NAME = "Иван"
LAST_NAME = "Петров"
POSTAL_CODE = "12345"
EXPECTED_TOTAL_PRICE = "$58.29"


class TestSauceDemoCheckout:
    """
    Тестовый класс для проверки сценария оформления заказа.
    """
    @pytest.fixture
    def driver(self):
        """
        Фикстура для инициализации и закрытия драйвера Firefox.
        Returns:
            WebDriver: Экземпляр драйвера Firefox
        """
        service = FirefoxService(GeckoDriverManager().install())
        firefox_driver = webdriver.Firefox(service=service)
        firefox_driver.maximize_window()
        yield firefox_driver
        firefox_driver.quit()

    @allure.feature("Оформление заказа")
    @allure.story("Проверка итоговой суммы заказа")
    @allure.title("Проверка корректности итоговой суммы при оформлении заказа")
    @allure.description("""
        Тест проверяет сценарий оформления заказа:
        1. Авторизация на сайте
        2. Добавление трех товаров в корзину
        3. Переход в корзину и оформление заказа
        4. Заполнение информации о пользователе
        5. Проверка итоговой суммы заказа
    """)
    @allure.severity(allure.severity_level.CRITICAL)
    def test_verify_checkout_total_price_pom(self, driver):
        """
        Тест проверяет корректность итоговой суммы при оформлении заказа.
        Args:
            driver: WebDriver экземпляр из фикстуры
        Returns:
            None
        """
        with allure.step("Создать экземпляр страницы авторизации"):
            login_page = LoginPage(driver, BASE_URL)
        with allure.step("Выполнить авторизацию"):
            products_page = login_page.open().login(USERNAME, PASSWORD)
        with allure.step("Добавить товары в корзину"):
            products_page.add_item_to_cart("sauce-labs-backpack") \
                        .add_item_to_cart("sauce-labs-bolt-t-shirt") \
                        .add_item_to_cart("sauce-labs-onesie")
        with allure.step("Перейти в корзину"):
            cart_page = products_page.go_to_cart()
        with allure.step("Начать оформление заказа"):
            checkout_one_page = cart_page.click_checkout()
        with allure.step("Заполнить информацию о пользователе"):
            checkout_two_page = checkout_one_page.fill_user_info(
                FIRST_NAME, LAST_NAME, POSTAL_CODE
            ).click_continue()
        with allure.step("Получить итоговую сумму заказа"):
            actual_total_price = checkout_two_page.get_total_price()
        with allure.step("Проверить соответствие итоговой суммы"):
            assert actual_total_price == EXPECTED_TOTAL_PRICE, (
                f"Ожидаемая итоговая сумма: {EXPECTED_TOTAL_PRICE}, "
                f"Фактическая: {actual_total_price}"
            )
        with allure.step("Логирование успешного завершения теста"):
            allure.attach(
                f"Итоговая сумма '{actual_total_price}' соответствует ожидаемой",
                name="Результат проверки",
                attachment_type=allure.attachment_type.TEXT
            )
