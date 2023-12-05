# accept an alert:
# alert = browser.switch_to.alert
# alert.accept()
#
# get text from an alert:
# alert = browser.switch_to.alert
# alert_text = alert.text
#
# confirm:
# confirm = browser.switch_to.alert
# confirm.accept()
# confirm.dismiss()
#
# prompt:
# prompt = browser.switch_to.alert
# prompt.send_keys("My answer")
# prompt.accept()
import time
import math

from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    browser = webdriver.Chrome()
    link = 'http://suninjuly.github.io/alert_accept.html'
    browser.get(link)

    start_button = browser.find_element(By.CSS_SELECTOR, '.btn')
    start_button.click()

    confirm = browser.switch_to.alert
    confirm.accept()

    x_obj = browser.find_element(By.CSS_SELECTOR, '#input_value')
    x = int(x_obj.text)
    result = math.log(abs(12 * math.sin(x)))

    input_field = browser.find_element(By.CSS_SELECTOR, '#answer')
    input_field.send_keys(result)

    submit_button = browser.find_element(By.CSS_SELECTOR, '.btn')
    submit_button.click()

finally:
    time.sleep(10)
    browser.quit()
