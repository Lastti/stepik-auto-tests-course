from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try:
    link = 'http://suninjuly.github.io/execute_script.html'

    browser = webdriver.Chrome()
    browser.get(link)

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    x_element = browser.find_element(By.ID, 'input_value')
    x = x_element.text
    answer = calc(x)

    input = browser.find_element(By.ID, 'answer')
    input.send_keys(answer)

    checkbox = browser.find_element(By.CSS_SELECTOR, '[for="robotCheckbox"')
    checkbox.click()

    radiobutton = browser.find_element(By.CSS_SELECTOR, '[for="robotsRule"')
    browser.execute_script("return arguments[0].scrollIntoView(true);", radiobutton)
    radiobutton.click()

    submit = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    browser.execute_script("return arguments[0].scrollIntoView(true);", submit)
    submit.click()

finally:
    time.sleep(30)
    browser.quit()





