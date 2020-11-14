from selenium import webdriver
import time 
import math
from selenium.webdriver.support.ui import Select


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
  
link = "http://SunInJuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    y = calc(x)
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(str(y))
    browser.execute_script("window.scrollBy(0, 200);")
    option1 = browser.find_element_by_css_selector('[for="robotCheckbox"]').click()
    option2 = browser.find_element_by_id("robotsRule").click()
    select = Select(browser.find_element_by_id("dropdown"))
    select.select_by_visible_text(z)
    button = browser.find_element_by_css_selector("button")
    button.click()
    


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()