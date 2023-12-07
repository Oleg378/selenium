from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest

def script(lnk):
    browser = webdriver.Chrome()
    browser.get(lnk)

    input_first_name = browser.find_element(By.CSS_SELECTOR, ".first:required")
    input_last_name = browser.find_element(By.CSS_SELECTOR, ".second:required")
    input_email = browser.find_element(By.CSS_SELECTOR, ".third:required")

    input_first_name.send_keys("Biba")
    input_last_name.send_keys("Bobav")
    input_email.send_keys("fhdfjvkjcv@jgjf.d")

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    return welcome_text


class TestSanity(unittest.TestCase):
    final_value = 'Congratulations! You have successfully registered!'

    def test_first(self):
        self.assertEqual(script('http://suninjuly.github.io/registration1.html'), TestSanity.final_value, 'you failed')


    def test_second(self):
        self.assertEqual(script('http://suninjuly.github.io/registration2.html'), TestSanity.final_value, 'you failed')


if __name__ == "__main__":
    unittest.main()