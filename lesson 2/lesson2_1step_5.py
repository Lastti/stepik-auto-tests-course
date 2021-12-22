from selenium import webdriver
import time
import math
from selenium.webdriver.common.by import By


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))
try:
    link = 'http://suninjuly.github.io/math.html'
    browser = webdriver.Chrome()
    browser.get(link)


    x_element = browser.find_element(By.ID, 'input_value')
    x = x_element.text
    y = calc(x)

    input1 = browser.find_element(By.ID, 'answer')
    input1.send_keys(y)

    input2 = browser.find_element(By.CSS_SELECTOR, '[for="robotCheckbox"]')
    input2.click()

    input3 = browser.find_element(By.CSS_SELECTOR, '[for="robotsRule"]')
    input3.click()

    input4 = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    input4.click()

finally:
    time.sleep(30)
    browser.quit()





