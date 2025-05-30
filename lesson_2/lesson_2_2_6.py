import document
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "https://suninjuly.github.io/execute_script.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    option1 = browser.find_element(By.ID, "robotCheckbox")
    option1.click()
    option2 = browser.find_element(By.ID, "robotsRule")
    option2.click()
    button.click()
    #button = browser.find_element(By.TAG_NAME, "button")
    #browser.execute_script("window.scrollBy(0, 100);")
    #browser.execute_script("return arguments[0].scrollIntoView(true);", button)

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()