import time
import math

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope='class')
def test_auth(browser, auth_data):
    link = 'https://stepik.org/lesson/236895/step/1'
    browser.implicitly_wait(5)
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, '#ember33').click()
    browser.find_element(By.CSS_SELECTOR, '#id_login_email').send_keys(auth_data[0])
    browser.find_element(By.CSS_SELECTOR, '#id_login_password').send_keys(auth_data[1])
    browser.find_element(By.CSS_SELECTOR, '.button_with-loader').click()
    comment_button = WebDriverWait(browser, 5).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, '.comment-input__bait'), 'Оставить комментарий')
    )
    browser.find_element(By.CSS_SELECTOR, '.comment-input__bait')
    assert browser.find_element(By.CSS_SELECTOR, '.comment-input__bait').text == 'Оставить комментарий'


class TestStepic:
    @pytest.mark.parametrize('ref', [
        # "https://stepik.org/lesson/236895/step/1",
        # "https://stepik.org/lesson/236896/step/1",
        # "https://stepik.org/lesson/236897/step/1"
        "https://stepik.org/lesson/236898/step/1",
        "https://stepik.org/lesson/236899/step/1",
        "https://stepik.org/lesson/236903/step/1",
        "https://stepik.org/lesson/236904/step/1",
        "https://stepik.org/lesson/236905/step/1"
    ])
    def test_simple_test(self, browser, test_auth, ref):
        browser.get(f'{ref}')
        answer = math.log(int(time.time()))
        browser.find_element(By.CSS_SELECTOR, '.ember-text-area').send_keys(answer)
        browser.find_element(By.CSS_SELECTOR, '.submit-submission').click()
        assert browser.find_element(By.CSS_SELECTOR, '.smart-hints__hint').text == 'Correct!'

# this fixture was added to the conftest.py :
# @pytest.fixture(scope='class')
# def auth_data():
#     data = ('my_email', 'my_password')
#     return data

# and this one:
# @pytest.fixture(scope='class')
# def browser():
#     print("\nstart browser for test..")
#     browser = webdriver.Chrome()
#     yield browser
#     print("\nquit browser..")
#     browser.quit()
