
# Открыть браузер Google Chrome
# Перейти на страницу: http://uitestingplayground.com/dynamicid.
# Кликнуть на синюю кнопку

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("http://uitestingplayground.com/dynamicid")

element = WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, ".btn-primary"))
)
element.click()


driver.find_element(By.CSS_SELECTOR,".btn-primary").click()
