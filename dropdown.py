# select.select_by_visible_text("text")
# select.select_by_index(index)
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

try:
    link = 'https://suninjuly.github.io/selects1.html'
    browser = webdriver.Chrome()
    browser.get(link)

    num1_element = browser.find_element(By.CSS_SELECTOR, '#num1')
    num2_element = browser.find_element(By.CSS_SELECTOR, '#num2')
    result = int(num1_element.text) + int(num2_element.text)

    select_dropdown = Select(browser.find_element(By.CSS_SELECTOR, '#dropdown'))
    select_dropdown.select_by_value(str(result))

    submit = browser.find_element(By.CSS_SELECTOR, '.btn')
    submit.click()

finally:
    time.sleep(10)
    browser.quit()
