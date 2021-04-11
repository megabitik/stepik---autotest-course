from selenium import webdriver
from time import sleep
import unittest

links = ['http://suninjuly.github.io/registration1.html',
         'http://suninjuly.github.io/registration2.html']


def register(link):
    browser = webdriver.Chrome()
    browser.get(link)

    # Fill the form
    browser.find_element_by_css_selector('div.first_block > div.form-group.first_class > '
                                         '.first').send_keys('asdf')
    browser.find_element_by_css_selector('div.first_block > div.form-group.second_class > '
                                         'input').send_keys('asdf@ya.ru')
    browser.find_element_by_class_name('form-control.third').send_keys('asdf')

    # Submit
    browser.find_element_by_css_selector('button.btn.btn-default').click()

    sleep(2)

    return browser.find_element_by_tag_name("h1").text


class TestRegistration(unittest.TestCase):
    def test_registration(self):
        for link in links:
            self.assertEqual("Congratulations! You have successfully registered!",
                             register(link), "Couldn't register")


if __name__ == "__main__":
    unittest.main()
