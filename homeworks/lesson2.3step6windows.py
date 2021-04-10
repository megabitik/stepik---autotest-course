from selenium import webdriver
from time import sleep
from math import log, e, sin

USERNAME = 'megabitik@gmail.com'
PASSWORD = '7COOp1IWrH9S&g@7W*o47b4jHxUni6'

try:
    link = 'http://suninjuly.github.io/redirect_accept.html'
    browser = webdriver.Chrome()
    browser.get(link)

    # Click the button
    browser.find_element_by_css_selector('button.btn').click()

    browser.switch_to.window(browser.window_handles[1])

    x = browser.find_element_by_id('input_value').text
    answer = log(abs(12 * sin(int(x))), e)
    browser.find_element_by_id('answer').send_keys(str(answer))
    browser.find_element_by_css_selector('button.btn').click()
    alert = browser.switch_to.alert
    the_answer = alert.text.split()[-1]
    alert.accept()

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

    browser.get('https://stepik.org/lesson/184253/step/6?unit=158843')
    sleep(8)
    browser.find_element_by_tag_name('textarea').send_keys(the_answer)
    browser.find_element_by_css_selector('button.submit-submission').click()

finally:
    sleep(10)
    browser.quit()
