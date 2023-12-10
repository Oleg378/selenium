import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By


#  you will use conftest file in order to define common fixture one time for several tests


# in this case when you use this browser() fixture you will be able to choose between chrome nad firefox:
def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome()
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()


# In order to pick between firefox and chrome you need write:
# pytest -s -v --browser_name=chrome filename.py
# pytest -s -v --browser_name=firefox filename.py

# basic browser() definition:
#
# @pytest.fixture(scope='class')
# def browser():
#     print("\nstart browser for test..")
#     browser = webdriver.Chrome()
#     yield browser
#     print("\nquit browser..")
#     browser.quit()


@pytest.fixture(scope='class')
def auth_data():
    data = ('my_email', 'my_password')  # you need add here a real data.
    return data
