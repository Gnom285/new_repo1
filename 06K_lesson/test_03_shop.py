

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_03_shop():

    s = Service(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=s)

    try:

        driver.get("https://www.saucedemo.com/")
    

        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()


        driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()

        driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()

        driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()



        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()



        driver.find_element(By.ID, "checkout").click()



        driver.find_element(By.ID, "first-name").send_keys("Иван")
        driver.find_element(By.ID, "last-name").send_keys("Петров")
        driver.find_element(By.ID, "postal-code").send_keys("12345")



        driver.find_element(By.ID, "continue").click()



        total_price_element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "summary_total_label"))
        )
        total_text = total_price_element.text
        final_total = total_text.replace("Total: ", "")

        assert final_total == "$58.29", f"Сумма не совпадает! Ожидалось $58.29, а получили {final_total}"
        print(f"Тест пройден, итоговая сумма: {final_total} - как и ожидалось!")

    except Exception as e:
        print(f"Тест провалился из-за ошибки: {e}")

    finally:
        driver.quit()


