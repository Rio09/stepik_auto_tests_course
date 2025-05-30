import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestRegistration(unittest.TestCase):

    def test_registration1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Заполняем форму
        input1 = browser.find_element(By.XPATH, "//div[label[text()='First name*']]//input")
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.XPATH, "//div[label[text()='Last name*']]//input")
        input2.send_keys("Petrov")
        input3 = browser.find_element(By.XPATH, "//div[label[text()='Email*']]//input")
        input3.send_keys("test@test.com")

        # Отправляем форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем результат
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text

        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!")

        browser.quit()

    def test_registration2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Заполняем форму
        input1 = browser.find_element(By.XPATH, "//div[label[text()='First name*']]//input")
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.XPATH, "//div[label[text()='Last name*']]//input")
        input2.send_keys("Petrov")
        input3 = browser.find_element(By.XPATH, "//div[label[text()='Email*']]//input")
        input3.send_keys("test@test.com")

        # Отправляем форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем результат
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text

        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!")

        browser.quit()