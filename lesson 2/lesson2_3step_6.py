import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import math

link = 'http://suninjuly.github.io/redirect_accept.html'

try:

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element(By.CLASS_NAME, 'trollface')
    button.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x_element = browser.find_element(By.ID, 'input_value')
    x = x_element.text
    y = calc(x)

    input = browser.find_element(By.ID, 'answer')
    input.send_keys(y)

    submit = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    submit.click()

finally:
    time.sleep(30)
    browser.quit()



