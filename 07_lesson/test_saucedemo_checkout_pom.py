

import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from pages.saucedemo_pages import (LoginPage,
    ProductsPage, 
    CartPage,
    CheckoutStepOnePage, 
    CheckoutStepTwoPage
)

BASE_URL = "https://www.saucedemo.com/"
USERNAME = "standard_user"
PASSWORD = "secret_sauce"
FIRST_NAME = "Иван"
LAST_NAME = "Петров"
POSTAL_CODE = "12345"
EXPECTED_TOTAL_PRICE = "$58.29"

class TestSauceDemoCheckout:
    @pytest.fixture
    def driver(self):
        service = FirefoxService(GeckoDriverManager().install())
        firefox_driver = webdriver.Firefox(service=service)
        firefox_driver.maximize_window()
        yield firefox_driver
        firefox_driver.quit()

    def test_verify_checkout_total_price_pom(self, driver):

        login_page = LoginPage(driver, BASE_URL)
        
        products_page = login_page.open().login(USERNAME, PASSWORD)
        
        products_page.add_item_to_cart("sauce-labs-backpack") \
                     .add_item_to_cart("sauce-labs-bolt-t-shirt") \
                     .add_item_to_cart("sauce-labs-onesie")
        
        cart_page = products_page.go_to_cart()
        
        checkout_one_page = cart_page.click_checkout()
        
        checkout_two_page = checkout_one_page.fill_user_info(
            FIRST_NAME, LAST_NAME, POSTAL_CODE
        ).click_continue()
        
        actual_total_price = checkout_two_page.get_total_price()
        
        assert actual_total_price == EXPECTED_TOTAL_PRICE, (
            f"Ожидаемая итоговая сумма: {EXPECTED_TOTAL_PRICE}, "
            f"Фактическая: {actual_total_price}"
        )
        
        print(f"Тест пройден успешно! Итоговая сумма '{actual_total_price}' "
              f"соответствует ожидаемой.")