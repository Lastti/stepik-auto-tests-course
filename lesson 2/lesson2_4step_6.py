from selenium import webdriver
from selenium.webdriver.common.by import By
import math

link = 'http://suninjuly.github.io/cats.html'
browser = webdriver.Chrome()
browser.get(link)
browser.find_element_by_id("button")



