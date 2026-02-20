
# Открыть браузер FireFox
# Перейти на страницу: http://the-internet.herokuapp.com/inputs
# Ввести в поле текст Sky
# Очистить это поле (метод clear())
# Ввести в поле текст Pro
# Закрыть браузер (метод quit())


from selenium import webdriver
from selenium.webdriver.firefox.service import Service 
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

driver.get("http://the-internet.herokuapp.com/inputs")

input_field = driver.find_element(By.TAG_NAME, "input")

input_field.send_keys("Sky")

input_field.clear()

input_field.send_keys("Pro")

driver.quit()
