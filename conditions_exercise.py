import time
import math

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()

try:
    browser.get('http://suninjuly.github.io/explicit_wait2.html')

    # in this case we should wait until price will = 100
    price = WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#price'), '100')
        )

    book_button = browser.find_element(By.CSS_SELECTOR, '#book')
    book_button.click()

    x_obj = browser.find_element(By.CSS_SELECTOR, '#input_value')
    x = int(x_obj.text)
    result = math.log(abs(12 * math.sin(x)))

    input_field = browser.find_element(By.CSS_SELECTOR, '#answer')
    input_field.send_keys(result)

    submit = browser.find_element(By.CSS_SELECTOR, '#solve')
    submit.click()

finally:
    time.sleep(10)
    browser.quit()
