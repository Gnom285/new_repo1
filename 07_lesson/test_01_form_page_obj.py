
import pytest
from selenium import webdriver
from pages.FormPage import FormPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(3)
    driver.maximize_window()
    yield driver
    driver.quit()


def test_form_submission_flow(driver):

    form_page = FormPage(driver)

    form_page.open()
    form_page.fill_form()
    form_page.submit_form()

    assert form_page.is_zip_code_error()
    assert form_page.are_fields_success()
