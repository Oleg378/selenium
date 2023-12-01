import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import math

try:
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.CSS_SELECTOR, '#input_value')
    x = int(x_element.text)
    result = math.log(abs(12 * math.sin(x)))

    input_result = browser.find_element(By.CSS_SELECTOR, '#answer')
    checkbox = browser.find_element(By.CSS_SELECTOR, '#robotCheckbox')
    radiobutton = browser.find_element(By.CSS_SELECTOR, '#robotsRule')
    submit_button = browser.find_element(By.CSS_SELECTOR, '.btn')

    input_result.send_keys(result)
    checkbox.click()
    radiobutton.click()
    submit_button.click()

finally:
    time.sleep(10)
    browser.quit()


