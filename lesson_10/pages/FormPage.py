"""
Модуль содержит Page Object для формы регистрации.
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class FormPage:
    """
    Класс для работы со страницей формы регистрации данных.
    Содержит методы для заполнения формы, отправки и проверки результатов.
    """

    def __init__(self, driver):
        """
        Инициализация страницы формы.
        Args:
            driver: WebDriver экземпляр
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)
        self.fields = {
            'first-name': "Иван",
            'last-name': "Петров",
            'address': "Ленина, 55-3",
            'zip-code': "",
            'city': "Москва",
            'country': "Россия",
            'e-mail': "test@skypro.com",
            'phone': "+7985899998787",
            'job-position': "QA",
            'company': "SkyPro"
        }

    @allure.step("Открыть страницу формы регистрации")
    def open(self) -> None:
        """
        Открывает страницу формы регистрации данных.
        Returns:
            None
        """
        self.driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
        )

    @allure.step("Заполнить все поля формы данными")
    def fill_form(self) -> None:
        """
        Заполняет все поля формы предопределенными данными.
        Returns:
            None
        """
        for field, value in self.fields.items():
            self.wait.until(EC.presence_of_element_located((By.NAME, field))
                            ).send_keys(value)

    @allure.step("Отправить форму")
    def submit_form(self) -> None:
        """
        Нажимает кнопку отправки формы.
        Returns:
            None
        """
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                                   '[type="submit"]'))).click()

    @allure.step("Получить CSS класс элемента по ID: {field_id}")
    def get_field_class(self, field_id: str) -> str:
        """
        Получает значение атрибута class для элемента по его ID.
        Args:
            field_id: ID элемента
        Returns:
            str: Значение атрибута class
        """
        element = self.wait.until(EC.presence_of_element_located
                                  ((By.ID, field_id)))
        return element.get_attribute("class")

    @allure.step("Проверить наличие ошибки в поле zip-code")
    def check_zip_code_error(self) -> bool:
        """
        Проверяет, что поле zip-code имеет класс alert-danger (ошибка).
        Returns:
            bool: True если ошибка присутствует, иначе False
        """
        return "alert-danger" in self.get_field_class("zip-code")

    @allure.step("Проверить успешное заполнение остальных полей")
    def check_fields_success(self) -> bool:
        """
        Проверяет, что все поля (кроме zip-code) имеют класс success.
        Returns:
            bool: True если все поля успешно валидированы, иначе False
        """
        fields = ['first-name', 'last-name', 'address', 'e-mail', 'phone',
                  'city', 'country', 'job-position', 'company']
        for field in fields:
            if "success" not in self.get_field_class(field):
                return False
        return True

    @allure.step("Выполнить проверку результатов отправки формы")
    def check_form_submission(self) -> None:
        """
        Выполняет комплексную проверку формы:
        - zip-code должен быть подсвечен как ошибка (alert-danger)
        - остальные поля должны быть подсвечены как успешные (success)
        Returns:
            None
        Raises:
            AssertionError: Если проверки не пройдены
        """
        assert self.check_zip_code_error(), ""
        "Поле zip-code не подсвечено как ошибка"
        assert self.check_fields_success(), ""
        "Не все поля подсвечены как успешные"
