from selenium import webdriver
from selenium.webdriver.common.by import By

# In order to avoid errors related with JS scripts and dynamic pages we need use .implicitly_wait method:
# common exceptions:
# NoSuchElementException
# StaleElementReferenceException
# ElementNotVisibleException

try:
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)

    browser.get("http://suninjuly.github.io/wait1.html")

    button = browser.find_element(By.ID, "verify")
    button.click()
    message = browser.find_element(By.ID, "verify_message")

    assert "successful" in message.text

finally:
    browser.quit()