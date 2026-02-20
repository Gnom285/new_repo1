
# Открыть страницу калькулятора
# Ввести значение 45 в поле задержки (локатор #delay)
# Нажать кнопки: 7, +, 8, =
# Проверить (assert), что в окне отобразится результат 15 через 45 секунд

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.calculator_page import CalculatorPage

@pytest.fixture
def driver():
    service = Service(ChromeDriverManager().install())
    chrome_driver = webdriver.Chrome(service=service)
    chrome_driver.maximize_window()
    yield chrome_driver
    chrome_driver.quit()

def test_slow_calculator_sum(driver):
    # Создаем объект страницы
    calculator = CalculatorPage(driver)
    
    # 1. Открыть страницу
    calculator.open()
    
    # 2. Ввести значение 45 в поле задержки
    calculator.set_delay("45")
    
    # 3. Нажать кнопки 7, +, 8, =
    calculator.click_button("7")
    calculator.click_button("+")
    calculator.click_button("8")
    calculator.click_button("=")
    
    # 4. Проверить результат через 45 секунд
    # Используем таймаут чуть больше задержки (например, 50 секунд)
    result = calculator.get_result("15", 50)
    
    assert result == "15"