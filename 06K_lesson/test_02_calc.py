
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

element = driver.find_element(By.CSS_SELECTOR, "#delay")
element.clear()
element.send_keys("45")

driver.find_element(By.XPATH, "// span[text()='7']").click()

driver.find_element(By.XPATH, "// span[text()='+']").click()

driver.find_element(By.XPATH, "// span[text()='8']").click()

driver.find_element(By.XPATH, "// span[text()='=']").click()

wait = WebDriverWait(driver, 45)

screen_locator = (By.CLASS_NAME, "screen")
wait.until(EC.text_to_be_present_in_element(screen_locator, "15"))

result = driver.find_element(*screen_locator).text
assert result == "15"


driver.quit()