import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"


@pytest.fixture  # you can use @pytest.fixture(scope="class") or "function", class", "module", "session"
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    # этот код выполнится после завершения теста
    print("\nquit browser..")
    browser.quit()


@pytest.fixture(autouse=True)  # autouse=True will indicate that this one will be used without direct calling inside
# each testcase
def prepare_data():
    print()
    print("preparing some critical data for every test")


class TestMainPage1():
    # вызываем фикстуру в тесте, передав ее как параметр

    @pytest.mark.smoke
    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "#login_link")

    @pytest.mark.regression
    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")

# pytest -s -v fixture.py pytest -s -v -m smoke fixture.py - you cag run only tests marked with specific name (you
# need use '-m' mode and call required mark name, for example 'smoke')

# aslo strictly recommended to create pytest.ini file:
# [pytest]
# markers =
#     smoke: marker for smoke tests
#     regression: marker for regression tests
