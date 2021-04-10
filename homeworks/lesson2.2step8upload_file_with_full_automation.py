from selenium import webdriver
from time import sleep
import os

USERNAME = ''  # Enter your Stepik login (e-mail)
PASSWORD = ''  # Enter your Stepik password

try:
    link = 'http://suninjuly.github.io/file_input.html'
    browser = webdriver.Chrome()
    browser.get(link)

    for i in browser.find_elements_by_css_selector('div.form-group input'):
        i.send_keys('asdf')

    with open('file.txt', 'w') as tmpfile:
        tmpfile.write(' ')

    filepath = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'file.txt')
    browser.find_element_by_id('file').send_keys(filepath)

    # Submit
    browser.find_element_by_css_selector('button.btn').click()
    sleep(1)
    alert = browser.switch_to.alert
    the_answer = alert.text.split()[-1]
    alert.accept()
    sleep(1)

    browser.get('https://stepik.org/catalog?auth=login')
    sleep(8)
    elem = browser.find_element_by_id('id_login_email')
    elem.click()
    elem.send_keys(USERNAME)
    elem = browser.find_element_by_id('id_login_password')
    elem.click()
    elem.send_keys(PASSWORD)
    browser.find_element_by_css_selector('button.sign-form__btn').click()
    sleep(3)
    browser.get('https://stepik.org/lesson/228249/step/8?unit=200781')
    sleep(8)
    browser.find_element_by_tag_name('textarea').send_keys(the_answer)
    browser.find_element_by_css_selector('button.submit-submission').click()

finally:
    sleep(10)
    browser.quit()