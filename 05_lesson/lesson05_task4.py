
# Открыть браузер FireFox
# Перейти на страницу http://the-internet.herokuapp.com/login
# В поле username ввести значение tomsmith
# В поле password ввести значение SuperSecretPassword!
# Нажать кнопку Login
# Вывести текст с зеленой плашки в консоль
# Закрыть браузер (метод quit())


from selenium import webdriver
from selenium.webdriver.firefox.service import Service 
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

try:
    driver.get("http://the-internet.herokuapp.com/login")

    wait = WebDriverWait(driver, 10)

    driver.find_element(By.ID, "username").send_keys("tomsmith")

    driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")

    driver.find_element(By.CSS_SELECTOR, "button.radius").click()

finally: 
    if driver: driver.quit()




