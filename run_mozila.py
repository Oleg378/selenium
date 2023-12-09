import time

from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

driver.get('https://habr.com/ru/articles/448786/')
time.sleep(4)
driver.quit()

# https://pypi.org/project/webdriver-manager/