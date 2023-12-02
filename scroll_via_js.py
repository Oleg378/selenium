import time
import math

from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    link = 'http://suninjuly.github.io/execute_script.html'
    browser = webdriver.Chrome()
    browser.get(link)

    x = int(browser.find_element(By.CSS_SELECTOR, '#input_value').text)
    result = math.log(abs(12 * math.sin(x)))

    input_result = browser.find_element(By.CSS_SELECTOR, '#answer')
    input_result.send_keys(result)

    submit_button = browser.find_element(By.CSS_SELECTOR, '.btn')
    browser.execute_script("return arguments[0].scrollIntoView(true);", submit_button)

    checkbox = browser.find_element(By.CSS_SELECTOR, '#robotCheckbox')
    radiobutton = browser.find_element(By.CSS_SELECTOR, '#robotsRule')
    checkbox.click()
    radiobutton.click()

    submit_button.click()

finally:
    time.sleep(10)
    browser.quit()
