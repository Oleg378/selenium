import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    link = 'http://suninjuly.github.io/file_input.html'
    browser = webdriver.Chrome()
    browser.get(link)

    first_name = browser.find_element(By.NAME, 'firstname')
    last_name = browser.find_element(By.NAME, 'lastname')
    email = browser.find_element(By.NAME, 'email')
    first_name.send_keys('biba')
    last_name.send_keys('bobff')
    email.send_keys('sdfsd@fff.qqq')

    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла

    upload_elem = browser.find_element(By.CSS_SELECTOR, '#file')
    upload_elem.send_keys(file_path)

    submit = browser.find_element(By.CSS_SELECTOR, '.btn')
    submit.click()

finally:
    time.sleep(10)
    browser.quit()
