from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import Select


try:
    # link = "http://suninjuly.github.io/registration1.html"  # old registration form
    # link = "http://suninjuly.github.io/registration2.html"
    # link = 'http://suninjuly.github.io/math.html'
    link = 'http://suninjuly.github.io/selects1.html'
    browser = webdriver.Chrome()
    browser.get(link)

    # Fill the form
    a = browser.find_element_by_id("num1").text
    b = browser.find_element_by_id("num2").text
    answer = int(a) + int(b)
    print(answer)
    select = Select(browser.find_element_by_id("dropdown"))
    select.select_by_visible_text(str(answer))

    # Submit
    browser.find_element_by_css_selector('button.btn.btn-default').click()

finally:
    sleep(10)
    browser.quit()
