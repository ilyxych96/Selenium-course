from selenium import webdriver
import time 
import math
from selenium.webdriver.support.ui import Select
import os 


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
  
link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    input1 = browser.find_element_by_name('firstname').send_keys('ilya')
    input2 = browser.find_element_by_name('lastname').send_keys('krysko')
    input3 = browser.find_element_by_name('email').send_keys('ilya@mail')
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'test.txt')
    element = browser.find_element_by_name('file')
    element.send_keys(file_path)
    button = browser.find_element_by_css_selector("button")
    button.click()

    

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()