from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

import time
import math
def calc(x,y):
    return str(int(x) + int(y))

try:
    link = 'http://suninjuly.github.io/selects1.html'
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element(By.ID, 'num1')
    first = x.text
    y = browser.find_element(By.ID, 'num2')
    second = y.text
    summ = calc(first,second)

    select = Select(browser.find_element(By.TAG_NAME, 'select'))
    select.select_by_value(summ)

    submit_input = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    submit_input.click()

finally:
    time.sleep(30)
    browser.quit()
