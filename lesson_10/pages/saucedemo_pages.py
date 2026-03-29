"""
Модуль содержит Page Object классы для интернет-магазина SauceDemo.
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class BasePage:
    """
    Базовый класс для всех страниц с общей функциональностью.
    """
    def __init__(self, driver, base_url):
        """
        Инициализация базовой страницы.
        Args:
            driver: WebDriver экземпляр
            base_url: Базовый URL приложения
        """
        self.driver = driver
        self.base_url = base_url
        self.wait = WebDriverWait(driver, 10)


class LoginPage(BasePage):
    """
    Класс для работы со страницей авторизации.
    """
    def __init__(self, driver, base_url):
        """
        Инициализация страницы авторизации.
        Args:
            driver: WebDriver экземпляр
            base_url: Базовый URL приложения
        """
        super().__init__(driver, base_url)
        self.url = f"{self.base_url}"
        self._username_field = (By.ID, "user-name")
        self._password_field = (By.ID, "password")
        self._login_button = (By.ID, "login-button")

    @allure.step("Открыть страницу авторизации")
    def open(self):
        """
        Открывает страницу авторизации.
        Returns:
            LoginPage: Экземпляр текущей страницы
        """
        self.driver.get(self.url)
        return self

    @allure.step("Выполнить авторизацию с username: {username}, password: {password}")
    def login(self, username, password):
        """
        Выполняет авторизацию с указанными учетными данными.
        Args:
            username: Имя пользователя
            password: Пароль
        Returns:
            ProductsPage: Экземпляр страницы товаров
        """
        self.wait.until(EC.visibility_of_element_located(self._username_field)
                        ).send_keys(username)
        self.driver.find_element(*self._password_field).send_keys(password)
        self.driver.find_element(*self._login_button).click()
        return ProductsPage(self.driver, self.base_url)


class ProductsPage(BasePage):
    """
    Класс для работы со страницей каталога товаров.
    """
    def __init__(self, driver, base_url):
        """
        Инициализация страницы товаров.
        Args:
            driver: WebDriver экземпляр
            base_url: Базовый URL приложения
        """
        super().__init__(driver, base_url)
        self.url = f"{self.base_url}inventory.html"
        self._shopping_cart_link = (By.CLASS_NAME, "shopping_cart_link")

    @allure.step("Добавить товар в корзину: {item_name_slug}")
    def add_item_to_cart(self, item_name_slug):
        """
        Добавляет товар в корзину по его slug имени.
        Args:
            item_name_slug: Уникальный идентификатор товара
        Returns:
            ProductsPage: Экземпляр текущей страницы
        """
        add_button_locator = (By.ID, f"add-to-cart-{item_name_slug}")
        self.wait.until(EC.element_to_be_clickable(add_button_locator)).click()
        return self

    @allure.step("Перейти в корзину")
    def go_to_cart(self):
        """
        Переходит на страницу корзины.
        Returns:
            CartPage: Экземпляр страницы корзины
        """
        self.wait.until(EC.element_to_be_clickable(self._shopping_cart_link)
                        ).click()
        return CartPage(self.driver, self.base_url)


class CartPage(BasePage):
    """
    Класс для работы со страницей корзины.
    """
    def __init__(self, driver, base_url):
        """
        Инициализация страницы корзины.
        Args:
            driver: WebDriver экземпляр
            base_url: Базовый URL приложения
        """
        super().__init__(driver, base_url)
        self.url = f"{self.base_url}cart.html"
        self._checkout_button = (By.ID, "checkout")
        self._cart_item_name = (By.CLASS_NAME, "inventory_item_name")

    @allure.step("Нажать кнопку 'Checkout'")
    def click_checkout(self):
        """
        Нажимает кнопку оформления заказа.
        Returns:
            CheckoutStepOnePage: Экземпляр страницы оформления (шаг 1)
        """
        self.wait.until(EC.element_to_be_clickable(self._checkout_button)
                        ).click()
        return CheckoutStepOnePage(self.driver, self.base_url)

    @allure.step("Получить список товаров в корзине")
    def get_cart_items_names(self):
        """
        Получает названия всех товаров в корзине.
        Returns:
            list: Список названий товаров
        """
        items = self.driver.find_elements(*self._cart_item_name)
        return [item.text for item in items]


class CheckoutStepOnePage(BasePage):
    """
    Класс для работы со страницей ввода информации о пользователе.
    """
    def __init__(self, driver, base_url):
        """
        Инициализация страницы ввода данных.
        Args:
            driver: WebDriver экземпляр
            base_url: Базовый URL приложения
        """
        super().__init__(driver, base_url)
        self.url = f"{self.base_url}checkout-step-one.html"
        self._first_name_field = (By.ID, "first-name")
        self._last_name_field = (By.ID, "last-name")
        self._postal_code_field = (By.ID, "postal-code")
        self._continue_button = (By.ID, "continue")

    @allure.step("Заполнить информацию о пользователе: {first_name} {last_name} {postal_code}")
    def fill_user_info(self, first_name, last_name, postal_code):
        """
        Заполняет поля с информацией о пользователе.
        Args:
            first_name: Имя
            last_name: Фамилия
            postal_code: Почтовый индекс
        Returns:
            CheckoutStepOnePage: Экземпляр текущей страницы
        """
        self.wait.until(EC.visibility_of_element_located
                        (self._first_name_field)).send_keys(first_name)
        self.driver.find_element(*self._last_name_field).send_keys(last_name)
        self.driver.find_element(*self._postal_code_field
                                 ).send_keys(postal_code)
        return self

    @allure.step("Нажать кнопку 'Continue'")
    def click_continue(self):
        """
        Нажимает кнопку продолжения оформления заказа.
        Returns:
            CheckoutStepTwoPage: Экземпляр страницы подтверждения заказа
        """
        self.wait.until(EC.element_to_be_clickable(self._continue_button)
                        ).click()
        return CheckoutStepTwoPage(self.driver, self.base_url)


class CheckoutStepTwoPage(BasePage):
    """
    Класс для работы со страницей подтверждения заказа.
    """
    def __init__(self, driver, base_url):
        """
        Инициализация страницы подтверждения.
        Args:
            driver: WebDriver экземпляр
            base_url: Базовый URL приложения
        """
        super().__init__(driver, base_url)
        self.url = f"{self.base_url}checkout-step-two.html"
        self._total_price_label = (By.CLASS_NAME, "summary_total_label")

    @allure.step("Получить итоговую сумму заказа")
    def get_total_price(self):
        """
        Получает итоговую сумму заказа.
        Returns:
            str: Итоговая сумма в формате "$XX.XX"
        """
        total_element = self.wait.until(EC.visibility_of_element_located
                                        (self._total_price_label))
        return total_element.text.replace("Total: ", "")
