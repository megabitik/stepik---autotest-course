from selenium import webdriver
import time
from math import log, e,sin

try:
    link = 'http://suninjuly.github.io/get_attribute.html'
    browser = webdriver.Chrome()
    browser.get(link)

    # Fill the form
    x = browser.find_element_by_id('treasure').get_attribute('valuex')
    answer = log(abs(12 * sin(int(x))), e)
    browser.find_element_by_id('answer').send_keys(str(answer))

    browser.find_element_by_id("robotCheckbox").click()
    browser.find_element_by_id("robotsRule").click()

    # Submit
    time.sleep(5)
    browser.find_element_by_css_selector('button.btn.btn-default').click()

finally:
    time.sleep(10)
    browser.quit()
