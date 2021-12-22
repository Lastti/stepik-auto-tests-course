from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    link = 'http://suninjuly.github.io/get_attribute.html'

    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.ID, 'treasure')
    x = x_element.get_attribute('valuex')
    y = calc(x)

    input = browser.find_element(By.ID, 'answer')
    input.send_keys(y)

    robot_checkbox = browser.find_element(By.ID, 'robotCheckbox')
    robot_checkbox.click()

    robot_radiobutton = browser.find_element(By.ID, 'robotsRule')
    robot_radiobutton.click()

    submit_input = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    submit_input.click()

finally:
    time.sleep(30)
    browser.quit()
