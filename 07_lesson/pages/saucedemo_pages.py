
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url
        self.wait = WebDriverWait(driver, 10)

class LoginPage(BasePage):
    def __init__(self, driver, base_url):
        super().__init__(driver, base_url)
        self.url = f"{self.base_url}"
        self._username_field = (By.ID, "user-name")
        self._password_field = (By.ID, "password")
        self._login_button = (By.ID, "login-button")

    def open(self):
        self.driver.get(self.url)
        return self

    def login(self, username, password):
        self.wait.until(EC.visibility_of_element_located(self._username_field)).send_keys(username)
        self.driver.find_element(*self._password_field).send_keys(password)
        self.driver.find_element(*self._login_button).click()
        return ProductsPage(self.driver, self.base_url)

class ProductsPage(BasePage):
    def __init__(self, driver, base_url):
         super().__init__(driver, base_url)
         self.url = f"{self.base_url}inventory.html"
         self._shopping_cart_link = (By.CLASS_NAME, "shopping_cart_link")

    def add_item_to_cart(self, item_name_slug):
         add_button_locator = (By.ID, f"add-to-cart-{item_name_slug}")
         self.wait.until(EC.element_to_be_clickable(add_button_locator)).click()
         return self

    def go_to_cart(self):
         self.wait.until(EC.element_to_be_clickable(self._shopping_cart_link)).click()
         return CartPage(self.driver, self.base_url)

class CartPage(BasePage):
    def __init__(self, driver, base_url):
        super().__init__(driver, base_url)
        self.url = f"{self.base_url}cart.html"
        self._checkout_button = (By.ID, "checkout")
        self._cart_item_name = (By.CLASS_NAME, "inventory_item_name")

    def click_checkout(self):
        self.wait.until(EC.element_to_be_clickable(self._checkout_button)).click()
        return CheckoutStepOnePage(self.driver, self.base_url)

    def get_cart_items_names(self):
        items = self.driver.find_elements(*self._cart_item_name)
        return [item.text for item in items]

class CheckoutStepOnePage(BasePage):
    def __init__(self, driver, base_url):
        super().__init__(driver, base_url)
        self.url = f"{self.base_url}checkout-step-one.html"
        self._first_name_field = (By.ID, "first-name")
        self._last_name_field = (By.ID, "last-name")
        self._postal_code_field = (By.ID, "postal-code")
        self._continue_button = (By.ID, "continue")

    def fill_user_info(self, first_name, last_name, postal_code):
        self.wait.until(EC.visibility_of_element_located(self._first_name_field)).send_keys(first_name)
        self.driver.find_element(*self._last_name_field).send_keys(last_name)
        self.driver.find_element(*self._postal_code_field).send_keys(postal_code)
        return self

    def click_continue(self):
        self.wait.until(EC.element_to_be_clickable(self._continue_button)).click()
        return CheckoutStepTwoPage(self.driver, self.base_url)

class CheckoutStepTwoPage(BasePage):
    def __init__(self, driver, base_url):
        super().__init__(driver, base_url)
        self.url = f"{self.base_url}checkout-step-two.html"
        self._total_price_label = (By.CLASS_NAME, "summary_total_label")

    def get_total_price(self):
        total_element = self.wait.until(EC.visibility_of_element_located(self._total_price_label))
        return total_element.text.replace("Total: ", "")