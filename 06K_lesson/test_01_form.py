


from selenium import webdriver
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By


def test_01_form():
    service_for_edge = Service(EdgeChromiumDriverManager().install())

    driver = webdriver.Edge(service=service_for_edge)


    try:

        driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")


        first_name_field = driver.find_element(By.ID, "first-name")
        first_name_field.send_keys("Иван")


        last_name_field = driver.find_element(By.ID, "last-name")
        last_name_field.send_keys("Петров")


        address_field = driver.find_element(By.ID, "address")
        address_field.send_keys("Ленина, 55-3")


        email_field = driver.find_element(By.ID, "email")
        email_field.send_keys("test@skypro.com")


        phone_field = driver.find_element(By.ID, "phone")
        phone_field.send_keys("+7985899998787")



        city_field = driver.find_element(By.ID, "city")
        city_field.send_keys("Москва")


        country_field = driver.find_element(By.ID, "country")
        country_field.send_keys("Россия")


        job_field = driver.find_element(By.ID, "job-position")
        job_field.send_keys("QA")


        company_field = driver.find_element(By.ID, "company")
        company_field.send_keys("SkyPro")


        submit_button = driver.find_element(By.ID, "submit-button")
        submit_button.click()



        EXPECTED_RED_COLOR = "rgb(248, 215, 218)"

        EXPECTED_GREEN_COLOR = "rgb(209, 231, 221)"


        zip_code_element = driver.find_element(By.ID, "zip-code")
        actual_zip_color = zip_code_element.value_of_css_property("color")


        assert actual_zip_color == EXPECTED_RED_COLOR, \
            f"Поле 'Zip code' должно быть красным. Ожидался '{EXPECTED_RED_COLOR}', а получили '{actual_zip_color}'"
        print("Проверка Zip code: ОК (красный)")



        all_green_fields_ids = [
            "first-name", "last-name", "address", "email", "phone",
            "city", "country", "job-position", "company"
        ]


        for field_id_name in all_green_fields_ids:
            field_element = driver.find_element(By.ID, field_id_name)
            actual_field_color = field_element.value_of_css_property("color")


            assert actual_field_color == EXPECTED_GREEN_COLOR, \
                f"Поле '{field_id_name}' должно быть зеленым. " \
                f"Ожидался '{EXPECTED_GREEN_COLOR}', а получили '{actual_field_color}'"
            print(f"Проверка поля '{field_id_name}': ОК (зеленый)")

        print("Все проверки цветов формы прошли успешно!")

    except Exception as general_error:

        print(f"ОШИБКА! Тест провалился: {general_error}")

    finally:

        if driver:
            driver.quit()