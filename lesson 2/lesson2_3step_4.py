import math
import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

link = 'http://suninjuly.github.io/alert_accept.html'

try:

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element(By.CLASS_NAME, 'btn-primary')
    button.click()

    confirm = browser.switch_to.alert
    confirm.accept()

    x_element = browser.find_element(By.ID, 'input_value')
    x = x_element.text
    answer = calc(x)

    input = browser.find_element(By.ID, 'answer')
    input.send_keys(answer)

    submit = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    submit.click()
finally:
    time.sleep(30)
    browser.quit()






