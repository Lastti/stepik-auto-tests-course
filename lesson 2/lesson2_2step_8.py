import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    name_input = browser.find_element(By.CSS_SELECTOR, "[name='firstname']")
    name_input.send_keys('A')

    surname_input = browser.find_element(By.CSS_SELECTOR, "[name='lastname']")
    surname_input.send_keys('S')

    email_input = browser.find_element(By.CSS_SELECTOR, "[name='email']")
    email_input.send_keys('S@mail.ru')

    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_name = "file.txt"
    file_path = os.path.join(current_dir, file_name)  # добавляем к этому пути имя файла
    file_element = browser.find_element(By.CSS_SELECTOR, "[type='file']")
    file_element.send_keys(file_path)

    submit = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    submit.click()

finally:
    time.sleep(30)
    browser.quit()

