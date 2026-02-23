
# Создать класс для страницы калькулятора, 
# который будет содержать методы для взаимодействия с элементами
# Поле ввода задержки (локатор #delay)
# Кнопки калькулятора (цифры, операторы, кнопка =)
# Поле вывода результата

# калькулятор

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
        # Локаторы
        self._delay_input = (By.CSS_SELECTOR, "#delay")
        self._screen = (By.CLASS_NAME, "screen")

    def open(self):
        self.driver.get(self.url)

    def set_delay(self, seconds: str):
        delay = self.driver.find_element(*self._delay_input)
        delay.clear()
        delay.send_keys(seconds)

    def click_button(self, text: str):
        button_locator = (By.XPATH, f"//span[text()='{text}']")
        self.driver.find_element(*button_locator).click()

    def get_result(self, expected_value: str, timeout: int) -> str:
        wait = WebDriverWait(self.driver, timeout)
        wait.until(EC.text_to_be_present_in_element(self._screen, expected_value))
        return self.driver.find_element(*self._screen).text