"""
Тесты для проверки формы регистрации данных.
"""
import pytest
from selenium import webdriver
from pages.FormPage import FormPage
import allure


@pytest.fixture
def driver():
    """
    Фикстура для инициализации и закрытия драйвера Chrome.
    Returns:
        WebDriver: Экземпляр драйвера Chrome
    """
    driver = webdriver.Chrome()
    driver.implicitly_wait(3)
    driver.maximize_window()
    yield driver
    driver.quit()


@allure.feature("Форма регистрации данных")
@allure.story("Проверка валидации полей формы")
@allure.title("Проверка успешной отправки формы с валидацией полей")
@allure.description("""
    Тест проверяет, что при отправке формы:
    - Поле zip-code подсвечивается красным (alert-danger)
    - Остальные поля подсвечиваются зеленым (success)
""")
@allure.severity(allure.severity_level.CRITICAL)
def test_form_submission_flow(driver):
    """
    Тест проверяет корректность валидации полей формы.
    Шаги:
    1. Открыть страницу формы
    2. Заполнить все поля
    3. Отправить форму
    4. Проверить результаты валидации
    Args:
        driver: WebDriver экземпляр из фикстуры
    Returns:
        None
    """
    with allure.step("Создать экземпляр страницы формы"):
        form_page = FormPage(driver)
    with allure.step("Выполнить основной сценарий заполнения формы"):
        form_page.open()
        form_page.fill_form()
        form_page.submit_form()
    with allure.step("Проверить результаты валидации полей"):
        form_page.check_form_submission()
    with allure.step("Логирование успешного завершения теста"):
        allure.attach(
            "Форма успешно отправлена, валидация полей работает корректно",
            name="Результат теста",
            attachment_type=allure.attachment_type.TEXT
        )
