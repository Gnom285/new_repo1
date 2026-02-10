
# Перейдите на сайт http://uitestingplayground.com/textinput
# Укажите в поле ввода текст SkyPro
# Нажмите на синюю кнопку
# Получите текст кнопки и выведите в консоль ("SkyPro")
# использовала FireFox т.к. через хром не даёт открыть касперский

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

driver.get("http://uitestingplayground.com/textinput")

element = driver.find_element(By.CSS_SELECTOR, "#newButtonName")
element.send_keys("SkyPro")

driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()

content = driver.find_element(By.CSS_SELECTOR, "#updatingButton").text
print(content)

driver.quit()
