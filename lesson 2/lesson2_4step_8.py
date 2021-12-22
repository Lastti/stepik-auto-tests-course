import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math

link = 'http://suninjuly.github.io/explicit_wait2.html'

try:
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element(By.ID, 'book')
    WebDriverWait(browser,12).until(EC.text_to_be_present_in_element((By.ID, 'price'), '$100'))
    button.click()

    x_element = browser.find_element(By.ID, 'input_value').text
    y = calc(x_element)

    input = browser.find_element(By.ID, 'answer')
    input.send_keys(y)

    submit = browser.find_element(By.ID, 'solve')
    submit.click()
finally:
    time.sleep(30)
    # browser.quit()
