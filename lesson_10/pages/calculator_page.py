"""
Модуль содержит Page Object для страницы калькулятора с задержкой.
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class CalculatorPage:
    """
    Класс для работы со страницей калькулятора с задержкой вычислений.
    Содержит методы для установки задержки,
    нажатия кнопок и получения результата.
    """
    def __init__(self, driver):
        """
        Инициализация страницы калькулятора.
        Args:
            driver: WebDriver экземпляр
        """
        self.driver = driver
        self.url = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
        # Локаторы
        self._delay_input = (By.CSS_SELECTOR, "#delay")
        self._screen = (By.CLASS_NAME, "screen")

    @allure.step("Открыть страницу калькулятора")
    def open(self) -> None:
        """
        Открывает страницу калькулятора.
        Returns:
            None
        """
        self.driver.get(self.url)

    @allure.step("Установить задержку: {seconds} секунд")
    def set_delay(self, seconds: str) -> None:
        """
        Устанавливает задержку перед вычислением результата.
        Args:
            seconds: Значение задержки в секундах
        Returns:
            None
        """
        delay = self.driver.find_element(*self._delay_input)
        delay.clear()
        delay.send_keys(seconds)

    @allure.step("Нажать кнопку: {text}")
    def click_button(self, text: str) -> None:
        """
        Нажимает кнопку на калькуляторе
        Args:
            text: Текст на кнопке (цифра, оператор или '=')
        Returns:
            None
        """
        button_locator = (By.XPATH, f"//span[text()='{text}']")
        self.driver.find_element(*button_locator).click()

    @allure.step("Получить результат вычислений, ожидая значение:"" {expected_value}")
    def get_result(self, expected_value: str, timeout: int) -> str:
        """
        Ожидает появления ожидаемого результата на экране калькулятора.
        Args:
            expected_value: Ожидаемое значение результата
            timeout: Максимальное время ожидания в секундах
        Returns:
            str: Текст результата с экрана калькулятора
        """
        wait = WebDriverWait(self.driver, timeout)
        wait.until(EC.text_to_be_present_in_element
                   (self._screen, expected_value))
        return self.driver.find_element(*self._screen).text
