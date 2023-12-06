# syntax for switching:
# browser.switch_to.window(window_name)
#
# How to get window name:
# new_window = browser.window_handles[1]
# first_window = browser.window_handles[0]
import time
import math

from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    link = 'http://suninjuly.github.io/redirect_accept.html'
    browser = webdriver.Chrome()
    browser.get(link)

    start_btn = browser.find_element(By.CSS_SELECTOR, '.trollface.btn')
    start_btn.click()

    browser.switch_to.window(browser.window_handles[1])

    x_obj = browser.find_element(By.CSS_SELECTOR, '#input_value')
    x = int(x_obj.text)
    result = math.log(abs(12 * math.sin(x)))

    input_field = browser.find_element(By.CSS_SELECTOR, '#answer')
    input_field.send_keys(result)

    submit = browser.find_element(By.CSS_SELECTOR, '.btn')
    submit.click()

finally:
    time.sleep(10)
    browser.quit()
