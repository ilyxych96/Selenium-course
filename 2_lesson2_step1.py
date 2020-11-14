from selenium import webdriver
import time 
import math
from selenium.webdriver.support.ui import Select


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
  
link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    x_element = browser.find_element_by_id('num1')
    x = x_element.text
    y_element = browser.find_element_by_id('num2')
    y = y_element.text
    z = str(int(x) + int(y))
    print(z)
    select = Select(browser.find_element_by_id("dropdown"))
    select.select_by_visible_text(z)
    button = browser.find_element_by_css_selector("button")
    button.click()

    


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()