"""
Тесты для проверки работы калькулятора с задержкой.
"""
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.calculator_page import CalculatorPage
import allure


@pytest.fixture
def driver():
    """
    Фикстура для инициализации и закрытия драйвера Chrome.
    Returns:
        WebDriver: Экземпляр драйвера Chrome
    """
    service = Service(ChromeDriverManager().install())
    chrome_driver = webdriver.Chrome(service=service)
    chrome_driver.maximize_window()
    yield chrome_driver
    chrome_driver.quit()


@allure.feature("Калькулятор с задержкой")
@allure.story("Вычисление суммы с задержкой")
@allure.title("Проверка сложения 7 + 8 с задержкой 45 секунд")
@allure.description("""
    Тест проверяет работу калькулятора с установленной задержкой:
    1. Устанавливается задержка 45 секунд
    2. Выполняется операция 7 + 8
    3. Результат 15 отображается через указанную задержку
""")
@allure.severity(allure.severity_level.NORMAL)
def test_slow_calculator_sum(driver):
    """
    Тест проверяет корректность вычисления суммы с задержкой.
    Args:
        driver: WebDriver экземпляр из фикстуры
    Returns:
        None
    """
    with allure.step("Создать экземпляр страницы калькулятора"):
        calculator = CalculatorPage(driver)
    with allure.step("Открыть страницу калькулятора"):
        calculator.open()
    with allure.step("Установить задержку 45 секунд"):
        calculator.set_delay("45")
    with allure.step("Выполнить вычисление 7 + 8"):
        calculator.click_button("7")
        calculator.click_button("+")
        calculator.click_button("8")
        calculator.click_button("=")
    with allure.step("Ожидать результат 15 (таймаут 50 секунд)"):
        result = calculator.get_result("15", 50)
    with allure.step("Проверить, что результат равен 15"):
        assert result == "15", f"Ожидался результат '15', получен '{result}'"
    with allure.step("Логирование успешного завершения теста"):
        allure.attach(
            f"Результат вычисления: {result}",
            name="Результат операции",
            attachment_type=allure.attachment_type.TEXT
        )
