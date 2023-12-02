import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

try:

    link = 'http://suninjuly.github.io/get_attribute.html'
    browser = webdriver.Chrome()
    browser.get(link)

    target_element = browser.find_element(By.CSS_SELECTOR, '#treasure')
    x = int(target_element.get_attribute('valuex'))
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


