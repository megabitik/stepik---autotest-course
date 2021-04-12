import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
import time
import math


links = ['https://stepik.org/lesson/236895/step/1',
         'https://stepik.org/lesson/236896/step/1',
         'https://stepik.org/lesson/236897/step/1',
         'https://stepik.org/lesson/236898/step/1',
         'https://stepik.org/lesson/236899/step/1',
         'https://stepik.org/lesson/236903/step/1',
         'https://stepik.org/lesson/236904/step/1',
         'https://stepik.org/lesson/236905/step/1']

the_big_answer = []


def get_answer():
    return str(math.log(int(time.time())))


@pytest.mark.parametrize('link', links)
def test_get_next_msg(browser, link):
    browser.get(link)
    wait = WebDriverWait(browser, 10)

    # Wait for the loading of textarea
    tarea = wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, 'textarea.string-quiz__textarea')))
    tarea.send_keys(get_answer())
    send_button = wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, 'button.submit-submission')))
    send_button.click()

    message_pre = wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, 'pre.smart-hints__hint')))
    msg = message_pre.text
    print('Message #{}: {}'.format(links.index(link), msg))

    if msg != 'Correct!':
        the_big_answer.append(msg)

def test_reveal_answer():
    print('The answer:', ''.join(the_big_answer))