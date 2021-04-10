from selenium import webdriver
from time import sleep
import os

try:
    link = 'http://suninjuly.github.io/file_input.html'
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element_by_css_selector('[name="firstname"]').send_keys('michael'.capitalize())
    browser.find_element_by_css_selector('[name="lastname"]').send_keys('jackson'.capitalize())
    browser.find_element_by_css_selector('[name="email"]').send_keys('abra@cadabra.com')

    filepath = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'file.txt')
    browser.find_element_by_id('file').send_keys(filepath)
    print(filepath)

    # Submit
    browser.find_element_by_css_selector('button.btn').click()

finally:
    sleep(5)
    browser.quit()
