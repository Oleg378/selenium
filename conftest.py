import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture(scope='class')
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


#  you will use conftest file in order to define common fixture one time for several tests


@pytest.fixture(scope='class')
def auth_data():
    data = ('my_email', 'my_password') # you need add here a real data.
    return data

